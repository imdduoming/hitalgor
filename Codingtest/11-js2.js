function solution(N, K) {
    // write your code in JavaScript (Node.js 8.9.4)
    let b = new Array(N + 1);
    for (let i = N; i >= 1; i--) {
        b[i] = i;
    }
    let total = 0;
    let cnt = 0;

    for (let i = N; i >= 1; i--) {
        total += b[i]
        cnt += 1;
        // console.log(total)
        // console.log(cnt)
        if (total >= K)
            break;
    }
    // console.log(b)
    if (total < K) {
        return -1;

    }
    else{
        return cnt;
    }
}


console.log(solution(2,2));