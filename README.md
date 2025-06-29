# Geospatial Database Project – ITU Ayazağa Campus

This project is a spatial database implementation using PostgreSQL and PostGIS. It models a real-world campus environment (ITU Ayazağa) with buildings, roads, and POIs like cafes.

## 📁 Project Contents

| File Name                        | Description                                      |
|----------------------------------|--------------------------------------------------|
| `CBS_Uzamsal_Veritabanı_Raporu.pdf` | 📄 Project report in PDF format                |
| `CBS_Uzamsal_Veritabanı_Raporu.docx` | Word version of the project report             |
| `kampus_db_schema.sql`          | SQL schema export of the PostGIS database       |
| `sorgular.sql`                  | Spatial SQL queries used in the project         |
| `map.osm`                       | Source OSM file used for importing spatial data |
| `kampus.qgz`, `kampus1.qgz`     | QGIS project files with visualized layers       |
| `Cafes.py`, `Imagination with py.py` | Python files for query visualization        |
| `.png` files (Buildings, Cafes) | Generated visuals from queries                  |

## ✅ Queries Implemented

1. **List all buildings within a 500m radius of the campus center**
2. **Show all cafes near the main buildings**
3. **Find cafes located alongside roads**

All queries were visualized using Python (GeoPandas, Matplotlib) and QGIS.

## 🛠 Technologies

- **PostgreSQL + PostGIS**
- **Python 3.12** (GeoPandas, SQLAlchemy, Psycopg2, Matplotlib)
- **QGIS**
- **osm2pgsql** (OSM → PostgreSQL conversion)

## 📌 Notes

- The database name used is: `kampus_db`
- All geometries use SRID: 4326 (WGS 84)
- Visuals are exported as PNG images
