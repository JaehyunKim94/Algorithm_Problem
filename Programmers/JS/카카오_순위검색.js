function solution(info, query) {
  var answer = [];
  var applyObject = {};
  for (var idx in info) {
    var infoString = info[idx];
    var infoList = infoString.split(" ");
    var applyString =
      infoList[0][0] + infoList[1][0] + infoList[2][0] + infoList[3][0];
    if (applyObject[applyString]) {
      applyObject[applyString].push(Number.parseInt(infoList[4]));
    } else {
      applyObject[applyString] = [Number.parseInt(infoList[4])];
    }
  }

  function getSearchList(q, lst, allList) {
    var newList = [];
    if (lst.length) {
      if (q === "-") {
        for (var k in lst) {
          for (var m in allList) {
            newList.push(lst[k] + allList[m]);
          }
        }
      } else {
        for (var k in lst) {
          newList.push(lst[k] + q);
        }
      }
    } else {
      if (q === "-") {
        newList = allList;
      } else {
        newList = [q];
      }
    }
    return newList;
  }

  for (var idx in query) {
    var q = query[idx];
    var queryList = q.split(" and ");
    var foodScore = queryList[3].split(" ");
    var res = 0;
    queryList[3] = foodScore[0];
    queryList[4] = Number.parseInt(foodScore[1]);
    var searchList = getSearchList(queryList[0][0], [], ["j", "c", "p"]);
    searchList = getSearchList(queryList[1][0], searchList, ["b", "f"]);
    searchList = getSearchList(queryList[2][0], searchList, ["j", "s"]);
    searchList = getSearchList(queryList[3][0], searchList, ["c", "p"]);
    for (var i in searchList) {
      var search = searchList[i];
      var targetList = applyObject[search];
      for (var tg in targetList) {
        if (targetList[tg] >= queryList[4]) {
          res += 1;
        }
      }
    }
    answer.push(res);
  }

  return answer;
}

// 2021.05.04 - 시간초과 발생중