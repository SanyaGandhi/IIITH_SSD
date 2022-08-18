show databases;
use COMPANY; 
select Distinct Fname, Minit, Lname, Ssn, Dno, Dname FROM EMPLOYEE JOIN DEPARTMENT WHERE Dno IN ( select Dnumber from DEPARTMENT where Mgr_ssn IN (select distinct Essn FROM WORKS_ON where Hours < "40.0"));