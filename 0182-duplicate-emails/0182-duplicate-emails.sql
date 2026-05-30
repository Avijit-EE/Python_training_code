# Write your MySQL query statement below
SELECT EMAIL AS Email FROM PERSON GROUP BY Email HAVING COUNT(*)>1;