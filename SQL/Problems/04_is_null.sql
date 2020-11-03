'''
Programmers IS NULL Problem 1 - 이름이 없는 동물의 아이디
  이름이 없는 동물의 id를 조회, ID 오름차순
'''
SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NULL ORDER BY NAME ASC;

'''
Programmers IS NULL Problem 2 - 이름이 있는 동물의 아이디
  이름이 있는 동물의 id를 조회, ID 오름차순
'''
SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NOT NULL ORDER BY ANIMAL_ID ASC;
'''
Programmers IS NULL Problem 3 - NULL 처리하기
  IFNULL을 사용하여 NULL일 경우를 처리해준다
'''
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name'), SEX_UPON_INTAKE FROM ANIMAL_INS ORDER BY ANIMAL_ID ASC;