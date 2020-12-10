n=5
arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]
result=["#####","# # #", "### #", "#  ##", "#####"]

def find(n, arr1,arr2):
    result=[]
    for i in range(n):
        tmp=bin(arr1[i]|arr2[i])[2:]
        tmp = tmp.replace('0', ' ')
        tmp=tmp.replace('1','#')
        while len(tmp)<n:
            tmp=" "+tmp
        result.append(tmp)
    return result

print(find(n,arr1,arr2))