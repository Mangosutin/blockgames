"""
first,I test a method of game "neighbor blocks kill":puri name
Now,I make 5*5 and just fall down vertion.
number range =1~9
"""
import random
import numpy
sx=5
sy=5
seed_num=4
maxn=9;minn=1#blocks num range
random.seed(seed_num)
#it is more easly than that 1st dimension is y line for falling process
blocks=[[int((random.random()*(maxn-minn+1)+minn)) for j in range(sy)]for i in range(sx)]
game_ov=False
def show_justrow(blocks):
    for low in blocks:
        print(low)
def show_blocks(blocks):
    #----list's law and line is reversed.So,first turn 90.
    bl_turn90=[]
    for low in range(sy):
        bl_turn90.append([])
        for obj in blocks:
            obj=obj[::-1]
            bl_turn90[-1].append(obj[low])
    #----make the text object for print
    pri="y\n"
    #show_justrow(bl_turn90)
    for linedx in range(sy):
        pri+=str(len(bl_turn90)-linedx)+"  "
        for obj in bl_turn90[linedx]:
            pri+=str(obj)+" "
        pri+="\n"
    pri+="\n0 "
    for i in range(sx):
        pri+=" "+str(i+1)
    pri+=" x"
    print(pri)
    return pri
show_blocks(blocks)
while not game_ov:
    delplace=[input("X位置:"),input("Y位置:")]
    dx=int(delplace[0])-1
    dy=int(delplace[1])-1
    deln=blocks[dx].pop(dy)
    blocks[dx].append(0)
    show_blocks(blocks)