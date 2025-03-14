# Satellite Data Management System

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
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd satellite-data-management
   ```
2. Ensure Python 3.8 is installed.
3. Install dependencies using Pipenv:
   ```bash
   pipenv install
   ```
4. Initialize the database:
   ```bash
   pipenv run alembic upgrade head
   ```
5. Run the script:
   ```bash
   pipenv run python main.py
   ```

## How to Use
### Viewing Data
- See all satellites: `display_satellite()`
- See collected data: `display_data()`
- See region details: `display_region()`

### Managing Satellites
- Add a new satellite: `handle_sat_create()`
- Update satellite details: `handle_sat_edit()`
- Remove a satellite: `handle_sat_delete()`

### Managing Data
- Add satellite data: `handle_satdata_create()`
- Update satellite data: `handle_data_edit()`
- Remove satellite data: `handle_data_delete()`

### Managing Regions
- Add a new region: `handle_region_create()`
- Update region details: `handle_region_edit()`
- Remove a region: `handle_region_delete()`

## Database Setup & Structure
### Setting Up the Database
To initialize the database, run:
```bash
pipenv run alembic upgrade head
```
This applies migrations and sets up the necessary tables.

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

## Error Handling
- Ensures correct data types for input (integer, string, float, etc.).
- Provides prompts for valid input entries.
- Displays warnings for invalid operations.
- Logs errors and invalid operations for debugging.

## License
This project is licensed under the MIT License.

## Author
[Your Name]

