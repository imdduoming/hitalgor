from typing import List
import re
def check(dic,str,k):
    # k=1~5
    s=''
    for i in range(k):
        c = re.sub("([a-z]){1}", '..', str)
        s +=c
    




def solution(k: int, dic: List[str], chat: str) -> str:
    answer = ''
    result=[]
    chats=list(chat.split(' '))
    print(chats)
    for word in chats:
        print(word)
        if word in dic:
            word = '#'*(len(word))
            result.append(word)
        else:
            check(dic,word,k)
    return result

print(solution(2,["slang","badword"],"badword ab.cd"))