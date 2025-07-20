```markdown
# 🧠 CVMate – Interactive CV Viewer with Chatbot

CVMate is a modern, interactive Python desktop application that presents your CV in a sleek GUI. It allows users to browse CV sections like skills, education, and projects — or ask natural language questions via a built-in chatbot.

Built using `Tkinter` and `SQLite`, it is structured for extensibility, style, and ease of use.
```

---

## ✨ Features

- 📘 **Section Navigator** – Browse CV content like Objective, Skills, Projects, etc.
- 🤖 **Built-in Chatbot** – Ask questions like “What projects have you worked on?” or “Tell me about your education.”
- 💾 **SQLite Backend** – All CV data is stored in a local database for flexibility and persistence.
- 🧰 **Admin Panel** – Update or add CV sections using a terminal-based editor.
- 🎨 **Themed UI** – Teal modern layout with clear fonts, spacing, and scrollable content.
- 🪄 **Modular Structure** – Easily extend or replace modules (e.g. switch GUI toolkit, export PDF, or host as web app).

---

## 📂 Project Structure

```

CVMate/
├── main.py               # Entry point
├── db/
│   └── cv\_data.db        # SQLite database storing CV sections
├── data/
│   └── init\_db.py        # Seeds database with initial CV content
├── gui/
│   └── viewer.py         # Styled Tkinter GUI
├── chatbot/
│   └── bot.py            # Keyword-matching chatbot logic
├── admin/
│   └── editor.py         # CLI admin tool to edit/add/delete CV data
└── utils/
└── db\_access.py      # Common DB helper functions

````

---

## 🖥️ Usage

### 1. Initialize the database:
```bash
python data/init_db.py
````

### 2. Launch the GUI app:

```bash
python main.py
```

### 3. Edit or update CV sections:

```bash
python admin/editor.py
```

---

## 🔧 Dependencies

* Python 3.8+
* No external packages required (uses `tkinter` and `sqlite3`, both built-in)

---

## 🛠️ Future Ideas

* [ ] Dark/light mode toggle
* [ ] Export CV as PDF
* [ ] Voice chatbot or typing animation
* [ ] Online hosted version (Flask/Gradio)

---

## 👤 About the Author

**Azhar Khan** – Software Engineer | Algorithm Enthusiast | Backend Developer
📍 Durban, South Africa
🔗 [github.com/azharxkhan](https://github.com/azharxkhan)
✉️ [Azhargamer15@gmail.com](mailto:Azhargamer15@gmail.com)

---

## 📃 License

MIT License — free to use, modify, and build upon.

