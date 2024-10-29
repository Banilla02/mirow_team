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

PastWay = []
PassingWay = []
l10 = []
l11 = []
random_v1 = []
random_v2 = []
random_v3 = []
To_remove = []

def start_list_remove(list_1,list_2):
  To_remove = []
  for i in range(len(list_1)):
    if list_1[i][0] > 4 or list_1[i][1] > 4:
      To_remove.append(list_1[i])
    elif list_1[i][0] < 0 or list_1[i][1] < 0:
      To_remove.append(list_1[i])
    for j in range(len(list_2)):
      if list_1[i][0] == list_2[j][0] and list_1[i][1] == list_2[j][1]:
        To_remove.append(list_1[i]) 
        
  for i in range(len(To_remove)):
    if To_remove[i] in list_1:
      print("삭제할 값:",To_remove[i])
      list_1.remove(To_remove[i])


random_v1 = range(5)
random_v2 = random.choices(random_v1,k=2)
PastWay.append(random_v2)
print("star_point :",random_v2)

PassingWay.append([PastWay[-1][0],PastWay[-1][1]+1])
PassingWay.append([PastWay[-1][0],PastWay[-1][1]-1])
PassingWay.append([PastWay[-1][0]+1,PastWay[-1][1]])
PassingWay.append([PastWay[-1][0]-1,PastWay[-1][1]])
print("spread_start_point :",PastWay)
print("will_passing_way",PassingWay)


start_list_remove(PassingWay,PastWay)
random_v3 = random.choice(PassingWay)
print("passing way에서 갈 방향",random_v3)
l10.append([random_v3[0],random_v3[1]+1])
l10.append([random_v3[0],random_v3[1]-1])
l10.append([random_v3[0]+1,random_v3[1]])
l10.append([random_v3[0]-1,random_v3[1]])
start_list_remove(l10,PassingWay)
print("",l10)
for i in l10:
  if PastWay[i] in l10:
    l11.append(PastWay[i])
print(l11)


