#coding:utf-8
import string
import numpy as np
## from matplotlib import pyplot as plt


def data_set():
    f = open('lsmdata1_test.csv','r')

    all_list = list() 

    for row in f:
        all_list.extend(row.split())

    f.close()

    x = list()
    y = list()
    count = 0

    for item in all_list:
        if count % 2 == 0 :
            x.append( all_list[count] )
            print(all_list[count])
        else :
            y.append( all_list[count] )

        count += 1

    print(x)
    print(y)




