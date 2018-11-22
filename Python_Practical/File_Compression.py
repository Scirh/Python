# Author Scon
# -*- coding utf-8 -*-
# help()


import tarfile
import time
import subprocess

dt = time.strftime('%Y-%m-%d', time.localtime())
time = time.asctime()  # 转换时间元组
alist = time.split(' ')  # 将获取的时间,分割存储为列表

# 增量备份
def sync():
    subprocess.call('rsync -a  --delete /tongbu  /mnt/rsync_files', shell=True)

# 每周一完全备份一次
def compression(filename='/mnt/'):
    with tarfile.open(filename + '/' + 'backup-' + dt + '.tar.gz', 'w:gz') as fobj:
        fobj.add('/mnt/rsync_files')


if __name__ == '__main__':

    if alist[0] == 'Mon':
        compression()
    else:
        sync()

# 结合Linux的定时计划任务可以实现定时备份
＃➜ /  mnt ji crontab  -l
#  0 18 * * * /usr/local/bin/python3 /mnt/python/File\ Compression.py


#解压文件:
# with tarfile.open('/mnt/demo.tar.gz') as fobj:
#     fobj.extractall()
