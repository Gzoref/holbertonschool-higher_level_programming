-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT name AS 'genre', COUNT(*) AS 'number_of_shows'
FROM tv_genres, tv_show_genres
WHERE tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
