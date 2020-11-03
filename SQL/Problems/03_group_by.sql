'''
Programmers Group by Problem 1 - 고양이와 개는 몇마리 있을까
  ANIMAL_TYPE을 기준으로 count 한 값을 나타내준다.
  HAVING 뒤의 문장은 고양이와 개를 제외한 다른 동물의 종류가 있을 경우를 대비하여 추가한 구문
  조회 순서가 있을 경우 ORDER BY를 추가해주자.
'''
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS 'count' FROM ANIMAL_INS GROUP BY ANIMAL_TYPE HAVING (ANIMAL_TYPE='Cat' or ANIMAL_TYPE='Dog') ORDER BY ANIMAL_TYPE ASC;

'''
Programmers Group by Problem 2 - 동명 동물 수 찾기
  HAVING 문에 COUNT를 추가하여 중복된 이름의 동물수만 조회
  Null 값을 체크할 경우 NAME != Null 이 아닌 IS NULL 을 사용
'''
SELECT NAME, COUNT(NAME) AS 'COUNT' FROM ANIMAL_INS GROUP BY NAME HAVING (COUNT > 1 AND NOT(NAME IS NULL) ) ORDER BY NAME ASC;

'''
Programmers Group by Problem 3 - 입양 시각 구하기(1)
  DATETIME의 속성을 다뤄봄
  YEAR(날짜), MONTH(날짜), DAY(날짜), HOUR(날짜), MINUTE(날짜), SECOND(날짜)로 원하는 타입의 자료형을 뽑을 수 있음
'''
SELECT HOUR(DATETIME) AS HOUR, COUNT(HOUR(DATETIME)) AS COUNT FROM ANIMAL_OUTS GROUP BY HOUR HAVING (HOUR>=9 AND HOUR <20) ORDER BY HOUR ASC;

'''
Programmers Group by Problem 3 - 입양 시각 구하기(2)
  테이블에 없는 컬럼도 생성해야 함 - 변수 생성
  SET은 SQL문에 변수를 생성하는 것으로 
  @hours 가 23보다 작을 떄 까지 +1 이 된다
'''
SET @hours = -1;
SELECT (@hours := @hours + 1) AS HOUR, (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hours) AS COUNT FROM ANIMAL_OUTS WHERE @hours < 23;