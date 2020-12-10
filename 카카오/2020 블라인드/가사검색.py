# hint: 트라이 사용, 하위 트리 글자길이 별 개수 관리

class Node(object): # Trie Node 구성
    def __init__(self,key):
        self.key=key    # 시작값
        self.remain_length={}   # Terminal까지 남아있는 문자열의 길이
        self.children={}    # 자식

class Trie(object):
    def __init__(self):
        self.head=Node(None)

    def insert(self,string):
        curr_node=self.head

        # 문자열 길이 딕셔너리 저장
        remain_length=len(string)
        curr_node.remain_length.setdefault(remain_length,0)
        curr_node.remain_length[remain_length]+=1

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char]=Node(char)
            curr_node=curr_node.children[char]
            remain_length-=1
            curr_node.remain_length.setdefault(remain_length, 0)
            curr_node.remain_length[remain_length] += 1

    def search_count(self,string,check_length): # string-> 검색 키워드, check_length -> ?의 개수수
        cur_node=self.head

        if check_length+len(string) not in cur_node.remain_length:
            return 0

        for char in string:
            if char not in cur_node.children:   # 찾는 키워드가 없는 경우
                return 0
            cur_node=cur_node.children[char]

        if check_length not in cur_node.remain_length:
            return 0
        return cur_node.remain_length[check_length]

def solution(words,queries):
    t=Trie()        # 정방향
    inv_t=Trie()    # 역방향
    for word in words:
        t.insert(word)
        inv_t.insert(word[-1::-1])

    answer=[]
    for i in queries:
        if i[0]=='?':
            i=i[-1::-1]
            chars=i.replace('?',"")
            check_length=len(i)-len(chars)
            answer.append(inv_t.search_count(chars,check_length))
        else:
            chars=i.replace("?","")
            check_length=len(i)-len(chars)
            answer.append(t.search_count(chars,check_length))
    return answer

words=["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries=["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words,queries))


