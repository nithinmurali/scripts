#!/usr/bin/python

import os
import sys

folder = '.'
i = 0
os.system('mkdir mvtemp')
for file in os.listdir(folder):
    # print file + "to" + str(i) + os.path.splitext(file)[1]
    if str(file) == 'mvtemp':
        continue
        pass

    cmd = 'mv ' + file + " mvtemp/"+ str(i) + os.path.splitext(file)[1] 
    # print cmd
    os.system(cmd) 
    i += 1;
    # print i;
    pass
os.system('mv mvtemp/* ./');
os.system('rm -r mvtemp');