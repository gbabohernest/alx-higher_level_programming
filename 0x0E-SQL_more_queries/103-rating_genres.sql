-- A script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating

SELECT name, SUM(rate) AS rating
FROM tv_genres AS genres
INNER JOIN tv_show_genres AS show
ON show.genre_id = genres.id
INNER JOIN tv_show_ratings AS rate_tv_show
ON rate_tv_show.show_id = show.show_id
GROUP BY name
ORDER BY rating DESC;
