#!/bin/bash

if PGPASSWORD=postgres psql -U postgres -lqt | cut -d \| -f 1 | grep -qw bfr; then
  PGPASSWORD=postgres psql -U postgres -c "DROP DATABASE bfr"
fi
PGPASSWORD=postgres psql -U postgres -c "CREATE DATABASE bfr"
PGPASSWORD=postgres psql -U postgres -d bfr -c "CREATE SCHEMA client"
PGPASSWORD=postgres psql -U postgres -d bfr -c "CREATE TABLE client.players(login varchar(200), key varchar(200), salt varchar(200), games_cnt int, wins_cnt int)"
