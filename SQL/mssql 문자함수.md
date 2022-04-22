## mssql 문자열 함수

### ASCII

    //문자를 아스키코드로 변환
    //SELECT ASCII('변환할 문자')
    SELECT ASCII('A') -> 65
    
### CHAR

   //아스키코드를 문자로 변환
   //SELECT CHAR('변환할 숫자')
   SELECT CHAR(65) -> A
   
### LEFT, RIGHT

   //문자열 왼쪽부터 지정한 수 만큼 문자 반환(LEFT)
   SELECT LEFT('ABCD', 2) -> AB
   
   //문자열 오른쪽 부터 지정한 수 만큼 문자열 반환(RIGHT)
   SELECT RIGHT('ABCD',2) -> CD
   
### LEN

    //문자열의 길이 반환
    SELECT LEN('ABCD') -> 4
    
### UPPER, LOWER
    
    //대문자를 변환(UPPER)
    SELECT UPPER('abc') -> ABC
    
    //소문자로 변환(LOWER)
    SELECT LOWER('ABC') -> abc
    
    
