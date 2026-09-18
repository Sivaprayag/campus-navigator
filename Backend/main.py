from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
import sqlite3
app = FastAPI()
app.add_middleware(
    SessionMiddleware,
    secret_key="campus-secret-key"
)
templates = Jinja2Templates(directory="templates")

university_name = "Vertex University"


connection = sqlite3.connect("../database/campus.db")
cursor = connection.cursor()

# =========================
# LOCATIONS TABLE
# =========================

cursor.execute("DROP TABLE IF EXISTS locations")

cursor.execute("""
CREATE TABLE locations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    block TEXT,
    location TEXT,
    description TEXT,
    latitude REAL,
    longitude REAL
)
""")


locations = [

    # Central Library
    ("Central Library", "CS Level",
     "Computer science books and study area", 10.10, 20.10),

    ("Central Library", "Mechanical Level",
     "Mechanical engineering books and study area", 10.11, 20.11),

    ("Central Library", "Business Level",
     "Business and management books", 10.12, 20.12),

    ("Central Library", "Arts Level",
     "Arts and humanities books", 10.13, 20.13),

    ("Central Library", "Computer Lab",
     "Computers available for students", 10.14, 20.14),


    # Food Block
    ("Food Block", "Campus Canteen",
     "Main campus dining area", 10.20, 20.20),

    ("Food Block", "Cafe",
     "Coffee, beverages and snacks", 10.21, 20.21),

    ("Food Block", "Juice Shop",
     "Fresh juices and drinks", 10.22, 20.22),

    ("Food Block", "North Indian Food Store",
     "North Indian food", 10.23, 20.23),

    ("Food Block", "South Indian Food Store",
     "South Indian food", 10.24, 20.24),


    # CSE Block
    ("CSE Block", "Lecture Hall 1",
     "CSE lecture hall", 10.30, 20.30),

    ("CSE Block", "Lecture Hall 2",
     "CSE lecture hall", 10.31, 20.31),

    ("CSE Block", "Lecture Hall 3",
     "CSE lecture hall", 10.32, 20.32),

    ("CSE Block", "Lecture Hall 4",
     "CSE lecture hall", 10.33, 20.33),

    ("CSE Block", "Lecture Hall 5",
     "CSE lecture hall", 10.34, 20.34),

    ("CSE Block", "Faculty Office 1",
     "CSE faculty office", 10.35, 20.35),

    ("CSE Block", "Faculty Office 2",
     "CSE faculty office", 10.36, 20.36),

    ("CSE Block", "Security Office",
     "CSE security office", 10.37, 20.37),


    # Mechanical Block
    ("Mechanical Block", "Lecture Hall 1",
     "Mechanical lecture hall", 10.40, 20.40),

    ("Mechanical Block", "Lecture Hall 2",
     "Mechanical lecture hall", 10.41, 20.41),

    ("Mechanical Block", "Lecture Hall 3",
     "Mechanical lecture hall", 10.42, 20.42),

    ("Mechanical Block", "Lecture Hall 4",
     "Mechanical lecture hall", 10.43, 20.43),

    ("Mechanical Block", "Lecture Hall 5",
     "Mechanical lecture hall", 10.44, 20.44),

    ("Mechanical Block", "Faculty Office 1",
     "Mechanical faculty office", 10.45, 20.45),

    ("Mechanical Block", "Faculty Office 2",
     "Mechanical faculty office", 10.46, 20.46),

    ("Mechanical Block", "Security Office",
     "Mechanical security office", 10.47, 20.47),


    # BBA Block
    ("BBA Block", "Lecture Hall 1",
     "BBA lecture hall", 10.50, 20.50),

    ("BBA Block", "Lecture Hall 2",
     "BBA lecture hall", 10.51, 20.51),

    ("BBA Block", "Lecture Hall 3",
     "BBA lecture hall", 10.52, 20.52),

    ("BBA Block", "Lecture Hall 4",
     "BBA lecture hall", 10.53, 20.53),

    ("BBA Block", "Lecture Hall 5",
     "BBA lecture hall", 10.54, 20.54),

    ("BBA Block", "Faculty Office 1",
     "BBA faculty office", 10.55, 20.55),

    ("BBA Block", "Faculty Office 2",
     "BBA faculty office", 10.56, 20.56),

    ("BBA Block", "Security Office",
     "BBA security office", 10.57, 20.57),


    # Arts Block
    ("Arts Block", "Lecture Hall 1",
     "Arts lecture hall", 10.60, 20.60),

    ("Arts Block", "Lecture Hall 2",
     "Arts lecture hall", 10.61, 20.61),

    ("Arts Block", "Lecture Hall 3",
     "Arts lecture hall", 10.62, 20.62),

    ("Arts Block", "Lecture Hall 4",
     "Arts lecture hall", 10.63, 20.63),

    ("Arts Block", "Lecture Hall 5",
     "Arts lecture hall", 10.64, 20.64),

    ("Arts Block", "Faculty Office 1",
     "Arts faculty office", 10.65, 20.65),

    ("Arts Block", "Faculty Office 2",
     "Arts faculty office", 10.66, 20.66),

    ("Arts Block", "Security Office",
     "Arts security office", 10.67, 20.67),


    # Auditorium
    ("Auditorium", "Main Auditorium",
     "University auditorium for events and seminars", 10.70, 20.70)
]


