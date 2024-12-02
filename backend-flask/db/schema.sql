CREATE EXTENSION IF NOT EXISTS "uuid-ossp";


psql cruddur < db/schema.sql -h localhost -U postgres