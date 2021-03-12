function solution(brown, yellow) {
  var answer = [];
  var total = brown + yellow;
  function getNumber(num, total) {
    var otherSide = total / num;
    var checkBrown = 2 * (num + otherSide) - 4;
    var checkYellow = total - checkBrown;
    return [checkBrown, checkYellow];
  }
  for (var i = 2; i < total; i++) {
    if (total % i === 0) {
      var numSet = getNumber(i, total);
      console.log(numSet);
      if (numSet[0] === brown && numSet[1] === yellow) {
        answer[1] = total / i;
        answer[0] = i;
      }
    }
  }
  return answer;
}
