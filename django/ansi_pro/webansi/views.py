# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect,HttpResponse
from webansi.models import Group,Hosts,Module,Args
import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C
# Create your views here.

def mainpage(request):
    return render(request,'webansi/mainpage.html')

def index(request):
    return render(request,'webansi/hostsinfo.html')

def addhosts(request):
    if request.method=='POST':
        g = request.POST.get('group')
        h = request.POST.get('hostname')
        ip = request.POST.get('ipaddr')
        groupobj = Group.objects.get_or_create(group=g)[0]
        Hosts.objects.get_or_create(hostname=h,ip_addr=ip,group=groupobj)

    host_info={}
    groups = Group.objects.all()
    for group in groups:
        hosts = []
        for host in group.hosts_set.all():
            hosts.append(host.hostname)
        host_info[group] = hosts
    return render(request,'webansi/addhosts.html', {'host_info': host_info})

def addmodules(request):
    if request.method == 'POST':
        modename = request.POST.get('module')
        arg = request.POST.get('args')
        moduleobj = Module.objects.get_or_create(mod_name=modename)[0]
        Args.objects.get_or_create(mod_args=arg,mod=moduleobj)

    module_info = {}
    mods = Module.objects.all()
    for m in mods:
        argss=[]
        for args in m.args_set.all():
            argss.append(args.mod_args)
        module_info[m] = argss
    return render(request,'webansi/addmodules.html', {'module_info':module_info})

def tasks(request):
    if request.method=='POST':
        ip = request.POST.get('ipaddr')
        group = request.POST.get('group')
        mod = request.POST.get('module')
        args = request.POST.get('args')
        print ip,group,mod,args
        if ip :
            dest = ip
        else:
            dest = group
        exec_task (dest,mod,args)

    hosts = list(Hosts.objects.all())
    groups = list(Group.objects.all())
    mod_info = {}
    mods = Module.objects.all()
    for m in mods:
        argss = []
        for args in m.args_set.all():
            argss.append(args.mod_args)
        mod_info[m] = argss
    result = {'hosts':hosts,'groups':groups,'mods':mods,'args':args,'mod_info':mod_info}
    return render(request, 'webansi/task.html',result)

def exec_task(dest,mod,args):
    Options = namedtuple('Options',
                         ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check',
                          'diff'])
    options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
                      become_user=None, check=False, diff=False)

    loader = DataLoader()
    passwords = dict()

    inventory = InventoryManager(loader=loader, sources=['ansicfg/dhosts.py'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source = dict(
        name="Ansible Play",
        hosts=dest,
        gather_facts='no',
        tasks=[
            dict(action=dict(module=mod, args=args), register='shell_out'),
        ]
    )

    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

    tqm = None
    try:
        tqm = TaskQueueManager(
            inventory=inventory,
            variable_manager=variable_manager,
            loader=loader,
            options=options,
            passwords=passwords,
        )
        result = tqm.run(play)
    finally:
        if tqm is not None:
            tqm.cleanup()

        shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)











