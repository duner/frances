DROP DATABASE IF EXISTS frances;
DROP USER IF EXISTS frances;
CREATE ROLE frances PASSWORD 'frances' LOGIN;
CREATE DATABASE frances OWNER frances;
\c frances
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;