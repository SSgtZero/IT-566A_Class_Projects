#!/bin/bash
# Create the expense_tracker database, user, tables, and test data.

# Run from this script's directory so the paths below work from anywhere
cd "$(dirname "$0")"
mkdir -p logs
d=$(date)

echo $d': Creating database...' | tee -a logs/create_database.log
mysql < db_version_1/create_database.sql 2>&1 | tee -a logs/create_database.log
echo $d': Creating user...' | tee -a logs/create_user.log
mysql < db_version_1/create_user.sql 2>&1 | tee -a logs/create_user.log
echo $d': Creating tables...' | tee -a logs/create_tables.log
mysql < db_version_1/create_tables.sql 2>&1 | tee -a logs/create_tables.log
echo $d': Inserting test data...' | tee -a logs/insert_test_data.log
mysql < db_version_1/insert_test_data.sql 2>&1 | tee -a logs/insert_test_data.log