function solution(array, commands) {
    var answer = [];
    commands.forEach(function(e, i) {
        var targetArr = array.slice(e[0]-1, e[1])
        targetArr.sort(function(a, b) {
            // if(a > b) return 1;
            // if(a===b) return 0;
            // if(a < b) return -1;
            return a-b;
        })
        answer[i] = targetArr[e[2]-1]
    })
    return answer;
}