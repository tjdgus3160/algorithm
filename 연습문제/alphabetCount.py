# 가장 많이 등장하는 알파벳의 개수 구하기

word = "test"

def alphabetCount(string):
    dict={}
    for c in string:
        if c in dict:
            dict[c]+=1
        else:
            dict[c]=1
    return dict

dict=alphabetCount(word)
print(dict)
dict=sorted(dict.items(), key=lambda a:a[1], reverse=True)
print(dict)
print(dict[0][1])