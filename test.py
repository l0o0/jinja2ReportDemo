import os
import sys
import json
import pprint

pp = pprint.PrettyPrinter()
init_dict = {'dirs':{},'files':[]}

def path_to_dict(path, init_dict):
    d = init_dict
    for x in os.listdir(path):
        if os.path.isdir(os.path.join(path, x)):
            print 'dir:', x
            if x not in d['dirs']:
                d['dirs'][x] = {'dirs':{},'files':[]}
            d['dirs'][x]= path_to_dict(os.path.join(path,x), d['dirs'][x])
        else:
            print 'file:', x
            d['files'].append(x)
    
    return d

mydict = path_to_dict(sys.argv[1], init_dict)
pp.pprint(mydict)
