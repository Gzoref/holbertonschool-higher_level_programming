-- Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT tv_shows
FROM tv_genres
WHERE tv_genres.name NOT IN
(SELECT tv_genres.name
from tv_genres
JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter')
ORDER BY name ASC
