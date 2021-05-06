/*
https://programmers.co.kr/learn/courses/30/lessons/76501?language=javascript
*/

function solution(absolutes, signs) {
    var answer = 0;
    for (var i in absolutes) {
        var num = absolutes[i];
        if (signs[i]) {
            answer += num;
        } else {
            answer -= num;
        }
    }
    return answer;
}