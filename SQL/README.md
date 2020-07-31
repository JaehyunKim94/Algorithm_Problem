# Algorithm - SQL

SQL 문제를 풀기 위해 SQL 문법을 정리해놓은 문서입니다. 

## SQL 문법

- `SELECT`

  - 조회

    ```mysql
    -- Select All
    SELECT * FROM <table>;
    
    -- Select using AND/OR
    SELECT * FROM <table> WHERE <조건식1> AND <조건식2>;
    
    -- Select column with limits
    SELECT * FROM <table_name> LIMIT 2,2; 
    ```



- `GROUP BY`

  - 특정 칼럼을 기준으로 데이터를 그룹핑

    ```mysql
    -- Group cloumn
    SELECT <column> FROM <table> GROUP BY <target_coulumn>;
    
    -- Group column using option
    SELECT <column> FROM <table> WHERE <조건식> GROUP BY <target_column>;
    
    -- 조건처리 (HAVING)
    SELECT <column> FROM <table> GROUP BY <target_column> HAVING <조건식>
    ```

  - **WHERE과 HAVING의 차이**

    - WHERE: 모든 필드를 조건에 둘 수 있습니다.

    - HAVING: 그룹핑된 새로운 테이블에 조건을 주게 됩니다

    - 예시

      | column1 | column2    |
      | ------- | ---------- |
      | 1       | 인사       |
      | 2       | hi         |
      | 2       | hello      |
      | 3       | 안녕하세요 |
      | 3       | 안녕       |

      ```mysql
      SELECT column1, COUNT(column2) AS cnt FROM <table> WHERE column1<3 GROUP BY column1 HAVING cnt>1;
      /* 결과
      |  column1	|  cnt	|
      |  2		|  2	|
      */
      ```



- `JOIN`

  - 복수의 테이블을 하나의 테이블처럼 출력

    ![join1](./images/join1.png)

    - INNER JOIN
      - 조인하려는 테이블 모두에 데이터가 존재하는 행에 대해서만 결과를 출력(교집합)
    - OUUTER JOIN
      - 매칭되는 데이터가 없는 경우 null로 표시되어 결과를 출력
      - LEFT JOIN
        - 레프트
      - RIGHT JOIN
        - 라이트

    