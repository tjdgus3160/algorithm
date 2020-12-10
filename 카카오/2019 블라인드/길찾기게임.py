# hint: y좌표 기준 정렬하고 이진트리라 x값만 비교하면 됌, 이진 트리 클래스로 구현
import sys
sys.setrecursionlimit(10**9)

class node(object):
    def __init__(self,id,x,left=None,right=None):
        self.id=id
        self.left=left
        self.right=right
        self.x=x

def solution(arr):
    res = []
    tree=sorted([[i+1,dot[0],dot[1]] for i,dot in enumerate(arr)],key=lambda x:(-x[2],x[1]))
    root=None
    for idx,x,y in tree:
        if root== None:
            root=node(idx,x)
            continue
        tmp=root
        while True:
            if tmp.x<x:
                if tmp.right==None:
                    tmp.right=node(idx,x)
                    break
                tmp=tmp.right
            elif tmp.x>x:
                if tmp.left==None:
                    tmp.left=node(idx,x)
                    break
                tmp=tmp.left
    tmp=[]
    def pre(node):
        tmp.append(node.id)
        if node.left:
            pre(node.left)
        if node.right:
            pre(node.right)
    pre(root)
    res.append(tmp)
    tmp=[]
    def pos(node):
        if node.left:
            pos(node.left)
        if node.right:
            pos(node.right)
        tmp.append(node.id)
    pos(root)
    res.append(tmp)
    return res

arr=[[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(arr))