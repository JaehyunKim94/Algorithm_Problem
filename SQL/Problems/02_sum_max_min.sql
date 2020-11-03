'''
Programmers Sum, Max, Min Problem 1 - 최댓값 구하기
  가장 최근에 들어온 동물의 DATETIME 조회
  MAX() 이용할 경우 쉽게 구할 수 있으나 두 번째 방법은 ORDER BY 와 LIMIT을 설정해서 출력
  결과는 같다.
'''
SELECT MAX(DATETIME) FROM ANIMAL_INS;
SELECT DATETIME FROM ANIMAL_INS ORDER BY DATETIME DESC LIMIT 1;


'''
Programmers Sum, Max, Min Problem 2 - 최솟값 구하기
  가장 최근에 들어온 동물의 DATETIME 조회
  MIN() 사용
'''
SELECT MIN(DATETIME) FROM ANIMAL_INS;

'''
Programmers Sum, Max, Min Problem 3 - 동물 수 구하기
  테이블의 데이터 수를 조회
  COUNT() 사용
'''
SELECT COUNT(ANIMAL_ID) FROM ANIMAL_INS;

'''
Programmers Sum, Max, Min Problem 4 - 중복 제거하기
  DISTINCT <컬럼명> 사용 
'''
SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS;