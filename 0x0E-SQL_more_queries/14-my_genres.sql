-- List all genres of the show Dexter in a tv show database
SELECT tv_genres.name
  FROM tv_genres
 INNER JOIN
 (
	tv_show_genres
	INNER JOIN tv_shows
	   ON tv_show_genres.show_id = tv_shows.id
 )
    ON tv_genres.id = tv_show_genres.genre_id
 WHERE tv_shows.title = 'Dexter'
 ORDER BY tv_genres.name;
