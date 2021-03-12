function solution(numbers, target) {
    var answer = 0;
    
    function BFS(idx, number, numbers, target) {
    if (idx === numbers.length){
        if (number === target) {
             answer += 1
        }
    } else {
        var i = idx + 1
        var plusNum = number + numbers[idx]
        var minusNum = number - numbers[idx]
        BFS(i, plusNum, numbers, target)
        BFS(i, minusNum, numbers, target)
    }
}
    BFS(0, 0, numbers, target)
    return answer;
}