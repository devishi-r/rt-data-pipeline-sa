# pulling postgres latest image
# asking it to copy paste the sql file into the database 

FROM postgres:latest

COPY create_table.sql /docker-entrypoint-initdb.d/
# Anything inside docker-entrypoint-initdb.d/ will be run as create_table.sql file when the container starts 