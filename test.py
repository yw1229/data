import os
path='C:/Users/Yuanwei/Desktop/yw/'
a =1
for i in os.listdir(path):
    os.rename(path+i,path+str(a)+'.jpg')
    a +=1