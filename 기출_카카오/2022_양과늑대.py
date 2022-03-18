#2022카카오블라인드 채용
# 트리 레벨3
ans=0

def solution(info, edges):
    answer = 0
    tree={}
    for i,j in edges:
        if i not in tree:
            tree[i]=[j]
        else:
            tree[i].append(j)

    ans=0


    def dfs(now, sheep, wolf, path):
        global ans

        if info[now] == 1:
            wolf += 1
        else:
            sheep += 1

        # print('sheep:', sheep, 'wolf:', wolf)
        if sheep <= wolf:
            return
        ans=max(sheep,ans)
        # print('now:', now, 'answer:', ans,'path:',path)
        for p in path:
            if p in tree:
                for i in tree[p]:
                    if i not in path:
                        path.append(i)
                        dfs(i,sheep, wolf, path)
                        path.pop()

        return ans

    ans = dfs(0,0, 0 ,[0])
    return ans



print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
