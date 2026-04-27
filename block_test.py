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
check=True if input("check?")=="y" else False
mx=5
my=7
seed_num=4
maxn=4;minn=0#blocks num range
random.seed(seed_num)
#it is more easly than that 1st dimension is y line for falling process
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
turnednum=0
game_ov=False
blocklib=list("▧▤▦▩▥")
blocks=[[blocklib[num_makein_range(random.random())] for j in range(my)]for i in range(mx)]
to4=[
    [0,1],
    [0,-1],
    [1,0],
    [-1,0]]
def checking(text,hensu={"":""},sltime=0):#かさばるのが嫌だ
    text="|"+text+"_"
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
def turn90(blocks,left=False):
    """blocksを90度回転させる。left=Trueなら左回転、Falseなら右回転"""
    checking("Function:turn90")
    sy=len(blocks[0])
    sx=len(blocks)
    bl_turn90=[]
    for _ in range(sy):
        bl_turn90.append([0]*sx)
    for lowdx in range(sx):
        for linedx in range(sy):
            if left:
                bl_turn90[linedx][sx-1-lowdx]=blocks[lowdx][linedx]
            else:
                bl_turn90[sy-1-linedx][lowdx]=blocks[lowdx][linedx] 

    return bl_turn90

def show_blocks(blocks,justrow=False):
    checking("Function:show_blocks")
    sy=len(blocks[0])
    sx=len(blocks)
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
    sx=len(blocks)
    sy=len(blocks[0])
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
    did=[fis_penguin[0:2]]#killed and will broaken orz
    while len(que)>0:
        q=que.pop(0)
        for s in to4:
            pl=[q[0]+s[0],q[1]+s[1]]#上下左右
            if pl[0]<0 or pl[1]<0 or pl[0]>=sx or pl[1]>=sy:
                continue
            else:
                b=blocks[pl[0]][pl[1]]  #試験体
            if b==keynum:
                if not pl in did:
                    did.append(pl)
                    que.append(pl)
    if len(did)<lim:
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
        while ok<sy and len(low)>1:
            b=low[0]
            for adx in range(1,len(low)):
                a=low[adx]
                
                if a>b:
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
            blocks[x].append(".")
    return blocks
def tikanENP(blocks,taikiblock):
    for lowdx in range(len(blocks)):
        for linedx in range(len(blocks[0])):
            if blocks[lowdx][linedx]==".":
                blocks[lowdx][linedx]=taikiblock[0]
                taikiblock=taikiblock[1:]
                taikiblock+=blocklib[num_makein_range(random.random())]
    return blocks,taikiblock
taikiblock=""
for i in range(20):
    taikiblock+=blocklib[num_makein_range(random.random())]

show_blocks(blocks)
while not game_ov:
    dx=max([mx,my])+1
    dy=max([mx,my])+1
    while dx>=mx or dy>=my:
        delplace=[input("X位置:"),input("Y位置:")]
        if (delplace[0])=="check":
            check=True if input("check?")=="y" else False
            delplace=[input("X位置:"),input("Y位置:")]
        dx=int(delplace[0])-1
        dy=int(delplace[1])-1
        if dx>=mx or dy>=my:
            print("again plz")
    for t in to4:
        tx=dx+t[0]
        ty=dy+t[1]
        if tx<0 or ty<0 or tx>=len(blocks) or ty>=len(blocks[0]):
            continue
        blocks=break_block(blocks,[tx,ty,blocks[tx][ty]])
        show_blocks(blocks)
        
        blocks,taikiblock=tikanENP(blocks,taikiblock)
    blocks=turn90(blocks)
    """
    ####juts del the pushed block####
    deln=blocks[dx].pop(dy)
    blocks[dx].append(num_makein_range(random.random()))"""

    show_blocks(blocks)
    print(taikiblock)