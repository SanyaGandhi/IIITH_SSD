show databases;
use COMPANY; 
SELECT Fname, Minit, Lname, Super_ssn From EMPLOYEE Where count(ssn)= group by Super_ssn; 