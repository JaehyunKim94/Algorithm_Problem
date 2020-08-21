function solve(params) {
    if (params.number > answer){
        return params
    } else {
        ck = true
        for(i=0; i<params.count; i++){
            num = params.num_list[i]
            if (params.number % num == 0) {
                ck = false
                break
            };
        };
    };
};

function solution(n) {
    var answer = 0;
    parameter = {
        num_list: [],
        number: 1,
        count: 1
    };
    solve(parameter);
    return answer;
}