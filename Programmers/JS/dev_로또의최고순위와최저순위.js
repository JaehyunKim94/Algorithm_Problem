function solution(lottos, win_nums) {
  var answer = [];
  var res = 0;
  var anon = 0;
  for (var idx in lottos) {
    var lotto = lottos[idx];
    if (lotto == 0) {
      anon += 1;
    } else if (win_nums.includes(lotto)) {
      res += 1;
    }
  }
  var rank = {
    6: 1,
    5: 2,
    4: 3,
    3: 4,
    2: 5,
    1: 6,
    0: 6,
  };
  answer.push(rank[anon + res]);
  answer.push(rank[res]);
  return answer;
}
