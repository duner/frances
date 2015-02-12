# Frances

### Getting Started 
Please note – this guide assumes you are using OS X. If you aren't, you hopefully know the equivalent commands to make these things happen. If you don't, find someone to help you!

First, clone this project:

```
git clone git@github.com:duner/frances.git
cd frances
```

Then create the database using the `dbinit.sql` file. This assumes that you have Postgres and PostGIS installed.

```
psql < dbinit.sql
```

Then, create the virtual enviroment for the project and install the requirements:

```
mkvirtualenv frances
pip install -r requirements.txt
```

Now, download the National Historic Registry data and convert the Microsoft Access Database to a Shapefile. (Note: this requires you to have GDAL installed with the `.mdb` driver, which can be installed with Homebrew: `brew reinstall gdal --enable-mdb`)

```
mkdir frances/main/data
cd frances/main/data
curl -o spatial.mdb "http://nrhp.focus.nps.gov/natreg/docs/spatial.mdb" 
curl -O http://nrhp.focus.nps.gov/natreg/docs/NRHP_Midwest_Region.zip
unzip NRHP_Midwest_Region.zip
ogr2ogr -f "ESRI Shapefile" nrhp_spatial.shp spatial.mdb
ogr2ogr -f "KML" illinois.kml doc.kml ILLINOIS

#ogr2ogr -f "KML" -a_srs EPSG:900913 doc_projected.kml doc.kml
```

ogr2ogr -f "ESRI Shapefile" nrhp_spatial.shp nrhp_spatial.mdb
ogr2ogr -a_srs EPSG:900913 nrhp_projected.shp nrhp.shp
ogr2ogr -f CSV csv/output.csv nrhp_nad27.shp -lco CREATE_CSVT=YES


EPSG:900913

You should now be able to run your first migration:

```
python manage.py makemigrations
python manage.py migrate
``` 