'''
Programmers Select Problem 1 - 모든 레코드 조회하기
  주어진 테이블의 요소들을 ANIMAL_ID 순으로 출력
  ORDER BY (요소) ASC/DESC
'''
SELECT * FROM ANIMAL_INS ORDER BY ANIMAL_ID ASC;

'''
Programmers Select Problem 2 - 역순 정렬하기
  주어진 테이블의 동물의 이름과 보호 시작일을 ANIMAL_ID의 역순으로 출력
  Problem 1의 ORDER BY (요소) DESC
'''
SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC;

'''
Programmers Select Problem 3 - 아픈 동물 찾기
  특정한 조건의 컬럼만 ANIMAL_ID 순으로출력
  WHWER (조건문)
'''
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION = 'Sick' ORDER BY ANIMAL_ID ASC;

'''
Programmers Select Problem 4 - 어린 동물 찾기
  Problem 3의 WHERE 사용으로 CONDITION이 AGED가 아닌 동물을 ANIMAL_ID 순으로출력
'''
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION != 'Aged' ORDER BY ANIMAL_ID ASC;

'''
Programmers Select Problem 5 - 동물의 아이디와 이름
  모든 동물들의 아이디와 이름을 ANIMAL_ID 순으로 조회
'''
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS ORDER BY ANIMAL_ID ASC;

'''
Programmers Select Problem 6 - 여러 기준으로 정렬하기
 아이디와 이름, 보호 시작일을 기준으로 조회
'''
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS ORDER BY NAME ASC, DATETIME DESC;

'''
Programmers Select Problem 7 - 상위 n개 레코드
  가장 최근에 들어온 동물의 이름을 조회
  조회되는 컬럼의 양을 조절 - LIMIT
'''
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1;