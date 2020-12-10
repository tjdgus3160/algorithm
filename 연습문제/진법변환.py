# 지정숫자(문자열), 기존 진법, 변환 진법
def convert(number, base1, base2):
    strings= "0123456789ABCDEF"
    result=""
    tmp=int(number,base1)
    while tmp > 0:
        digit = tmp % base2
        result = strings[digit] + result
        tmp = tmp // base2
    return result

print(convert("1",2,16))