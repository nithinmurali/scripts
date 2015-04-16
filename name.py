#!/usr/bin/python

import os
import sys
import argparse

folder = '.'

parser = argparse.ArgumentParser()
parser.add_argument('-s',"--start",nargs='?',default =0,type = int)
args = parser.parse_args()

if args.start:
    start = args.start
else:
    start = 0

i = start 
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
