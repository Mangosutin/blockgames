"""
first,I test a method of game "neighbor blocks kill":puri name
Now,I make 5*5 and just fall down vertion.
number range =1~9
"""
import random
import numpy
import time
def num_makein_range(num):
    """0~1を受け取ってminとmaxの間にはめ込む。(整数)"""
    return int(num*(maxn-minn+1)+minn)
sx=5
sy=5
seed_num=4
maxn=9;minn=1#blocks num range
random.seed(seed_num)
#it is more easly than that 1st dimension is y line for falling process
blocks=[[num_makein_range(random.random()) for j in range(sy)]for i in range(sx)]
"""
seed_num=4
y
5  1 2 2 2 8 
4  2 7 1 8 8 
3  4 8 2 8 7 
2  1 9 3 8 6 
1  3 4 5 9 3 

0  1 2 3 4 5 x
"""
game_ov=False
to4=[
    [0,1],
    [0,-1],
    [1,0],
    [-1,0]]
def checking(text,hensu={"":""},sltime=.1):#かさばるのが嫌だ
    text="|"+text+"_"
    check=True#debug printing bool
    if check:
        keys=list(hensu.keys())
        """変数の中身を確認したければdictで渡してくれれば見れるで👍"""
        if len(hensu.keys())<2:
            print(text,keys[0],":",hensu[keys[0]])
        else:
            print(text)
            print("|_____")
            for k in keys:
                print("|",k,":",hensu[k])
            print("|_____")
    time.sleep(sltime)
def show_blocks(blocks,justrow=False):
    checking("Function:show_blocks")
    if justrow:
        for low in blocks:
            print(low)  
    else:
        #----list's law and line is reversed.So,first turn 90.
        checking("  Process:turn 90")
        bl_turn90=[]
        for low in range(sy):
            bl_turn90.append([])
            for obj in blocks:
                obj=obj[::-1]
                bl_turn90[-1].append(obj[low])
        #----make the text object for print
        pri="y\n"
        #show_justrow(bl_turn90)
        checking("  Process:make list format")
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
        checking("FIN Function:show_blocks")
        return pri
def break_block(blocks,fis_penguin,lim=3):
    ###########
    """___break_blockは、
    blocks(すべてのブロックの配置),
    fis_penguin(消去されるブロック1つの情報、ここから伝染的に消去) 形式:[x,y,keynum]
    lim(いくつ以上隣接したら破壊するか)
    を受け取り、一つの群を破壊したblocks（配置）を返す。"""
    ###########
    checking("Function:break_block")
    checking("  Process:look for team which will be breaked Orz")
    """first_penguinの周囲の群を検出する。"""
    keynum=fis_penguin[2]#break blocks that is same num this
    que=[fis_penguin[0:2]]#i will kill the list
    did=[]#killed and will broaken orz
    while len(que)>0:
        checking("      part:in While fis",{"q":que})
        q=que.pop(0)
        for s in to4:
            pl=[q[0]+s[0],q[1]+s[1]]#上下左右
            try:
                b=blocks[pl[0]][pl[1]]  #試験体
            except IndexError:
                continue
            if b==keynum:
                if not pl in did:
                    did.append(pl)
                    que.append(pl)
    if len(did)+1<lim:
        return blocks
    """列ごとに処理するためにdidを列ごとに整理する。"""
    xydid={}
    for x in range(sx):
        xydid[x]=[]
    checking("  Process:put each lows some of...",{"did":did}) 
    for d in did:
        checking("      Part:d in did",{"d":d})
        xydid[d[0]]=xydid[d[0]]+[d[1]]
    checking("  Process:sort the list xydid",{"xydid":xydid})
    """xydid、ブロックが消えて落下したときにその上のブロックの座標が変わるため、
    上から順に消す必要がある⇒各列をソートする。"""

    for lowdx in list(xydid.keys()):
        low=xydid[lowdx]
        checking("      Part:I will sort each low",{"low":low})
        ok=0
        while ok<sy and len(low)>0:
            b=low[0]
            for adx in range(1,len(low)):
                a=low[adx]
                
                if a<b:
                    low[adx]=b
                    low[adx-1]=a
                else:
                    ok+=1
                checking("      Part:let's look ")
                b=a
    """breakするブロックのリストが整理できたので壊します"""
    checking("  Process:break the blocks",{"xydid":xydid})
    for x in range(sx):
        for y in xydid[x]:
            blocks[x].pop(y)
            blocks[x].append(num_makein_range(0))
    return blocks



show_blocks(blocks)
while not game_ov:
    delplace=[input("X位置:"),input("Y位置:")]
    dx=int(delplace[0])-1
    dy=int(delplace[1])-1
    blocks=break_block(blocks,[dx,dy,blocks[dx][dy]])
    """
    ####juts del the pushed block####
    deln=blocks[dx].pop(dy)
    blocks[dx].append(num_makein_range(random.random()))"""

    show_blocks(blocks)
