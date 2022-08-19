-- Database: Proyecto

-- DROP DATABASE IF EXISTS "Proyecto";

CREATE DATABASE "Proyecto"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Spain.1252'
    LC_CTYPE = 'Spanish_Spain.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

COMMENT ON DATABASE "Proyecto"
    IS 'Proyecto de LALCEC';