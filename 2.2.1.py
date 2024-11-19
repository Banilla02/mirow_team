#모듈 설치하기
#pip install numpy
#pip install matplotlib

import random
import numpy as np
import matplotlib.pyplot as plt

num = 10 #맵의 크기

#기본 맵 크기 정하기
#맵 15로 채워넣기
#실질적인 맵 = l2
l1=list([15]*num)
l2=[]
for i in range(num):
  l2.append(list(l1))

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

PastWay = [] #지나갔던 길
PassingWay = [] #지나갈 길
l10 = [] 
l11 = [] 
l12 = []
random_v1 = [] #처음시작지점
random_v2 = [] #갈 길에서 랜덤
random_v3 = [] #갔던 길에서 랜덤
To_remove = [] #지울 리스트 값들

#범위 이외의 값들 지우는 지정함수
def start_list_remove(list_1,list_2):
  To_remove = []
  for i in range(len(list_1)):
    if list_1[i][0] > num-1 or list_1[i][1] > num-1:
      To_remove.append(list_1[i])
    elif list_1[i][0] < 0 or list_1[i][1] < 0:
      To_remove.append(list_1[i])
    for j in range(len(list_2)):
      if list_1[i][0] == list_2[j][0] and list_1[i][1] == list_2[j][1]:
        To_remove.append(list_1[i]) 
        
  for i in range(len(To_remove)):
    if To_remove[i] in list_1:
      list_1.remove(To_remove[i])

#기본 15에서 하나씩 벽을 지워서 길을 만드는 지정함수
def Direct_inform(list_1,list_2):
  if list_1[0] == list_2[0]:
    if list_1[1]-1 == list_2[1]:
      l2[random_v3[0]][random_v3[1]] = l2[random_v3[0]][random_v3[1]] - 2
      l2[random_v4[0]][random_v4[1]] = l2[random_v4[0]][random_v4[1]] - 8

    elif list_1[1]+1 == list_2[1]:
      l2[random_v3[0]][random_v3[1]] = l2[random_v3[0]][random_v3[1]] - 8
      l2[random_v4[0]][random_v4[1]] = l2[random_v4[0]][random_v4[1]] - 2

  elif list_1[0]-1 == list_2[0]:
    l2[random_v3[0]][random_v3[1]] = l2[random_v3[0]][random_v3[1]] - 1
    l2[random_v4[0]][random_v4[1]] = l2[random_v4[0]][random_v4[1]] - 4

  elif list_1[0]+1 == list_2[0]:
    l2[random_v3[0]][random_v3[1]] = l2[random_v3[0]][random_v3[1]] - 4
    l2[random_v4[0]][random_v4[1]] = l2[random_v4[0]][random_v4[1]] - 1

#중복되는 리스트 안에 값 제거하는 지정함수
def remove_Re(data):
  result = []
  for i in data:
    if i not in result:
      result.append(i)
  data = result

# start_algorism
random_v1 = range(num)
random_v2 = random.choices(random_v1,k=2) #시작지점 정하기
PastWay.append(random_v2) #시작지점을 갔던길 리스트에 추가하기

#마지막으로 갔던 길에 앞으로 나아갈 길 추가하기
while True:
  PassingWay.append([PastWay[-1][0],PastWay[-1][1]+1])
  PassingWay.append([PastWay[-1][0],PastWay[-1][1]-1])
  PassingWay.append([PastWay[-1][0]+1,PastWay[-1][1]])
  PassingWay.append([PastWay[-1][0]-1,PastWay[-1][1]])
  start_list_remove(PassingWay,PastWay) #범위 외 값들 제거
  remove_Re(PassingWay) #중복값들 지우기
  
  #갈 길이 남아있지 않으면 while문 멈추기
  if not PassingWay:
    break

#앞으로 나아갈 방향 정하기
  random_v3 = []
  random_v3 = random.choice(PassingWay)
  l10 = []
  l10.append([random_v3[0],random_v3[1]+1])
  l10.append([random_v3[0],random_v3[1]-1])
  l10.append([random_v3[0]+1,random_v3[1]])
  l10.append([random_v3[0]-1,random_v3[1]])
  start_list_remove(l10,PassingWay)
  remove_Re(l10)
  l11 = []

#두 리스트에 있는 값만 저장하기
  for item in PastWay:
    for i in l10:
      if item == i:
        l11.append(item)
  
  #갈수 있는 방향중에 하나만 정하기
  random_v4 = random.choice(l11)
  l12.append([random_v3,random_v4])
  Direct_inform(random_v3,random_v4) #방향에 따라 벽을 지우며 길을 만든다
  PastWay.append(random_v3) #갔던 길에 길 하나를 추가한다.
  PassingWay.remove(random_v3) #추가한 길을 중복되지 않게 갈 길에서 지워준다.

#시작지점과 끝지점 뚫어주기
l2[0][0]=l2[0][0]-2
l2[-1][-1]=l2[-1][-1]-8

# 미로 데이터 (비트 플래그 형식)
maze = np.array(l2)

# 방향별 비트 플래그 (위, 왼쪽, 아래, 오른쪽)
DIRECTIONS = {
    'UP': 1,     # 0001
    'LEFT': 2,   # 0010
    'DOWN': 4,   # 0100
    'RIGHT': 8   # 1000
}

# 벽을 그리는 함수
def draw_maze(maze):
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # 각 셀에 대해 벽을 그리기
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            cell = maze[i, j]
            
            # 위쪽 벽
            if cell & DIRECTIONS['UP']:
                ax.plot([j, j+1], [i, i], color='black', lw=2)
            # 왼쪽 벽
            if cell & DIRECTIONS['LEFT']:
                ax.plot([j, j], [i, i+1], color='black', lw=2)
            # 아래쪽 벽
            if cell & DIRECTIONS['DOWN']:
                ax.plot([j, j+1], [i+1, i+1], color='black', lw=2)
            # 오른쪽 벽
            if cell & DIRECTIONS['RIGHT']:
                ax.plot([j+1, j+1], [i, i+1], color='black', lw=2)

    # 기본 틀 제거: 축, 눈금, 격자선
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_aspect('equal')
    ax.axis('off')  # 축을 아예 표시하지 않도록 설정

    plt.show()

# 미로 그리기
draw_maze(maze)