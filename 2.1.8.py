import random
a=10
l1=list([15]*a)
l2=[] # l2는 맵
for i in range(a):
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
v4=0
v5=0
l4=(v4,v5)
v6=1
l5=[]
l7=[]
l5.append([v4,v5]) #얘는 다저장
l7.append([v4,v5]) #얘는 삭제가능
while len(l7)!=0:  #while l4!=(v4,v5) or v6==1:
  l6=[]
  for i in range(2):
    for i2 in range(2):
      if i==0:
        if 0<=l7[-1][0]-1+2*i2<=a-1 and 0<=l7[-1][1]<=a-1 and [l7[-1][0]-1+2*i2,l7[-1][1]] not in l5:
          l6.append([l7[-1][0]-1+2*i2,l7[-1][1]])
      else:
        if 0<=l7[-1][0]<=a-1 and 0<=l7[-1][1]-1+2*i2<=a-1 and [l7[-1][0],l7[-1][1]-1+2*i2] not in l5:
          l6.append([l7[-1][0],l7[-1][1]-1+2*i2]) # l6은 현재 위치에서 4방향으로 갈수있는곳
  if len(l6)!=0:
    v7=random.randint(0, len(l6)-1)
    v4=l6[v7][0]
    v5=l6[v7][1]
    if l7[-1][0]==v4+1 and l7[-1][1]==v5:
      l2[v4+1][v5]=l2[v4+1][v5]-1
      l2[v4][v5]=l2[v4][v5]-4
    elif l7[-1][0]==v4-1 and l7[-1][1]==v5:
      l2[v4-1][v5]=l2[v4-1][v5]-4
      l2[v4][v5]=l2[v4][v5]-1
    elif l7[-1][0]==v4 and l7[-1][1]==v5+1:
      l2[v4][v5+1]=l2[v4][v5+1]-2
      l2[v4][v5]=l2[v4][v5]-8
    elif l7[-1][0]==v4 and l7[-1][1]==v5-1:
      l2[v4][v5-1]=l2[v4][v5-1]-8
      l2[v4][v5]=l2[v4][v5]-2
    l5.append([v4,v5]) #얘는 다저장
    l7.append([v4,v5]) #얘는 삭제가능
  else:
    l7.pop()

l2[0][0]=l2[0][0]-2
l2[-1][-1]=l2[-1][-1]-8

import numpy as np
import matplotlib.pyplot as plt

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
