'''
Programmers Join Problem 1 - 없어진 기록 찾기
  SQL 문제의 핵심이라 할 수 있는 JOIN
  FROM에 들어오는 TABLE을 왼쪽, JOIN에 오는 테이블을 오른쪽이라 생각하자.
  두 테이블에서 ID가 같은 동물들 중 INS에 없을 경우를 조회
'''
SELECT OUTS.ANIMAL_ID, OUTS.NAME FROM ANIMAL_OUTS AS OUTS LEFT JOIN ANIMAL_INS AS INS ON OUTS.ANIMAL_ID = INS.ANIMAL_ID WHERE INS.ANIMAL_ID IS NULL;

'''
Programmers Join Problem 2 - 있었는데요 없었습니다
  두 테이블을 비교하여 ID값이 같은 동물들의 다른 속성을확인해줍니다.
  WHERE은 조건문이 들어간다고 생각하니 편함.
'''
SELECT INS.ANIMAL_ID, INS.NAME FROM ANIMAL_INS AS INS LEFT JOIN ANIMAL_OUTS AS OUTS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID WHERE OUTS.DATETIME < INS.DATETIME ORDER BY INS.DATETIME;

'''
Programmers Join Problem 3 - 오랜 기간 보호한 동물(1)
  아직 입양을 못간 동물중(OUTS에 포함되지 않은 INS) 가장 오래 보호소(ORDER BY DATETIME)에 있는 동물 3마리(LIMIT 3)
'''
SELECT INS.NAME, INS.DATETIME FROM ANIMAL_INS AS INS LEFT JOIN ANIMAL_OUTS AS OUTS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID WHERE OUTS.ANIMAL_ID IS NULL ORDER BY INS.DATETIME LIMIT 3; 


'''
Programmers Join Problem 4 - 보호소에서 중성화한 동물
  INS.SEX_UPON_INTAKE 와 OUTS.SEX_UPON_OUTCOME을 비교하여 다를 경우를 조회해준다.
  중성화를 거치지 않은 동물은 Intact, 중성화를 거친 동물은 Spayed 또는 Neutered가 적혀있으나 다른 경우만 조회해도 통과하였다.
'''
SELECT INS.ANIMAL_ID, INS.ANIMAL_TYPE, INS.NAME FROM ANIMAL_INS AS INS LEFT JOIN ANIMAL_OUTS AS OUTS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID WHERE INS.SEX_UPON_INTAKE != SEX_UPON_OUTCOME ORDER BY ANIMAL_ID ASC;