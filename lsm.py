#coding:utf-8
import string
import numpy as np
import matplotlib.pyplot as plt


f = open('lsmdata4_train.csv','r')
degrees = 1

all_list = list() 

for row in f:
    all_list.extend(row.split())

f.close()


x = list()
y = list()
count = 0

for item in all_list:
   
    # 1.14514 1.919810 みたいな感じで書かれてるcsvファイルを空白で区切ってリストに追加してる
    # 区切った回数が偶数のときはxに要素が入る 奇数のときはyに要素が入る
    if count % 2 :
        x.append(all_list[count])
        print(all_list[count])
    
    else :
        y.append( all_list[count] )
        
    count += 1

#21行目のforループはstr型でリストに追加しているので、ここでfloat型になおす
array_x =[float(f) for f in np.array(x)]
array_y =[float(f) for f in np.array(y)]

min_x = np.min(array_x)
min_y = np.min(array_y)

max_x = np.max(array_x)
max_y = np.max(array_y)

#インポートしたcsvをグラフにプロット
plt.scatter(array_x,array_y,label="sample")


#サンプルをもとに最小二乗法の関数を計算
lsm_result = np.poly1d(np.polyfit(array_x,array_y,degrees))

#グラフにプロットする
#np.linspace()は指定範囲に等間隔な点を生成する関数 使い方は調べてください
plt.plot(np.linspace(min_x,max_x,10000),lsm_result(np.linspace(min_x,max_x,10000)),label="result")

# plt.xlim(min_x-5,max_x+5)
# plt.ylim(min_y-5,max_y+5)

plt.show()





