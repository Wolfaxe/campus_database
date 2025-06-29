
-- Sorgu 1: Tüm binaları getir
SELECT * FROM planet_osm_polygon 
WHERE building IS NOT NULL;

-- Sorgu 2: Kampüs merkezine 500 metre mesafedeki binaları getir
SELECT * FROM planet_osm_polygon
WHERE building IS NOT NULL AND
ST_DWithin(
    way,
    ST_SetSRID(ST_MakePoint(29.01682, 41.11076), 4326)::geography,
    500
);

-- Sorgu 3: Kafeleri getir (noktalar)
SELECT * FROM planet_osm_point 
WHERE amenity = 'cafe';

