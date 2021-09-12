class Node(object):
    def __init__(self,key,data=None):
        self.key=key    # 이전 글자, 어디서 왔는지
        self.data=data  # 조건, 끝나는점 ex, Terminal
        self.remain_length={} # 하위에 존재하는 단어 길이별 개수
        self.children={}    # 하위 트리들

class Trie(object):
    def __init__(self):
        self.head=Node(None)

    def insert(self,string):
        curr_node=self.head

        remain_length=len(string)
        curr_node.remain_length.setdefault(remain_length, 0)
        curr_node.remain_length[remain_length] += 1
        for char in string: # 한 글자씩 확인인
            if char not in curr_node.children:  # 하위 트리에 없는 경우
                curr_node.children[char]=Node(char)
            curr_node=curr_node.children[char]  # 하위 트리로 이동

            remain_length-=1
            curr_node.remain_length.setdefault(remain_length, 0)
            curr_node.remain_length[remain_length] += 1

        curr_node.data=string   # 마지막엔 data에 문자열을 넣어 종료했음을 알림

    def search(self,string,target):    # 검색한 문자열이 존재하는지 확인

        curr_node=self.head
        for char in string: # 하위 트리로 이동
            if char in curr_node.children:
                curr_node=curr_node.children[char]
                if curr_node.data==target or (not curr_node.data and len(curr_node.remain_length.items())==1 and list(curr_node.remain_length.values())[0]==1):
                    return True
            else:   # 하위 트리가 없으면 False
                return False
        return bool(curr_node.data==target or (not curr_node.data and len(curr_node.remain_length.items())==1 and list(curr_node.remain_length.values())[0]==1))  # 현재 트리에 종료 문자열이 있는지 확인

def solution(words):
    t = Trie()
    for word in words:
        t.insert(word)
    res = 0
    for word in words:
        for i in range(1,len(word)+1):
            if t.search(word[:i],word):
                res+=i
                break
    return res

words=["wo", "word", "work"]
print(solution(words))