import geopandas as gpd 
import matplotlib.pyplot as plt
from sqlalchemy import create_engine 


engine=create_engine("postgresql://postgres:361002@localhost:5432/kampus_db")

sql="""
SELECT name, building, way
FROM planet_osm_polygon
WHERE building IS NOT NULL
    AND ST_DWithin(
    way,
    ST_Transform(ST_SetSRID(ST_MakePoint(29.025,41.105),4326),3857),
    200
    );
"""


gdf=gpd.read_postgis(sql,engine, geom_col='way')


gdf.plot(figsize=(12,12),edgecolor='orange',color="black")
plt.title("200m Çapında Binalar")
plt.axis('off')
plt.show()