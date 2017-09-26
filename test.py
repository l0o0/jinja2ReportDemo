# -*- coding: utf-8 -*-

import os
import sys
import pprint
from jinja2 import Environment, FileSystemLoader

pp = pprint.PrettyPrinter()
init_dict = {'dirs':{},'files':[]}

def path_to_dict(path, init_dict):
    d = init_dict
    for x in os.listdir(path):
        if x == '.git':
            continue
        if os.path.isdir(os.path.join(path, x)):
            print 'dir:', x
            if x not in d['dirs']:
                d['dirs'][x] = {'dirs':{},'files':[]}
            d['dirs'][x]= path_to_dict(os.path.join(path,x), d['dirs'][x])
        else:
            print 'file:', x
            d['files'].append(x)
    
    return d

if __name__ == "__main__":
    #mydict = path_to_dict(sys.argv[1], init_dict)
    #pp.pprint(mydict)
    temp_dir = os.path.join(os.path.abspath('.'), 'templates')
    # 读取目录的结果
    dir_tree = path_to_dict(os.path.abspath('.'), init_dict)
    # 设置jinja2的环境配置
    env = Environment(
                    loader = FileSystemLoader(temp_dir),
                    extensions = ['jinja2.ext.do']                                                                       )

    # 读取模板文件
    report = env.get_template('report.html')
    # 将字典传递到模板中，进行渲染
    with open('dirA/dirB2/Tophat-Mapping2Genome.stat.xls') as handle:
        tophat = handle.readlines()
        tophat = [x.strip().split('\t') for x in tophat]

    html = report.render(dir_tree = dir_tree, tophat = tophat)

    with open('Report.html', 'w') as handle:
        handle.write(html.encode('utf-8'))
