-- List all genres of the show "Dexter" in the database hbtn_0d_tvshows.
USE hbtn_0d_tvshows;
SELECT
    genres.name AS genre
FROM
    tv_shows
JOIN
    tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
JOIN
    genres ON tv_show_genres.genre_id = genres.id
WHERE
    tv_shows.title = 'Dexter'
ORDER BY
    genres.name ASC;
