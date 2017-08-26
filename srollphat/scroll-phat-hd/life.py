#!/usr/bin/env python
#Original code by joosteto, updated to run on scroll-phat-hd by alexmburns.

import copy
import random
import time

import scrollphathd


def scroll_life(delay):
    def count_neighbours(ibuf, i, j):
        tot=0
        for x,y in ((-1,-1), (-1,0), (-1,1),
                    ( 0,-1)         , (0,1),
                    (+1,-1), (+1,0), (+1,1)):
            ix=(i+x)%11
            jy=(j+y)%5
            tot+=ibuf[ix][jy]
        return tot
    
    def buffer(ibuf):
        return [ibuf2buf[tuple(v)] for v in ibuf]
    
    def rand_ibuf():
        return [[(random.random()>0.8)+0 for j in range(5)] for i in range(11)]
    
    def glider_ibuf():
        return [[0,0,0,0,0], 
                [0,0,0,0,0], 
                [0,0,0,0,0], 
                [0,0,1,0,0], 
                [0,1,0,0,0], 
                [0,1,1,1,0], 
                [0,0,0,0,0], 
                [0,0,0,0,0], 
                [0,0,0,0,0], 
                [0,0,0,0,0], 
                [0,0,0,0,0]]          

    ibuf=rand_ibuf()
    ibuf2buf={(i,j,k,l,m): (i<<0)+(j<<1)+(k<<2)+(l<<3)+(m<<4)
              for i in (0,1)
              for j in (0,1)
              for k in (0,1)
              for l in (0,1)
              for m in (0,1)}
    samecount=0
    while True:
        ibufbuf=copy.deepcopy(ibuf)
        for i in range(11):
            for j in range(5):
                c=count_neighbours(ibufbuf, i, j)
                if ibuf[i][j]:
                    if c in (0,1,4,5,6,7):
                        ibuf[i][j]=0
                else:
                    if c in (3,):
                        ibuf[i][j]=1
        buf=buffer(ibuf)
	scrollphathd.set_brightness(0.5)
        scrollphathd.write_string(buf)
        scrollphathd.show()
	scrollphathd.clear()
        time.sleep(delay)
        if ibufbuf==ibuf:
            samecount+=1
        if samecount>20:
            ibuf=rand_ibuf()
            
if __name__== "__main__":
    scroll_life(0.1)
