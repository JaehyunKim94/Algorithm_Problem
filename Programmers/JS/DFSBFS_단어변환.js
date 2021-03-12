function solution(begin, target, words) {
  var answer = 0;
  var visit = new Array(words.length);
  function wordCheck(wordA, wordB) {
    var res = 0;
    for (var i = 0; i < wordA.length; i++) {
      if (wordA[i] !== wordB[i]) {
        res += 1;
      }
    }
    if (res === 1) return true;
  }
  function DFS(now, visit, cnt) {
    if (now === target) {
      if (answer === 0) {
        answer = cnt;
      } else {
        if (cnt < answer) {
          answer = cnt;
        }
      }
      return;
    }
    for (var i = 0; i < words.length; i++) {
      var tgWord = words[i];
      if (visit[i] !== 1) {
        if (wordCheck(tgWord, now)) {
          var nxtCnt = cnt + 1;
          visit[i] = 1;
          DFS(tgWord, visit, nxtCnt);
          visit[i] = 0;
        }
      }
    }
  }
  DFS(begin, visit, 0);
  return answer;
}
