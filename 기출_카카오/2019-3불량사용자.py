def solution(user_id, banned_id):
    import re
    from itertools import permutations
    new_ban=[]
    answer=set()
    for i in banned_id:
        new_i=i.replace('*','.')
        new_ban.append(new_i)
    new_ban=','.join(new_ban)
    # print(new_ban)
    for i in permutations(user_id,len(banned_id)):
        # print(','.join(i))
        if re.fullmatch(new_ban,','.join(i)):
            # print('맞음')
            # print(''.join(i))
            answer.add(''.join(sorted(i)))
    # print(answer)
    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))