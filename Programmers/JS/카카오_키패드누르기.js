var distance = {
  1: {
    2: 1,
    5: 2,
    8: 3,
    0: 4,
  },
  2: {
    2: 0,
    5: 1,
    8: 2,
    0: 3,
  },
  3: {
    2: 1,
    5: 2,
    8: 3,
    0: 4,
  },
  4: {
    2: 2,
    5: 1,
    8: 2,
    0: 3,
  },
  5: {
    2: 1,
    5: 0,
    8: 1,
    0: 2,
  },
  6: {
    2: 2,
    5: 1,
    8: 2,
    0: 3,
  },
  7: {
    2: 3,
    5: 2,
    8: 1,
    0: 2,
  },
  8: {
    2: 2,
    5: 1,
    8: 0,
    0: 1,
  },
  9: {
    2: 3,
    5: 2,
    8: 1,
    0: 2,
  },
  "*": {
    2: 4,
    5: 3,
    8: 2,
    0: 1,
  },
  0: {
    2: 3,
    5: 2,
    8: 1,
    0: 0,
  },
  "#": {
    2: 4,
    5: 3,
    8: 2,
    0: 1,
  },
};

function click(l, r, n, mainHand) {
  var res = 0;
  if ((n == 1) | (n == 4) | (n == 7)) {
    res = 1;
  } else if ((n == 3) | (n == 6) | (n == 9)) {
    res = 2;
  } else {
    var l_dist = distance[l][n];
    var r_dist = distance[r][n];
    if (l_dist === r_dist) {
      res = mainHand;
    } else if (l_dist < r_dist) {
      res = 1;
    } else {
      res = 2;
    }
  }

  if (res == 1) {
    return [n, r, "L"];
  } else {
    return [l, n, "R"];
  }
}

function solution(numbers, hand) {
  var answer = "";
  var lp = "*";
  var rp = "#";
  var isLeft;
  if (hand === "left") {
    isLeft = 1;
  } else {
    isLeft = 2;
  }
  for (var idx in numbers) {
    var number = numbers[idx];
    var res = click(lp, rp, number, isLeft);
    lp = res[0];
    rp = res[1];
    answer += res[2];
  }

  return answer;
}
