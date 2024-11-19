#모듈 설치하기
#pip install numpy
#pip install matplotlib

import random
import numpy as np
import matplotlib.pyplot as plt

num = 30

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

def remove_Re(data):
  result = []
  for i in data:
    if i not in result:
      result.append(i)
  data = result

# start_algorism
random_v1 = range(num)
random_v2 = random.choices(random_v1,k=2)
PastWay.append(random_v2)

while True:
  PassingWay.append([PastWay[-1][0],PastWay[-1][1]+1])
  PassingWay.append([PastWay[-1][0],PastWay[-1][1]-1])
  PassingWay.append([PastWay[-1][0]+1,PastWay[-1][1]])
  PassingWay.append([PastWay[-1][0]-1,PastWay[-1][1]])
  start_list_remove(PassingWay,PastWay)
  remove_Re(PassingWay)
  
  if not PassingWay:
    print("end_point :",PastWay[-1])
    for i in range(num):
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

  for item in PastWay:
    for i in l10:
      if item == i:
        l11.append(item)
  random_v4 = random.choice(l11)
  l12.append([random_v3,random_v4])
  Direct_inform(random_v3,random_v4)
  PastWay.append(random_v3)
  PassingWay.remove(random_v3)
  

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