cursor.executemany("""
INSERT INTO locations
(block, location, description, latitude, longitude)
VALUES (?, ?, ?, ?, ?)
""", locations)

connection.commit()
# =========================
# TIMETABLE TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS timetable (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day TEXT,
    stream TEXT,
    subject TEXT,
    block TEXT,
    room TEXT,
    start_time TEXT,
    end_time TEXT,
    activity_type TEXT
)
""")
connection.commit()
# =========================
# TIMETABLE DATA
# =========================s

cursor.execute("DELETE FROM timetable")
# =========================
# DUMMY WEEKLY TIMETABLE
# =========================

timetable_data = [

    # ================= CSE =================
    ("Monday", "CSE", "Python Programming", "CSE Block", "Lecture Hall 1", "09:00", "10:00", "Class"),
    ("Monday", "CSE", "Engineering Mathematics", "CSE Block", "Lecture Hall 2", "10:00", "11:00", "Class"),
    ("Monday", "CSE", "Physics", "CSE Block", "Lecture Hall 3", "11:15", "12:15", "Class"),
    ("Monday", "CSE", "Programming Lab", "CSE Block", "Lecture Hall 4", "13:15", "15:15", "Lab"),
    ("Monday", "CSE", "English", "CSE Block", "Lecture Hall 5", "15:30", "16:30", "Class"),

    ("Tuesday", "CSE", "Engineering Mathematics", "CSE Block", "Lecture Hall 1", "09:00", "10:00", "Class"),
    ("Tuesday", "CSE", "Python Programming", "CSE Block", "Lecture Hall 2", "10:00", "11:00", "Class"),
    ("Tuesday", "CSE", "Electronics", "CSE Block", "Lecture Hall 3", "11:10", "12:10", "Class"),
    ("Tuesday", "CSE", "Physics Lab", "CSE Block", "Lecture Hall 4", "13:15", "15:15", "Lab"),
    ("Tuesday", "CSE", "Communication Skills", "CSE Block", "Lecture Hall 5", "15:30", "16:30", "Class"),

    ("Wednesday", "CSE", "Python Programming", "CSE Block", "Lecture Hall 1", "09:00", "10:00", "Class"),
    ("Wednesday", "CSE", "Electronics", "CSE Block", "Lecture Hall 2", "10:00", "11:00", "Class"),
    ("Wednesday", "CSE", "Engineering Mathematics", "CSE Block", "Lecture Hall 3", "11:15", "12:15", "Class"),
    ("Wednesday", "CSE", "English", "CSE Block", "Lecture Hall 4", "13:15", "14:15", "Class"),
    ("Wednesday", "CSE", "Programming Lab", "CSE Block", "Lecture Hall 5", "14:30", "16:30", "Lab"),

    ("Thursday", "CSE", "Physics", "CSE Block", "Lecture Hall 1", "09:00", "10:00", "Class"),
    ("Thursday", "CSE", "Python Programming", "CSE Block", "Lecture Hall 2", "10:00", "11:00", "Class"),
    ("Thursday", "CSE", "Engineering Mathematics", "CSE Block", "Lecture Hall 3", "11:10", "12:10", "Class"),
    ("Thursday", "CSE", "Electronics Lab", "CSE Block", "Lecture Hall 4", "13:15", "15:15", "Lab"),
    ("Thursday", "CSE", "English", "CSE Block", "Lecture Hall 5", "15:30", "16:30", "Class"),

    ("Friday", "CSE", "Engineering Mathematics", "CSE Block", "Lecture Hall 1", "09:00", "10:00", "Class"),
    ("Friday", "CSE", "Python Programming", "CSE Block", "Lecture Hall 2", "10:00", "11:00", "Class"),
    ("Friday", "CSE", "Physics", "CSE Block", "Lecture Hall 3", "11:15", "12:15", "Class"),
    ("Friday", "CSE", "Communication Skills", "CSE Block", "Lecture Hall 4", "13:15", "14:15", "Class"),
    ("Friday", "CSE", "Project Work", "CSE Block", "Lecture Hall 5", "14:30", "16:30", "Activity"),


    # ================= MECHANICAL =================
    ("Monday", "Mechanical", "Engineering Mechanics", "Mechanical Block", "Lecture Hall 1", "09:00", "10:00", "Class"),
    ("Monday", "Mechanical", "Engineering Mathematics", "Mechanical Block", "Lecture Hall 2", "10:00", "11:00", "Class"),
    ("Monday", "Mechanical", "Thermodynamics", "Mechanical Block", "Lecture Hall 3", "11:10", "12:10", "Class"),
    ("Monday", "Mechanical", "Workshop Lab", "Mechanical Block", "Lecture Hall 4", "13:15", "15:15", "Lab"),
    ("Monday", "Mechanical", "English", "Mechanical Block", "Lecture Hall 5", "15:30", "16:30", "Class"),

    ("Tuesday", "Mechanical", "Engineering Mathematics", "Mechanical Block", "Lecture Hall 1", "09:00", "10:00", "Class"),
    ("Tuesday", "Mechanical", "Thermodynamics", "Mechanical Block", "Lecture Hall 2", "10:00", "11:00", "Class"),
    ("Tuesday", "Mechanical", "Engineering Drawing", "Mechanical Block", "Lecture Hall 3", "11:15", "12:15", "Class"),
    ("Tuesday", "Mechanical", "Manufacturing Lab", "Mechanical Block", "Lecture Hall 4", "13:15", "15:15", "Lab"),
    ("Tuesday", "Mechanical", "Communication Skills", "Mechanical Block", "Lecture Hall 5", "15:30", "16:30", "Class"),

    ("Wednesday", "Mechanical", "Engineering Mechanics", "Mechanical Block", "Lecture Hall 1", "09:00", "10:00", "Class"),
    ("Wednesday", "Mechanical", "Engineering Drawing", "Mechanical Block", "Lecture Hall 2", "10:00", "11:00", "Class"),
    ("Wednesday", "Mechanical", "Engineering Mathematics", "Mechanical Block", "Lecture Hall 3", "11:10", "12:10", "Class"),
    ("Wednesday", "Mechanical", "English", "Mechanical Block", "Lecture Hall 4", "13:15", "14:15", "Class"),
    ("Wednesday", "Mechanical", "Workshop Lab", "Mechanical Block", "Lecture Hall 5", "14:30", "16:30", "Lab"),

    ("Thursday", "Mechanical", "Thermodynamics", "Mechanical Block", "Lecture Hall 1", "09:00", "10:00", "Class"),
    ("Thursday", "Mechanical", "Engineering Mechanics", "Mechanical Block", "Lecture Hall 2", "10:00", "11:00", "Class"),
    ("Thursday", "Mechanical", "Engineering Mathematics", "Mechanical Block", "Lecture Hall 3", "11:15", "12:15", "Class"),
    ("Thursday", "Mechanical", "Manufacturing Lab", "Mechanical Block", "Lecture Hall 4", "13:15", "15:15", "Lab"),
    ("Thursday", "Mechanical", "English", "Mechanical Block", "Lecture Hall 5", "15:30", "16:30", "Class"),

    ("Friday", "Mechanical", "Engineering Mathematics", "Mechanical Block", "Lecture Hall 1", "09:00", "10:00", "Class"),
    ("Friday", "Mechanical", "Thermodynamics", "Mechanical Block", "Lecture Hall 2", "10:00", "11:00", "Class"),
    ("Friday", "Mechanical", "Engineering Drawing", "Mechanical Block", "Lecture Hall 3", "11:10", "12:10", "Class"),
    ("Friday", "Mechanical", "Communication Skills", "Mechanical Block", "Lecture Hall 4", "13:15", "14:15", "Class"),
    ("Friday", "Mechanical", "Project Work", "Mechanical Block", "Lecture Hall 5", "14:30", "16:30", "Activity"),


    # ================= BBA =================
    ("Monday", "BBA", "Financial Accounting", "BBA Block", "Lecture Hall 1", "09:15", "10:15", "Class"),
    ("Monday", "BBA", "Business Economics", "BBA Block", "Lecture Hall 2", "10:15", "11:15", "Class"),
    ("Monday", "BBA", "Marketing", "BBA Block", "Lecture Hall 3", "11:30", "12:30", "Class"),
    ("Monday", "BBA", "Business Communication", "BBA Block", "Lecture Hall 4", "13:15", "14:15", "Class"),
    ("Monday", "BBA", "Management Principles", "BBA Block", "Lecture Hall 5", "14:30", "16:30", "Class"),

    ("Tuesday", "BBA", "Marketing", "BBA Block", "Lecture Hall 1", "09:15", "10:15", "Class"),
    ("Tuesday", "BBA", "Financial Accounting", "BBA Block", "Lecture Hall 2", "10:15", "11:15", "Class"),
    ("Tuesday", "BBA", "Human Resource Management", "BBA Block", "Lecture Hall 3", "11:30", "12:30", "Class"),
    ("Tuesday", "BBA", "Business Economics", "BBA Block", "Lecture Hall 4", "13:15", "14:15", "Class"),
    ("Tuesday", "BBA", "Presentation Skills", "BBA Block", "Lecture Hall 5", "14:30", "16:30", "Activity"),

    ("Wednesday", "BBA", "Business Economics", "BBA Block", "Lecture Hall 1", "09:15", "10:15", "Class"),
    ("Wednesday", "BBA", "Marketing", "BBA Block", "Lecture Hall 2", "10:15", "11:15", "Class"),
    ("Wednesday", "BBA", "Financial Accounting", "BBA Block", "Lecture Hall 3", "11:30", "12:30", "Class"),
    ("Wednesday", "BBA", "Management Principles", "BBA Block", "Lecture Hall 4", "13:15", "14:15", "Class"),
    ("Wednesday", "BBA", "Business Communication", "BBA Block", "Lecture Hall 5", "14:30", "16:30", "Class"),

    ("Thursday", "BBA", "Human Resource Management", "BBA Block", "Lecture Hall 1", "09:15", "10:15", "Class"),
    ("Thursday", "BBA", "Business Economics", "BBA Block", "Lecture Hall 2", "10:15", "11:15", "Class"),
    ("Thursday", "BBA", "Marketing", "BBA Block", "Lecture Hall 3", "11:30", "12:30", "Class"),
    ("Thursday", "BBA", "Financial Accounting", "BBA Block", "Lecture Hall 4", "13:15", "14:15", "Class"),
    ("Thursday", "BBA", "Management Principles", "BBA Block", "Lecture Hall 5", "14:30", "16:30", "Class"),

    ("Friday", "BBA", "Financial Accounting", "BBA Block", "Lecture Hall 1", "09:15", "10:15", "Class"),
    ("Friday", "BBA", "Marketing", "BBA Block", "Lecture Hall 2", "10:15", "11:15", "Class"),
    ("Friday", "BBA", "Business Economics", "BBA Block", "Lecture Hall 3", "11:30", "12:30", "Class"),
    ("Friday", "BBA", "Business Communication", "BBA Block", "Lecture Hall 4", "13:15", "14:15", "Class"),
    ("Friday", "BBA", "Project Work", "BBA Block", "Lecture Hall 5", "14:30", "16:30", "Activity"),


    # ================= ARTS =================
    ("Monday", "Arts", "English Literature", "Arts Block", "Lecture Hall 1", "09:15", "10:15", "Class"),
    ("Monday", "Arts", "History", "Arts Block", "Lecture Hall 2", "10:15", "11:15", "Class"),
    ("Monday", "Arts", "Psychology", "Arts Block", "Lecture Hall 3", "11:30", "12:30", "Class"),
    ("Monday", "Arts", "Sociology", "Arts Block", "Lecture Hall 4", "13:15", "14:15", "Class"),
    ("Monday", "Arts", "Creative Arts", "Arts Block", "Lecture Hall 5", "14:30", "16:30", "Activity"),

    ("Tuesday", "Arts", "Psychology", "Arts Block", "Lecture Hall 1", "09:15", "10:15", "Class"),
    ("Tuesday", "Arts", "English Literature", "Arts Block", "Lecture Hall 2", "10:15", "11:15", "Class"),
    ("Tuesday", "Arts", "History", "Arts Block", "Lecture Hall 3", "11:30", "12:30", "Class"),
    ("Tuesday", "Arts", "Sociology", "Arts Block", "Lecture Hall 4", "13:15", "14:15", "Class"),
    ("Tuesday", "Arts", "Communication", "Arts Block", "Lecture Hall 5", "14:30", "16:30", "Class"),

    ("Wednesday", "Arts", "History", "Arts Block", "Lecture Hall 1", "09:15", "10:15", "Class"),
    ("Wednesday", "Arts", "Psychology", "Arts Block", "Lecture Hall 2", "10:15", "11:15", "Class"),
    ("Wednesday", "Arts", "English Literature", "Arts Block", "Lecture Hall 3", "11:30", "12:30", "Class"),
    ("Wednesday", "Arts", "Creative Arts", "Arts Block", "Lecture Hall 4", "13:15", "14:15", "Activity"),
    ("Wednesday", "Arts", "Sociology", "Arts Block", "Lecture Hall 5", "14:30", "16:30", "Class"),

    ("Thursday", "Arts", "English Literature", "Arts Block", "Lecture Hall 1", "09:15", "10:15", "Class"),
    ("Thursday", "Arts", "History", "Arts Block", "Lecture Hall 2", "10:15", "11:15", "Class"),
    ("Thursday", "Arts", "Psychology", "Arts Block", "Lecture Hall 3", "11:30", "12:30", "Class"),
    ("Thursday", "Arts", "Sociology", "Arts Block", "Lecture Hall 4", "13:15", "14:15", "Class"),
    ("Thursday", "Arts", "Communication", "Arts Block", "Lecture Hall 5", "14:30", "16:30", "Class"),

    ("Friday", "Arts", "Psychology", "Arts Block", "Lecture Hall 1", "09:15", "10:15", "Class"),
    ("Friday", "Arts", "History", "Arts Block", "Lecture Hall 2", "10:15", "11:15", "Class"),
    ("Friday", "Arts", "English Literature", "Arts Block", "Lecture Hall 3", "11:30", "12:30", "Class"),
    ("Friday", "Arts", "Communication", "Arts Block", "Lecture Hall 4", "13:15", "14:15", "Class"),
    ("Friday", "Arts", "Project Work", "Arts Block", "Lecture Hall 5", "14:30", "16:30", "Activity")
]

cursor.executemany("""
INSERT INTO timetable
(day, stream, subject, block, room, start_time, end_time, activity_type)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", timetable_data)

