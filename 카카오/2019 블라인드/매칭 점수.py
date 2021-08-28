import re

def parser(target,HTML):
    url=re.search('<meta property="og:url" content="(https://[\S]*)"',HTML).group(1)
    score=0
    for word in re.findall('[a-zA-Z]+',HTML.lower()):
        if word==target.lower():
            score+=1
    link=re.findall('<a href="(https://[\S]*)"', HTML)
    print(link)
    return url,score,link

def solution(word, pages):
    word=word.lower()
    dic={}
    for idx,HTML in enumerate(pages):
        url,score,link=parser(word,HTML)
        dic[url]={'i':idx,'score':score,'link':link}
    res=0
    maxV=0
    for url, info in dic.items():
        score=info['score']
        for _url,_info in dic.items():
            if _url!=url and url in _info['link']:
                score+=_info['score']/len(_info['link'])
        if score>maxV:
            maxV=score
            res=info['i']
    return res

word='Muzi'
pages=["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution(word,pages))