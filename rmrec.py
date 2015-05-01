#!/usr/bin/python

import os
import sys
import argparse
import datetime

folder = '.'

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

parser = argparse.ArgumentParser()
parser.add_argument('-r',"--recent",nargs='1', action="store_true" )
parser.add_argument('-h',"--hour",nargs='1',default=0, type=int)
parser.add_argument('-m',"--minutes",nargs='1',default=0, type=int)
args = parser.parse_args()

if args.hour:
    hour = args.hour; 

for file in os.listdir(folder):
    # print file + "to" + str(i) + os.path.splitext(file)[1]
    mt = modification_date(file)
    ct = datetime.datetime.today()
    dt = ct - mt
    if args.hour:
        hour = divmod(c.days * 86400 + c.seconds, 60*60)[0]
        if hour < args.hour
            cmd = 'mv ' + file  
            os.system(cmd) 
    elif args.minutes:
        minutes = divmod(c.days * 86400 + c.seconds, 60)[0]
        if minutes < args.minutes
            cmd = 'ls'+file
            os.system(cmd)
    pass
