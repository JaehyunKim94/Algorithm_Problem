function solution(n, computers) {
    var answer = 0;
    var visit = new Array(n);
    
    function networking(idx, computers) {
        for(var l=0; l<n; l++){
            if(computers[idx][l] === 1){
                if(visit[l] !== 1){
                    visit[l] = 1
                    networking(l, computers)
                }
            }
        }
    }
    
    for(var i=0; i < n; i++){
        if (visit[i] !== 1){
            visit[i] = 1
            networking(i, computers)
            answer += 1
        }
    }
    
    return answer;
}