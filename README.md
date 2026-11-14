# COMP3005-Assignment3-josejrodriguez

Jose Rodriguez
101104860
josejrodriguez@cmail.carleton.ca

## Requirements
- Python 3.10 or newer
- PostgreSQL 14 or newer running locally
- A linux environment

## Database setup

The application expects a database named 'a3_database' and connects as your operating system user, so no password is needed or stored.

For the program to work, please create a role matching your OS user in postgreSQL if one is not made already. The following are bash commands will set up postgreSQL for the program to run.

    sudo -u postgres creatuser --creatdb "$USER" 
    
    createdb a3_database
    psql -d a3_database -f database/schema.sql
    psql -d a3_database -f database/seed.sql

The commands assume you are in the folder COMP3005-Assignment3-josejrodriguez 

## Python environment

    python3 -m venv .venv
    .venv/bin/pip install -r application/requirements.txt

## Running the program

    .venv/bin/python application/main.py
    
