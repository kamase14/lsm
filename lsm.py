#coding:utf-8
import string
import numpy as np
import matplotlib.pyplot as plt


f = open('lsmdata1_test.csv','r')

all_list = list() 

for row in f:
    all_list.extend(row.split())

f.close()


x = list()
y = list()
count = 0

for item in all_list:
    
    if count % 2 :
        x.append(all_list[count])
        print(all_list[count])
    
    else :
        y.append( all_list[count] )
        
    count += 1

array_x =[float(f) for f in np.array(x)]
array_y =[float(f) for f in np.array(y)]


print(type(array_x[1]),array_y)

plt.scatter(array_x,array_y,label="sample")


lsm_result = np.poly1d(np.polyfit(array_x,array_y,1))

plt.plot(np.linspace(-30,30,100),lsm_result(np.linspace(-30,30,100)),label="result")
plt.show()





