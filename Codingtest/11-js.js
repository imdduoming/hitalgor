
// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A)  {

    let b = new Array();
    for (let i=0; i<32; ++i)
    {   b[i] = 0;}
    // console.log(b)
    for (let i = 0; i < A.length; i++)
    {
        let x = 31;
        while (true) {
            // console.log(A[i])
            if(A[i]<=0)
                break;

            if (A[i] & 1 == 1)
            {
                b[x]+=1;
            }

            x-=1;
            A[i] = A[i] >> 1;
        }
    }

    let max_num;
    max_num= Number.MIN_VALUE;

    for (let a = 0; a < 32; a++) {
        max_num = Math.max(max_num, b[a]);
    }
    // console.log(max_num);
    return max_num;
}
let arr = [7, 13, 8, 2, 3];
let N = arr.length;
console.log(solution(arr));

