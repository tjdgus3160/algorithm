import re

def solution(new_id):
    new_id=new_id.lower()
    new_id=re.sub('[^a-z\d._\-]','', new_id)
    new_id=re.sub('\.+','.', new_id)
    new_id=re.sub('^[.]|[.]$','', new_id)
    new_id='a' if not len(new_id) else new_id[:15]
    new_id=re.sub('^[.]|[.]$','', new_id)
    if len(new_id)<=2:
        new_id=new_id.ljust(3,new_id[-1])
    return new_id