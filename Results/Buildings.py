import geopandas as gpd 
import matplotlib.pyplot as plt
from sqlalchemy import create_engine 


engine=create_engine("postgresql://postgres:361002@localhost:5432/kampus_db")

sql="""
SELECT name, building, way
FROM planet_osm_polygon
WHERE building IS NOT NULL
"""


gdf=gpd.read_postgis(sql,engine, geom_col='way')


gdf.plot(figsize=(12,12),edgecolor='black',color="lightgray")
plt.title("Bina Katmanı (planet_osm_polygon)")
plt.axis('off')
plt.show()