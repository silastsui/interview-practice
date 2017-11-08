SELECT
  id,
  movie,
  description,
  rating
FROM
  CINEMA
WHERE
  mod(id, 2) = 1 and
  description != 'boring'
ORDER BY
  rating DESC;
