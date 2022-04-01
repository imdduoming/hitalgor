import sys
from collections import deque
from itertools import combinations

input=sys.stdin.readline
N,K=map(int,input().split())
words=[]
for i in range(N):
    words.append(input().rstrip()[4:-4])
first_word = {'a','n','t','i','c'}

remain_alphabet = set(chr(i) for i in range(97, 123)) - first_word

def count_word(words,learned):
    cnt=0
    for word in words:
        canread=1 #읽을 수 있는게 디폴트
        for w in word:
            #배웠는지 확인
            if learned[ord(w)]==0:
                canread=0
                break
        if canread ==1:
            cnt+=1
    return cnt


answer=0
if K<5:
    print(0)
else:
    learned = [0] * 123
    for x in first_word:
        learned[ord(x)] = 1

    for select in list(combinations(remain_alphabet,K-5)):
        for alpha in select:
            learned[ord(alpha)]=1
        cnt=count_word(words,learned)
        answer=max(answer,cnt)
        for alpha in select:
            learned[ord(alpha)]=0
    print(answer)