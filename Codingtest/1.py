N = int(input())
words=[]

for i in range(N):
    words.append(input())
T = int(input())
for i in range(T):
    answer = 0
    word=input()
    for j in range(N):
        word_len=len(words[j])
        for k in range(1,word_len+1):
            if word==words[j][0:k]:
                answer+=1
                break
    print(answer)



