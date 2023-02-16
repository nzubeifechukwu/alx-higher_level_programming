-- List all comedy shows in a tv show database
SELECT tv_shows.title
  FROM tv_shows
 INNER JOIN (
	tv_show_genres
      INNER JOIN tv_genres
	 ON tv_show_genres.genre_id = tv_genres.id
)
    ON tv_shows.id = tv_show_genres.show_id
 WHERE tv_genres.name = 'Comedy'
 ORDER BY tv_shows.title