connection.commit()

print("Weekly timetable added successfully!")
connection.commit()


# =========================
# STUDENTS TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vid TEXT UNIQUE,
    password TEXT
)
""")


students = [
    ("VID1001", "Pass1001"),
    ("VID1002", "Pass1002"),
    ("VID1003", "Pass1003"),
    ("VID1004", "Pass1004"),
    ("VID1005", "Pass1005")
]


cursor.executemany("""
INSERT OR IGNORE INTO students (vid, password)
VALUES (?, ?)
""", students)

connection.commit()
@app.get("/")
def home(request: Request):

    if not request.session.get("logged_in"):
        return RedirectResponse(url="/login-page")

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


connection.commit()


@app.get("/login-page")
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )



@app.get("/login")
def login(request: Request, vid: str, password: str):

    connection = sqlite3.connect("../database/campus.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT vid FROM students
    WHERE vid = ? AND password = ?
    """, (vid, password))

    student = cursor.fetchone()
    connection.close()

    if student:

        request.session["logged_in"] = True
        request.session["vid"] = student[0]

        return RedirectResponse(url="/", status_code=303)

    return {
        "success": False,
        "message": "Invalid VID or password"
    }
@app.get("/logout")
def logout(request: Request):

    request.session.clear()

    return RedirectResponse(url="/login-page", status_code=303)
