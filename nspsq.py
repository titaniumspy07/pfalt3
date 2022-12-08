# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 13:25:34 2022
@author: Aman Kumar Tiwary, titaniumspy07
"""


def nspsq(n):
    i=1
    while i**2<=n:
        if i**2==n:
            return 1
        i+=1
        def check2(c):
            while c%2==0:
                c=c//2
            while c%5==0:
                c=c//5
            while c%9==0:
                c=c//9
            if c%3==0:
                return False
            if c in (0,1,3,13,17):
                return True
            i,j=0,int(c**0.5)
            while i<=j:
                if i*i+j*j==c:
                    return True
                if i*i+j*j<c:
                    i+=1
                if i*i+j*j>c:
                    j-=1
            return False
    if check2(n):
        return 2
    while not n%4:
        n//=4
    if n%8!=7:
        return 3
    return 4
