# Author Scon
# -*- coding:utf-8 -*-
# help()

import requests
import re
import os


# 根据给出的url进行网页数据的爬取
def get_web(url, fname):
    r = requests.get(url)
    data = r.content
    with  open(fname, 'wb') as fobj:
        fobj.write(data)

    return fname


# 调用 get_web 获得图片的url
def get_picurl(fname):
    patt = r'https://[.\w/-]+\.(jpg|jpeg|png|gif)'
    repatt = re.compile(patt)
    resutle = []

    with open(fname) as fobj:
        for line in fobj:
            data = repatt.search(line)
            if data:
                resutle.append(data.group())
    return resutle


def download_pic(url):
    pic_dir = '/mnt/pic_dir'
    if not os.path.exists(pic_dir):
        os.mkdir(pic_dir)

    for pic_url in url:
        pic_name = os.path.join(pic_dir, pic_url.split('/')[-1])
        try:
            get_web(pic_url, pic_name)
        except:
            pass


if __name__ == '__main__':
    url = 'https://www.douban.com'
    fname = '/mnt/douban.html'
    get_web(url, fname)
    picurl = get_picurl(fname)
    download_pic(picurl)