@app.get("/timetable")
def get_timetable():
    connection = sqlite3.connect("../database/campus.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT day, stream, subject, block, room, start_time, end_time, activity_type
    FROM timetable
    ORDER BY
        CASE day
            WHEN 'Monday' THEN 1
            WHEN 'Tuesday' THEN 2
            WHEN 'Wednesday' THEN 3
            WHEN 'Thursday' THEN 4
            WHEN 'Friday' THEN 5
        END,
        start_time
    """)

    timetable = cursor.fetchall()
    connection.close()

    return timetable
# =========================
# ROOM AVAILABILITY
# =========================

@app.get("/room-availability")
def room_availability(day: str, time: str, block: str):

    connection = sqlite3.connect("../database/campus.db")
    cursor = connection.cursor()

    # Get all lecture halls in the selected block
    cursor.execute("""
    SELECT location
    FROM locations
    WHERE block = ?
    AND location LIKE 'Lecture Hall%'
    ORDER BY location
    """, (block,))

    rooms = cursor.fetchall()

    # Get classes happening at the selected time
    cursor.execute("""
    SELECT room, subject, stream, start_time, end_time
    FROM timetable
    WHERE day = ?
    AND block = ?
    AND start_time <= ?
    AND end_time > ?
    """, (day, block, time, time))

    occupied = cursor.fetchall()

    connection.close()

    # Create a quick lookup for occupied rooms
    occupied_rooms = {}

    for room, subject, stream, start_time, end_time in occupied:

        occupied_rooms[room] = {
            "subject": subject,
            "stream": stream,
            "start_time": start_time,
            "end_time": end_time
        }

    result = []

    for room_tuple in rooms:

        room = room_tuple[0]

        if room in occupied_rooms:

            info = occupied_rooms[room]

            result.append({
                "room": room,
                "status": "Occupied",
                "subject": info["subject"],
                "stream": info["stream"],
                "start_time": info["start_time"],
                "end_time": info["end_time"]
            })

        else:

            result.append({
                "room": room,
                "status": "Available"
            })

    return result
@app.get("/rush")
def campus_rush(day: str, time: str):

    connection = sqlite3.connect("../database/campus.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT stream, block
    FROM timetable
    WHERE day = ?
    AND start_time <= ?
    AND end_time > ?
    """, (day, time, time))

    active_classes = cursor.fetchall()
    connection.close()

    rush = {
        "Central Library": 20,
        "Food Block": 20,
        "CSE Block": 0,
        "Mechanical Block": 0,
        "BBA Block": 0,
        "Arts Block": 0,
        "Auditorium": 10
    }

    for stream, block in active_classes:
        if block in rush:
            rush[block] += 30

    # Lunch-time crowd estimate
    if "12:30" <= time < "13:30":
        rush["Food Block"] += 60
        rush["Central Library"] += 10

    result = []

    for area, score in rush.items():

        if score >= 80:
            level = "Very High"
        elif score >= 50:
            level = "High"
        elif score >= 25:
            level = "Medium"
        else:
            level = "Low"

        result.append({
            "area": area,
            "score": score,
            "level": level
        })

    return result