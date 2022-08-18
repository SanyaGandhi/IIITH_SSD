show databases;
use COMPANY;  
-- SELECT Fname from EMPLOYEE where Super_ssn = (SELECT Essn from WORKS_ON where ( Hours < 40.0) AND Super_ssn = Essn ;
-- SELECT Fname FROM EMPLOYEE AS t
  -- WHERE 2 >= (SELECT COUNT(*) FROM WORKS_ON WHERE WORKS_ON.Essn = t.ssn);
SELECT Essn as 'Manager ssn', count(Pno) as 'Number of projects'from WORKS_ON WHERE Essn IN (select Mgr_ssn from DEPARTMENT  As D where Dnumber =( SELECT Dnum from PROJECT where Pname = "ProductY")) group by Essn; 