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

l8 = []
l9 = []
l10 = []
l11 = []
random_v1 = []
random_v2 = []
random_v3 = []
To_remove = []


random_v1 = range(5)
random_v2 = random.choices(random_v1,k=2)
l8.append(random_v2)
print(random_v1)
print(random_v2)

l9.append([l8[-1][0],l8[-1][1]+1])
l9.append([l8[-1][0],l8[-1][1]-1])
l9.append([l8[-1][0]+1,l8[-1][1]])
l9.append([l8[-1][0]-1,l8[-1][1]])
print(l8)
print(l9)

def start_list_remove(list_1):
  for i in range(len(list_1)):
    if list_1[i][0] > 4 or list_1[i][1] > 4:
      To_remove.append(list_1[i])
    elif list_1[i][0] < 0 or list_1[i][1] < 0:
      To_remove.append(list_1[i])
    for j in range(len(l8)):
      if list_1[i][0] == l8[j][0] and list_1[i][1] == l8[j][1]:
        To_remove.append(list[i])

  for item in To_remove:
    l9.remove(item)
  To_remove.clear

start_list_remove(l9)
print(l8)
print(l9)
print(To_remove)
random_v3.extend(random.choice(l9))
print(random_v3)
l10.append([random_v3[-1][0],random_v3[-1][1]+1])
l10.append([random_v3[-1][0],random_v3[-1][1]-1])
l10.append([random_v3[-1][0]+1,random_v3[-1][1]])
l10.append([random_v3[-1][0]-1,random_v3[-1][1]])
print(l10)
random_v1 = range(len(l9))
random_v2 = random.choice(random_v1,k=1)
l8[random_v2]


