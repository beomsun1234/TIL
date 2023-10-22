## LOAD DATA - csv 업로드
   show global variables like 'local_infile';
   
   set global local_infile=true;

   mysql --local_infile -u root -p

   //LOAD DATA 
   LOAD DATA LOCAL INFILE '/marcap-2022-insert.csv' INTO TABLE stock_day FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
