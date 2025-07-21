import sqlite3

cv_entries = {
    "Objective": "I'm a passionate and detail-oriented Software Engineer...",
    "Skills": "Python, Java, SQL, React, FastAPI, Docker, Git, etc.",
    "Projects": "WeShare, Code Clinics, Claim Bot, Pathfinding Visualizer, etc.",
    "Achievements": "1st in Motheo Hackathon, 3rd in AWS DeepRacer...",
    "Education": "WeThinkCode_, Merebank Secondary...",
    "Personal": "Durban-based, loves building projects, gaming, automation.",
    "Contact": "Email: Azhargamer15@gmail.com, GitHub: github.com/azharxkhan..."
}

def init_db():
    conn = sqlite3.connect("db/cv_data.db")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS cv_sections")
    cur.execute("""
        CREATE TABLE cv_sections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            section TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)
    for section, content in cv_entries.items():
        cur.execute("INSERT INTO cv_sections (section, content) VALUES (?, ?)", (section, content))
    conn.commit()
    conn.close()
    print("Database initialized with CV content.")

if __name__ == "__main__":
    init_db()
