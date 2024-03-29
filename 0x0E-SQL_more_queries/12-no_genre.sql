-- List title and genre_id of all tv shows without no genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_shows LEFT OUTER JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id
 WHERE tv_shows.id IS NULL
    OR tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id
