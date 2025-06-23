# Late Show Code Challenge
A Flask API for managing episodes, guests, and appearances on a TV show (Late Show).

## Overview
This project is a backend API built with Flask and SQLAlchemy, designed to handle episodes, guests, and their appearances. It supports CRUD operations and data validation for appearances.

### Features
**Episode Management:** List and retrieve episodes.

**Guest Management:** List guests.

**Appearance Management:** Create new appearances with validation (rating must be between 1 and 5).

## Data Models
**Episode:** Stores show date and episode number.

**Guest:** Stores guest name and occupation.

**Appearance:** Links guests to episodes with a rating.

## API Endpoints
| Endpoint     | Method      | Description     |
|---------------|---------------|---------------|
| /  | GET | Welcome message |
| /episodes | GET | List all episodes |
| /episodes/<id> | GET | Get episode by id |
| /guests | GET | List all guests |
| /appearances | POST | Create a new appearance |

### Example Requests
**List all episodes:**

text
**GET /episodes**<br>
**Get episode by ID:**

text
**GET /episodes/1**<br>
**List all guests:**

text
**GET /guests**<br>
**Create an appearance:**

text
**POST /appearances**<br>
{
  "rating": 4,<br>
  "episode_id": 1,<br>
  "guest_id": 1<br>
}<br>
## Setup<br>
1.Clone the repository:

bash
git clone https://github.com/yourusername/lateshow-dorothy-chepkoech.git<br>
cd lateshow-dorothy-chepkoech<br>

2.Set up a virtual environment and install dependencies:

bash<br>
python -m venv .venv<br>
source .venv/bin/activate  # On Windows: venv\Scripts\activate<br>
pip install -r requirements.txt<br>

3.Initialize the database:

bash<br>
**python -m flask db init**<br>
**python -m flask db migrate -m "Initial migration"**<br>
**python -m flask db upgrade**<br>
**python seed.py**<br>

4.Run the application:

bash<br>
**python app.py**<br>
## Project Structure
text
```lateshow-dorothy-chepkoech/
├── app.py                # Main application file
├── models.py             # Database models
├── extensions.py         # Flask extensions
├── serialization.py      # Serialization logic
├── seed.py               # Database seeding script
├── requirements.txt      # Dependencies
└── README.md             # This file
You’re ready to go!
