function solution(answers) {
  var answer = [];
  var ansList = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
  ];
  var res = [0, 0, 0];
  answers.forEach(function (e, i) {
    if (ansList[0][i % 5] == e) {
      res[0] += 1;
    }
    if (ansList[1][i % 8] == e) {
      res[1] += 1;
    }
    if (ansList[2][i % 10] == e) {
      res[2] += 1;
    }
  });
  console.log(res);
  var maxVal = 0;
  res.forEach(function (e, i) {
    if (e > maxVal) {
      maxVal = e;
      answer = [i + 1];
    } else if (e == maxVal) {
      answer.push(i + 1);
    }
  });
  return answer;
}
