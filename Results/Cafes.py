import geopandas as gpd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:361002@localhost:5432/kampus_db")

sql_buildings = """
SELECT name, building, way
FROM planet_osm_polygon
WHERE building IS NOT NULL;
"""

gdf_buildings = gpd.read_postgis(sql_buildings, engine, geom_col='way')


sql_cafes = """
SELECT DISTINCT p.name, p.amenity, p.way
FROM planet_osm_point AS p
JOIN planet_osm_line AS l
  ON ST_DWithin(p.way, l.way, 30)
WHERE p.amenity = 'cafe';
"""
gdf_cafes = gpd.read_postgis(sql_cafes, engine, geom_col='way')


sql_roads = """
SELECT name, highway, way
FROM planet_osm_line
WHERE highway IS NOT NULL;
"""
gdf_roads = gpd.read_postgis(sql_roads, engine, geom_col='way')


fig, ax = plt.subplots(figsize=(12, 12))
gdf_buildings.plot(ax=ax, color='lightgray', edgecolor='black', linewidth=0.3)
gdf_cafes.plot(ax=ax, color='red', markersize=40)
gdf_roads.plot(ax=ax, color='black', linewidth=0.8)


plt.title("Yol Kenarındaki Kafeler ve Bina Katmanı")
plt.axis('off')
plt.show()