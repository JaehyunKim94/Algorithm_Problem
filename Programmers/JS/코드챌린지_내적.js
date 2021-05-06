/*
https://programmers.co.kr/learn/courses/30/lessons/70128
*/
function solution(a, b) {
    var answer = 0;
    for (var i in a) {
        var num1 = a[i];
        var num2 = b[i];
        answer += num1*num2;
    }
    return answer;
}