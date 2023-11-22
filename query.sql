--SELECT
SELECT * FROM MOVIE
--advanced SELECT
SELECT title ,AVG(r.score) AS avg_score
FROM review r
    GROUP BY title
   HAVING AVG(r.score) < (SELECT movie.avg_score 
                            FROM movie
                            WHERE movie.title =r.title);
--INSERT
INSERT INTO OWN (Own_ID, Customer_ID, Title)
VALUES (19, 1, 'The Godfather')

--DELETE
DELETE FROM MODERATOR WHERE MOD_ID = 1

