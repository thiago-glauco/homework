# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 07:56:11 2024

@author: thiago
"""
try:
    fh = open('fear.txt')
    for line in fh:
        print( line )
finally:
    fh.close()
