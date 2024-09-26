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

random_v1 = range(5)
l7 = [0,1,2,3,4]
random_v2 = random.choices(random_v1,k=2)

l8 = []
l9 = []

l8.append(random_v2)
l9.append([l8[-1][0],l8[-1][1]+1])
l9.append([l8[-1][0],l8[-1][1]-1])
l9.append([l8[-1][0]+1,l8[-1][1]])
l9.append([l8[-1][0]-1,l8[-1][1]])
print(l8)
print(l9)
l9_Copy = l9
Numl9 = len(l9)
def start_list_remove() :
  for i in range(Numl9):
    if l9[i][0] > 4 or l9[i][1] > 4:
      print(l9_Copy[i])
      l9_Copy[i].remove(l9[i])
    elif l9[i][0] < 0 or l9[i][1] < 0:
      print(l9[i])
      l9_Copy[i].remove(l9[i])

start_list_remove()

print(l9_Copy)