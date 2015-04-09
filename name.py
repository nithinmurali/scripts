#!/usr/bin/python

import os
 
folder = '.'
i=0
for file in os.listdir(folder):
    os.rename(file, i + os.path.splittext(file)[1] )    
    i++
    pass