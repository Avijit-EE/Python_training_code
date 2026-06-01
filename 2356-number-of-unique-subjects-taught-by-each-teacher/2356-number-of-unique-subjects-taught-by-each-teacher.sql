# Write your MySQL query statement below
select TEACHER_ID , COUNT(DISTINCT SUBJECT_ID) AS cnt
from TEACHER  GROUP BY TEACHER_ID