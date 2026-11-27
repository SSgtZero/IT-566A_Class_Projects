#!/bin/bash
# Drop the expense_tracker database and its user.

# Run from this script's directory so the paths below work from anywhere
cd "$(dirname "$0")"
mkdir -p logs
d=$(date)

echo $d': Dropping database...' | tee -a logs/drop_database.log
mysql < db_version_1/drop_database.sql 2>&1 | tee -a logs/drop_database.log
echo $d': Dropping user...' | tee -a logs/drop_user.log
mysql < db_version_1/drop_user.sql 2>&1 | tee -a logs/drop_user.log