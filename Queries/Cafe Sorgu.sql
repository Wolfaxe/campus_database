SELECT DISTINCT p.name, p.amenity, p.way
FROM planet_osm_point AS p
JOIN planet_osm_line AS l
  ON ST_DWithin(p.way, l.way, 30)
WHERE p.amenity = 'cafe';