import tkinter as tk
from tkinter import ttk
from utils.db_access import get_section_content, get_all_sections

def launch_gui(chat_callback):
    root = tk.Tk()
    root.title("Azhar Khan – Interactive CVMate")
    root.geometry("950x640")
    root.configure(bg="#2b6777")  # Teal background

    MAIN_FONT = ("Century Gothic", 11)

    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("TLabel", background="#2b6777", foreground="white", font=MAIN_FONT)
    style.configure("TButton", font=MAIN_FONT, padding=6)
    style.configure("TFrame", background="#2b6777")
    style.configure("Nav.TButton", background="white", foreground="#2b6777", relief="flat")
    style.map("Nav.TButton", background=[("active", "#dfeeea")])

    # === Master layout frame ===
    main_frame = tk.Frame(root, bg="#2b6777")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # === Sidebar ===
    nav_frame = tk.Frame(main_frame, bg="#2b6777", width=200)
    nav_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(10, 0), pady=10)

    tk.Label(nav_frame, text="📘 CV Sections", bg="#2b6777", fg="white",
             font=(MAIN_FONT[0], 13, "bold"), pady=10).pack(fill=tk.X, pady=(0, 10))

    def on_section_click(section):
        content = get_section_content(section)
        display_area.config(state="normal")
        display_area.delete(1.0, tk.END)
        display_area.insert(tk.END, f"{section}\n\n{content}")
        display_area.config(state="disabled")

    for section in get_all_sections():
        ttk.Button(nav_frame, text=section, style="Nav.TButton",
                   command=lambda s=section: on_section_click(s)).pack(fill=tk.X, padx=10, pady=4)

    # === Right column: Display + Chat ===
    right_frame = tk.Frame(main_frame, bg="#2b6777")
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 10), pady=10)

    # Display area
    display_frame = tk.Frame(right_frame)
    display_frame.pack(fill=tk.BOTH, expand=True)

    display_area = tk.Text(display_frame, wrap=tk.WORD, font=MAIN_FONT,
                           bg="white", fg="#2b6777", relief=tk.FLAT, padx=12, pady=10)
    display_area.config(state="disabled")
    display_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(display_frame, command=display_area.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    display_area["yscrollcommand"] = scrollbar.set

    # Chatbot area
    chatbot_frame = tk.Frame(right_frame, bg="#2b6777")
    chatbot_frame.pack(fill=tk.X, pady=(10, 0))

    tk.Label(chatbot_frame, text="🤖 Ask About My CV", bg="#2b6777", fg="white",
             font=(MAIN_FONT[0], 11, "bold")).pack(anchor="w", padx=5)

    chat_entry = tk.Entry(chatbot_frame, font=MAIN_FONT, bg="white", fg="#2b6777", relief=tk.FLAT)
    chat_entry.pack(fill=tk.X, expand=True, padx=5, pady=(5, 10))

    def handle_chat():
        msg = chat_entry.get()
        if msg:
            response = chat_callback(msg)
            display_area.config(state="normal")
            display_area.insert(tk.END, f"\nYou: {msg}\nBot: {response}\n")
            display_area.config(state="disabled")
            display_area.see(tk.END)
            chat_entry.delete(0, tk.END)

    chat_entry.bind("<Return>", lambda e: handle_chat())

    root.mainloop()
