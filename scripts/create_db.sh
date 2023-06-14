#!/bin/bash

if PGPASSWORD=postgres psql -U postgres -lqt | cut -d \| -f 1 | grep -qw bfr; then
  PGPASSWORD=postgres psql -U postgres -c "DROP DATABASE bfr"
  PGPASSWORD=postgres psql -U postgres -c "DROP USER clientbfr"
fi
PGPASSWORD=postgres psql -U postgres -c "CREATE DATABASE bfr"
PGPASSWORD=postgres psql -U postgres -d bfr -c "CREATE SCHEMA client"
PGPASSWORD=postgres psql -U postgres -d bfr -c "CREATE TABLE client.players(login varchar(200), key varchar(200), salt varchar(200), games_cnt int, wins_cnt int)"
PGPASSWORD=postgres psql -U postgres -d bfr -c "CREATE USER clientbfr WITH PASSWORD 'clientpwd'"
PGPASSWORD=postgres psql -U postgres -d bfr -c "GRANT USAGE ON SCHEMA client TO clientbfr"
PGPASSWORD=postgres psql -U postgres -d bfr -c "GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA client TO clientbfr"


# if doesn't work on ubuntu, try:

#if sudo -u postgres psql -U postgres -lqt | cut -d \| -f 1 | grep -qw bfr; then
#  sudo -u postgres psql -U postgres -c "DROP DATABASE bfr"
#  sudo -u postgres psql -U postgres -c "DROP USER clientbfr"
#fi
#sudo -u postgres psql -U postgres -c "CREATE DATABASE bfr"
#sudo -u postgres psql -U postgres -d bfr -c "CREATE SCHEMA client"
#sudo -u postgres psql -U postgres -d bfr -c "CREATE TABLE client.players(login varchar(200), key varchar(200), salt varchar(200), games_cnt int, wins_cnt int)"
#sudo -u postgres psql -U postgres -d bfr -c "CREATE USER clientbfr WITH PASSWORD 'clientpwd'"
#sudo -u postgres psql -U postgres -d bfr -c "GRANT USAGE ON SCHEMA client TO clientbfr"
#sudo -u postgres psql -U postgres -d bfr -c "GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA client TO clientbfr"
