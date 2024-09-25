import random

l1=list([2]+[0]*3+[8])
l2=[[3,1,1,1,9]]
for i in range(3):
  l2.append(list(l1))
l2.append([6,4,4,4,12])
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
v4=random.randint(0, 4)
v5=random.randint(0, 4)
l4=(v4,v5)
v6=1
l5=[]
l7=[]
while v6==1:  #while l4!=(v4,v5) or v6==1:
  l5.append([v4,v5])
  l7.append([v4,v5])
  l6=[]
  for i in range(2):
    for i2 in range(2):
      if i==0:
        if 0<=v4-1+2*i2<=4 and 0<=v5<=4 and [v4-1+2*i2,v5] not in l5:
          l6.append([v4-1+2*i2,v5])
      else:
        if 0<=v4<=4 and 0<=v5-1+2*i2<=4 and [v4,v5-1+2*i2] not in l5:
          l6.append([v4,v5-1+2*i2])
  if len(l6)!=0:
    v7=random.randint(0, len(l6)-1)
    v4=l6[v7][0]
    v5=l6[v7][1]
  else:
    v8=0
    v9=len(l7)-1
    while v8!=1:
      l6=[]
      for i in range(2):
        for i2 in range(2):
          if i==0:
            if 0<=v4-1+2*i2<=4 and 0<=v5<=4 and [v4-1+2*i2,v5] not in l5:
              l6.append([v4-1+2*i2,v5])
          else:
            if 0<=v4<=4 and 0<=v5-1+2*i2<=4 and [v4,v5-1+2*i2] not in l5:
              l6.append([v4,v5-1+2*i2])
      if len(l6)!=0:
        l8=[]
        if v9==len(l7)-1:
          if l7[v9-1][0]+1==l7[v9][0]:
            l8.append(1)
          if l7[v9-1][0]-1==l7[v9][0]:
            l8.append(4)
          if l7[v9-1][1]+1==l7[v9][1]:
            l8.append(2)
          if l7[v9-1][1]-1==l7[v9][1]:
            l8.append(8)
        for i2 in range(4):
          v10=2**i2
          if v10 not in l8:
            if v10==1:
              pass
        else:
          pass
      else:
        v8=1
  if False:
    v6=0
  print(l5)
