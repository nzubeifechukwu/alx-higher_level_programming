-- List the number of records with same score in second_table
SELECT score, COUNT(score) AS 'number' FROM second_table
 GROUP BY score
