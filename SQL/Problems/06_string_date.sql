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
  
'''