import random
turn=0
man=1
bot=2
area=[[0,0,0],
      [0,0,0],
      [0,0,0]]
AIx,AIy=0,0
def place(x,y,player):
 if area[y][x] == 0:
  area[y][x] = player
  return True
 else:
  return False
 #
while True:
 if turn==0:#man goes
  while True: 
   if place(int(input("x:"))-1,int(input("y:"))-1,man) == True:
    turn=1
    break
 else:#bot goes
  if area[0][0]!=bot and area[0][1]!=bot and area[0][2]!=bot and area[1][0]!=bot and area[1][1]!=bot and area[1][2]!=bot and area[2][0]!=bot and area[2][1]!=bot and area[2][2]!=bot:
   AIx,AIy=random.randint(0,2),random.randint(0,2)
  while True:
   i=random.randint(0,3)
   if area[0][0]==bot:
    if i==0:     AIx,AIy=1,0
    elif i==1:     AIx,AIy=1,1
    elif i==2:     AIx,AIy=0,1
    elif i==3:     AIx,AIy=random.randint(0,2),random.randint(0,2)
   elif area[1][0]==bot:
    if i==0:     AIx,AIy=0,0
    elif i==1:     AIx,AIy=2,0
    elif i==2:     AIx,AIy=0,1
    elif i==3:     AIx,AIy=random.randint(0,2),random.randint(0,2)
   elif area[2][0]==bot:
    if i==0:     AIx,AIy=1,0
    elif i==1:     AIx,AIy=1,1
    elif i==2:     AIx,AIy=2,1
    elif i==3:     AIx,AIy=random.randint(0,2),random.randint(0,2)
   elif area[0][1]==bot:
    if i==0:     AIx,AIy=0,0
    elif i==1:     AIx,AIy=1,1
    elif i==2:     AIx,AIy=0,2
    elif i==3:     AIx,AIy=random.randint(0,2),random.randint(0,2)
   elif area[1][1]==bot:
    i=random.randint(0,4)
    if i==0:     AIx,AIy=1,0
    elif i==1:     AIx,AIy=2,1
    elif i==2:     AIx,AIy=0,1
    elif i==3:     AIx,AIy=1,2
    elif i==4:     AIx,AIy=random.randint(0,2),random.randint(0,2)
   elif area[2][1]==bot:
    if i==0:     AIx,AIy=2,0
    elif i==1:     AIx,AIy=1,1
    elif i==2:     AIx,AIy=2,0
    elif i==3:     AIx,AIy=random.randint(0,2),random.randint(0,2)
   elif area[0][2]==bot:
    if i==0:     AIx,AIy=1,2
    elif i==1:     AIx,AIy=1,1
    elif i==2:     AIx,AIy=0,1
    elif i==3:     AIx,AIy=random.randint(0,2),random.randint(0,2)
   elif area[1][2]==bot:
    if i==0:     AIx,AIy=0,2
    elif i==1:     AIx,AIy=1,1
    elif i==2:     AIx,AIy=2,2
    elif i==3:     AIx,AIy=random.randint(0,2),random.randint(0,2)
   elif area[2][2]==bot:
    if i==0:     AIx,AIy=1,2
    elif i==1:     AIx,AIy=1,1
    elif i==2:     AIx,AIy=2,1
    elif i==3:     AIx,AIy=random.randint(0,2),random.randint(0,2)
   print(i,AIx,AIy)
   if place(AIx,AIy,bot) == True:
    turn=0
    break
 print()
 print(area[0])
 print(area[1])
 print(area[2])
