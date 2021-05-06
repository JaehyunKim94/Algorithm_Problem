/*
https://programmers.co.kr/learn/courses/30/lessons/60057?language=javascript
*/

function solution(s) {
    var answer = s.length;
    var maxCut = Math.floor(s.length/2);
    var res;
    maxCut += 1;
    for (var i=1; i<maxCut; i++) {
        res = solve(s, i);
        answer = Math.min(res, answer);
    }
    return answer;
}

function solve(st, cut) {
    var res = 0;
    var beforeWord = st.substring(0, cut);
    var nowWord = "";
    var count = 1;
    var idx = cut;
    var nextIdx = idx + cut;
    while (idx < st.length) {
        nowWord = st.substring(idx, nextIdx);
        if(nowWord === beforeWord) {
            count += 1;
        } else {
            if(count === 1) {
                res += cut;
            } else {
                res += cut + count.toString().length;   // 같은 문자열이 두자리수 이상 반복될 경우를 처리
            }
            count = 1;
        }
        idx = nextIdx;
        nextIdx += cut;
        beforeWord = nowWord;
    }
    if(count === 1) {
        res += beforeWord.length;
    } else {
        res += beforeWord.length + count.toString().length;
    }
    return res;
}