function solution(new_id) {
    var answer = '';
    answer = idRecommand(new_id)
    return answer;
}

function idRecommand(id) {
    var res;
    res = stepOne(id);
    res = stepTwo(res);
    res = stepThree("", res, "", 0)
    res = stepFour(res);
    res = stepFive(res);
    res = stepSix(res);
    res = stepFour(res);
    res = stepSeven(res);
    return res;
}

// 대문자를 소문자로 치환
function stepOne(ans) {
    return ans.toLowerCase();
}

// 허용되는 문자 외의 모든 문자 제거
function stepTwo(ans) {
    return ans.replace(/[~!@#$%^&*()=+\[\{\]\}:?,<>\/]/g, "");
}

// 마침표가 두번 이상일 경우 하나로 치환
function stepThree(s, ans, bef, idx) {
    if(idx === ans.length) {
        return s
    }
    else {
        if(bef === '.' && ans[idx] === '.') {
            return stepThree(s, ans, bef, idx+1)
        }
        else {
            return stepThree(s+ans[idx], ans, ans[idx], idx+1)
        }
    }
}

// 처음과 끝의 마침표 제거
function stepFour(ans) {
    var startIdx = 0;
    var endIdx = ans.length;
    if (ans[0] === ".") {
        startIdx = 1;
    }
    if (ans[endIdx-1] === ".") {
        endIdx -= 1
    }
    if (startIdx > endIdx) {
        return "";
    }
    return ans.substring(startIdx, endIdx);
}

// 빈 문자열일 경우 a 대입
function stepFive(ans) {
    if (ans === "") {
        return "a"
    }
    return ans
}

// 길이 15 이하로 자르기
function stepSix(ans) {
    if (ans.length > 15) {
        ans = ans.substring(0, 15)
    }
    return ans
}

// 길이가 2자 이하일 때, 길이가 3이 될때까지 마지막 문자 반복
function stepSeven(ans) {
    if (ans.length < 3) {
        var lastStr = ans[ans.length-1];
        ans += lastStr + lastStr
        return ans.substring(0, 3);
    }
    return ans
}