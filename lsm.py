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


#インポートしたcsvをグラフにプロット
plt.scatter(array_x,array_y,label="sample")


#サンプルをもとに最小二乗法の関数を計算
lsm_result = np.poly1d(np.polyfit(array_x,array_y,1))

#グラフにプロットする
#np.linspace()は指定範囲に等間隔な点を生成する関数 使い方は調べてください
plt.plot(np.linspace(-30,30,100),lsm_result(np.linspace(-30,30,100)),label="result")
plt.show()





