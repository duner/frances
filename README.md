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


