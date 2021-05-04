function solution(orders, course) {
  var answer = [];
  var courseCount = {};

  function getCount(tg, idx, now, cs) {
    if (idx < tg.length) {
      courseCount = getCount(tg, idx + 1, now + tg[idx], cs);
      courseCount = getCount(tg, idx + 1, now, cs);
    } else {
      if (cs.includes(now.length)) {
        if (courseCount[now]) {
          courseCount[now] += 1;
        } else {
          courseCount[now] = 1;
        }
      }
    }
    return courseCount;
  }

  for (var idx in orders) {
    var order = orders[idx];
    order = order.split("").sort().join("");
    courseCount = getCount(order, 0, "", course);
  }

  console.log(courseCount);
  for (var idx in course) {
    var num = course[idx];
    var max_cnt = 1;
    var res = [];
    for (var key in courseCount) {
      if (key.length == num) {
        var value = courseCount[key];
        if (value > 1) {
          if (value > max_cnt) {
            res = [];
            max_cnt = value;
            res.push(key);
          } else if (value == max_cnt) {
            res.push(key);
          }
        }
      }
    }
    for (var i in res) {
      answer.push(res[i]);
    }
  }
  answer = answer.sort();
  return answer;
}
