# 문자열을 숫자와 기호로 분리

string = "13+21*(3-4)"

def stringTokenizer(string):
    accu =""
    result=[]
    for c in string:
        if c in "+-*/(){}[]^":
            if accu != "":
                result.append(accu)
                accu=""
            result.append(c)
        else:
            accu+=c
            print(accu)
    return result

result = stringTokenizer(string)
print(result)