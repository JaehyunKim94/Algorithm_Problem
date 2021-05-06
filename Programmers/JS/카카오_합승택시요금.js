/*
https://programmers.co.kr/learn/courses/30/lessons/72413?language=javascript
*/

function solution(n, s, a, b, fares) {
    var answer = 100000000000;
    var distanceMap = makeArr(fares, n);
    for(var m = 0; m<n; m++) {
        for(var i=0; i<n; i++) {
            for(var j=0; j<n; j++) {
                if(distanceMap[i][m] + distanceMap[m][j]<distanceMap[i][j]) {
                    distanceMap[i][j] = distanceMap[i][m] + distanceMap[m][j]
                }
            }
        }
    }
    for(var i=0; i<n; i++) {
        var res = distanceMap[s-1][i] + distanceMap[i][a-1] + distanceMap[i][b-1];
        if(res < answer) {
            answer = res;
        }
    }
    return answer;
}

function makeArr(fares, n) {
    var distanceMap = [];
    const INF = 1000000001;
    for (var i =0; i<n; i++) {
        distanceMap[i] = [];
        for (var j =0; j<n; j++) {
            if(i===j) {
                distanceMap[i][j] = 0;
            } else {
                distanceMap[i][j] = INF;
            }
        }
    }
    for (var i=0; i<fares.length; i++) {
        var fare = fares[i];
        distanceMap[fare[0]-1][fare[1]-1] = fare[2];
        distanceMap[fare[1]-1][fare[0]-1] = fare[2];
    }
    return distanceMap;
}