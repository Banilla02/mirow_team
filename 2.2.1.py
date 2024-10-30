import random

l1=list([15]*5)
l2=[]
for i in range(5):
  l2.append(list(l1))
for i in l2:
  print(' '.join(map(str, i)))
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
l12 = []
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

def Direct_inform(list_1,list_2):
  if list_1[0] == list_2[0]:
    if list_1[1]-1 == list_2[1]:
      print('서')
      

    elif list_1[1]+1 == list_2[1]:
      print('동')

  elif list_1[0]-1 == list_2[0]:
    print('북')

  elif list_1[0]+1 == list_2[0]:
    print('남')


# start_algorism
random_v1 = range(5)
random_v2 = random.choices(random_v1,k=2)
PastWay.append(random_v2)
print("star_point :",random_v2)

PassingWay.append([PastWay[-1][0],PastWay[-1][1]+1])
PassingWay.append([PastWay[-1][0],PastWay[-1][1]-1])
PassingWay.append([PastWay[-1][0]+1,PastWay[-1][1]])
PassingWay.append([PastWay[-1][0]-1,PastWay[-1][1]])
start_list_remove(PassingWay,PastWay)
print("will_passing_way",PassingWay)

#앞으로 나아갈 방향 정하기
random_v3 = random.choice(PassingWay)
print("passing way에서 갈 방향",random_v3)
l10.append([random_v3[0],random_v3[1]+1])
l10.append([random_v3[0],random_v3[1]-1])
l10.append([random_v3[0]+1,random_v3[1]])
l10.append([random_v3[0]-1,random_v3[1]])
start_list_remove(l10,PassingWay)
print("l10의 값",l10)

for item in PastWay:
  for i in l10:
    if item == i:
      l11.append(item)
print('l10과 PastWay와 중복값',l11)
random_v4 = random.choice(l11)
l12.append([random_v3,random_v4])
print(l12)
Direct_inform(random_v3,random_v4)
print(l2)