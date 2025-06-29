SELECT name, building, way
FROM planet_osm_polygon
WHERE building IS NOT NULL 
	AND ST_DWithin(
		way,
		ST_Transform(ST_SetSRID(ST_MakePoint(29.025,41.105),4326),3857),
		500
	);