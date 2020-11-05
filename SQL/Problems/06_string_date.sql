'''
Programmers String, Date Problem 1 - 루시와 엘라 찾기
  IN 을 이용하여 찾고자 하는 이름인지 확인한다
  SET으로 먼저 선언할 수 는 없는지..
'''
SELECT INS.ANIMAL_ID, INS.NAME, INS.SEX_UPON_INTAKE FROM ANIMAL_INS AS INS WHERE INS.NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty') ORDER BY INS.ANIMAL_ID ;

'''
Programmers String, Date Problem 2 - 이름에 el이 들어가는 동물 찾기
  String에 el이 포함된지를 조회 >> LIKE %tg_word%
'''
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE (ANIMAL_TYPE = 'Dog' AND NAME LIKE '%el%') ORDER BY NAME ASC;

'''
Programmers String, Date Problem 3 - 중성화 여부 파악하기
  중성화 여부에 따라 O,X로 표시
  CASE WHEN 을 써서 조건문을 작성  ** 끝에 END 붙이기
'''
SELECT ANIMAL_ID, NAME, CASE 
  WHEN SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%'
  THEN 'O'
  ELSE 'X' END AS '중성화'
FROM ANIMAL_INS ORDER BY ANIMAL_ID ASC;

'''
Programmers String, Date Problem 4 - 오랜 기간 보호한 동물(2)
  입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 기간이 긴 순으로 조회해야 합니다.
  1) 날짜1 - 날짜2 > OUTS.DATETIME - INS.DATETIME
  2) TIMEDIFF(단위, 날짜1, 날짜2) > TIMESTAMPDIFF(SECOND, INS.DATETIME, OUTS.DATETIME)
  SECOND, MINUTE, HOUR, DAY, WEEK, MONTH, QUARTER, YEAR
'''
SELECT INS.ANIMAL_ID, INS.NAME FROM ANIMAL_INS AS INS
LEFT JOIN ANIMAL_OUTS AS OUTS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID WHERE OUTS.ANIMAL_ID IS NOT NULL
ORDER BY TIMESTAMPDIFF(SECOND, INS.DATETIME, OUTS.DATETIME) DESC
LIMIT 2;

'''
Programmers String, Date Problem 5 - DATETIME에서 DATE로 형 변환
  DATE_FORMAT(날짜, 형식)
'''
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS '날짜' FROM ANIMAL_INS ORDER BY ANIMAL_ID;