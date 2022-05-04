## mssql hint사용하기

      //문법
      SELECT select_list
        FROM table [ (INDEX ({index_name | index_id} [, index_name | index_id ... ]))]
        
      //
      SELECT *
        FROM EMP WITH (INDEX(사용할 인덱스 명))
       WHERE enterdate BETWEEN '2022-05-01' AND '2022-05-04'
       
      //힌트여러개사용
      
      SELECT *
        FROM EMP WITH (INDEX(사용할 인덱스 명1, 사용할 인덱스 명2))
       WHERE enterdate BETWEEN '2022-05-01' AND '2022-05-04'
