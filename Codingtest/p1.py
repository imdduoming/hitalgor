def solution(registered_list, new_id):
    answer = ''
    id={}
    for i in registered_list:
        id[i]=1
    if new_id not in id:
        answer = new_id
    else:
        while True:
            flag=False
            # print(new_id)
            for i in range(len(new_id)):
                if new_id[i].isdigit():
                    flag=True
                    break
            #숫자가 없다면
            if flag==False:
                new_id = new_id+'1'
            else:
                num = int(new_id[i:])+1
                new_id = new_id[:i] + str(num)

            if new_id not in id:
                answer = new_id
                break


    return answer

print(solution(
    ["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow"))