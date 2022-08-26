M = 10;
N = 100;

function  fcheck(remain, pre) {
    if (remain < 0) return 0;
    if (remain == 0) return 1;
    var cnt = 0;
    for (var i = pre; i <= M; i++){
        cnt += fcheck(remain - i, i);
    }
    return cnt;
}

//var result = fcheck(N, 2);
//console.log(result);
console.log(fcheck(N, 2));