#!/usr/bin/python

import os
 
folder = '.'
i=0
for file in os.listdir(folder):
    os.rename(file, str(i) + os.path.splitext(file)[1] )    
    i += 1;
    pass