#l2= 맵 구성
import random

#l2를 만들기 위한 과정
l1=list([2]+[0]*3+[8])
l2=[[3,1,1,1,9]]

for i in range(3):
  l2.append(list(l1))

l2.append([6,4,4,4,12])
for i in l2:
  print(' '.join(map(str, i)))

#l31(위),2(왼),4(아래),8(오른)
l31=[]
l32=[]
l34=[]
l38=[]


for i in range(15):
  v1=8
  v2=i+1
  v3=int(v2)

  for i in range(4):
    if v3>=v1:
      globals()[f'l3{v1}'].append(v2)
      v3=v3-v1

    v1=v1//2

