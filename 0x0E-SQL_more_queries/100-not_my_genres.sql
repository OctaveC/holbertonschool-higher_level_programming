-- Use the hbtn_0d_tvshows database to list all genres
-- not linked to the show Dexter
SELECT tv_genres.name FROM tv_genres
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
AND tv_shows.title = "Dexter"
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
