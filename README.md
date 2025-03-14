# Satellite Monitoring DataBase

## Overview
The Satellite Data Management System is a command-line application for managing satellite-related information. You can use it to store and organize satellite details, collected data, and associated regions. It allows you to create, view, update, and delete records as needed.

This system uses two one-to-many relationships:
1. A satellite can have multiple collected data entries.
2. A satellite can be associated with multiple regions.

### Technologies Used
- Python 3.8
- SQLAlchemy (for database management)
- Alembic (for database migrations)
- SQLite (default database, can be configured for other databases)
- Docker
- Tkinter

## Project Structure

```
satellite_monitoring_Db/ ├──
│-- migrations/
|      ├──versions/
|      ├──env.py
|      ├──README
|      ├──script.py.mako
|--mydb/
|      ├──models.py
|      ├──seed.py
|--alembic.ini
|--Dockerfile
|--main.py
|--monitoring.db
|--Pipfile
|--Pipfile.lock
|--README.md
|--run.py

```
## What You Can Do
- View satellite information
- View collected satellite data
- View region details
- Add new satellites, data, and regions
- Modify existing records
- Remove records from the system

## Requirements
- Python 3.8
- SQLAlchemy
- Alembic

## Installation
There are two ways for installation:

### 1. Clone the repo
Fork and clone the repository [repo](https://github.com/Edmund-Kiama/Satellite-Data-Monitoring-DB):
   ```bash
   git clone git@github.com:Edmund-Kiama/Satellite-Data-Monitoring-DB.git
   cd satellite-data-Monitoring-DB
   ```
### 2. Using Docker Images
If you have docker, you can pull and run its image from docker hub:
   ```bash
   docker run -it --rm edmundkiama/sat-monitoring-db:latest
   ```

## From cloning the repo
If you choose to clone the repo, follow the following:  
You can either run the program in CLI or via a python GUI:

### a) Using the CLI
1. Ensure Python 3.8 is installed.
   ```bash
   python3 --version
   ```
2. Install dependencies using Pipenv:
   ```bash
   pipenv install
   ```
3. Initialize the python environment in shell:
   ```bash
   pipenv shell
   ```
4. Run the main script and interact with its CLI:
   ```bash
   python main.py
   ```
### B) Using python GUI
1. Ensure Python 3.8 is installed.
   ```bash
   python3 --version
   ```
2. Install tkinter: (on Ubuntu or Debian)
   ```bash
   sudo apt-get install python3-tk
   ```
3. Install rest of the dependecies in your virtual environment:
   ```bash
   pipenv install
   ```
4. Initialize the python environment in shell:
   ```bash
   pipenv shell
5. Run the run script and interact with its tkinter GUI:
   ```bash
   python run.py
   ```

## How to Use
- There are three tables in our Database:
   - Satellite table
   - Satellite Data table
   - Region table    
  
Functionality of the program include:

1. Viewing Table Values
   - See all satellites 
   - See collected data 
   - See region details 

2. Managing Satellites
   - Add a new satellite
   - Update satellite details
   - Remove a satellite

3. Managing Satellite Data
   - Add satellite data
   - Update satellite data
   - Remove satellite data

4. Managing Regions
   - Add a new region
   - Update region details
   - Remove a region

### Database Tables
#### Satellite Table
| Id | Name | Orbit Type | Status | Description |
|----|------|-----------|--------|-------------|

#### Satellite Data Table
| Id | Sat Id | Data Type | Data Value | Date Recorded |
|----|--------|-----------|------------|---------------|

#### Region Table
| Id | Sat Id | Name | Latitude | Longitude |
|----|--------|------|----------|-----------|

## Error Handling features
- Ensures correct data types for input (integer, string, float, etc.).
- Provides prompts for valid input entries.
- Displays warnings for invalid operations.
- Logs errors and invalid operations for debugging.

## License
This project is licensed under the MIT License.


