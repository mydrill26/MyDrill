import pandas as pd
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import subprocess
import os

VIDEO_FOLDER = "/Users/mollyelder/Documents/Gymnastics Videos"  # Replace with the actual path to your video folder

def play_video1(): 
    video_name = video1_file.strip() + ".mp4"
    video_path = os.path.join(
        VIDEO_FOLDER, video1_file
    ) 
    print("VIDEO FOLDER:", repr(VIDEO_FOLDER))
    print("video1_file:", repr(video1_file))
    print("video_name =", repr(video_name))
    print("Full path:", repr(video_path))
    print("Exists:", os.path.exists(video_path))

    print("\nFiles Python can see in the folder:")
    print(os.listdir(VIDEO_FOLDER))

    subprocess.run(["open", video_path])  # For macOS

def play_video2():
    video_name = video2_file.strip() + ".mp4"
    video_path = os.path.join(
        VIDEO_FOLDER, video2_file
    )
    print("VIDEO FOLDER:", repr(VIDEO_FOLDER))
    print("video2_file:", repr(video2_file))
    print("video_name =", repr(video_name))
    print("Full path:", repr(video_path))
    print("Exists:", os.path.exists(video_path))

    print("\nFiles Python can see in the folder:")
    print(os.listdir(VIDEO_FOLDER))

    subprocess.run(["open", video_path])  # For macOS

# Load the drill database 
drills = pd.read_csv("Final Drill Dataset - Sheet1.csv")

def update_skills(event=None):
    selected_apparatus = apparatus_var.get().lower()

# Clean column headings
drills.columns = drills.columns.str.strip().str.lower()

# Clean the values in the columns used for matching
drills["apparatus"] = drills["apparatus"].str.strip().str.lower()
drills["skill"] = drills["skill"].str.strip().str.lower()
drills["problem"] = drills["problem"].str.strip().str.lower()

print(drills.columns)

video1_file = ""
video2_file = ""


# Define update problems 
def update_skills(event=None):
    selected_apparatus = apparatus_var.get().lower()
    selected_skill = skill_var.get().lower()
    skills = drills[drills["apparatus"] == selected_apparatus]["skill"].unique()
    skill_dropdown["values"] = [item.title() for item in skills]
    skill_var.set("")

def update_problems(event=None):
    selected_apparatus = apparatus_var.get().lower()
    selected_skill = skill_var.get().lower()
    problems = drills[
        (drills["apparatus"] == selected_apparatus) &
        (drills["skill"] == selected_skill)
    ]["problem"].unique()
    problem_dropdown["values"] = [item.title() for item in problems]
    problem_var.set("")

# Put find_drills HERE
def find_drills():
    global video1_file, video2_file

    apparatus = apparatus_var.get().lower()
    skill = skill_var.get().lower()
    problem = problem_var.get().lower()

    recommendations = drills[
        (drills["apparatus"] == apparatus) &
        (drills["skill"] == skill) &
        (drills["problem"] == problem)
    ]

    output.delete(1.0, tk.END)  # Clear previous output

    if recommendations.empty:
        output.insert(tk.END, "No exact drills found.")
    else:
        for index, row in recommendations.iterrows():

            video1_file = row["video 1"]
            video2_file = row["video 2"]

            output.insert(tk.END, "Drill 1: " + str(row["drill 1"]) + "\n\n")
            output.insert(tk.END, "Drill 2: " + str(row["drill 2"]) + "\n\n")
            output.insert(tk.END, "Purpose: " + str(row["purpose"]) + "\n\n")
            output.insert(tk.END, "Level: " + str(row["level"]) + "\n")
            output.insert(tk.END, "Equipment: " + str(row["equipment"]) + "\n")
        


# ---------------- APPLICATION ----------------

# Colours
BACKGROUND = "#E6DACB"
CARD = "#F8F4EF"
TEXT = "#3F3A36"
SUBTEXT = "#756E68"
MAIN_BUTTON = "#A8C5B5"
VIDEO_BUTTON = "#D9B5B5"

# Main window
root = ctk.CTk()
root.title("MyDrill")
root.geometry("700x760")
root.configure(fg_color=BACKGROUND)


# ---------------- HEADER ----------------

title = ctk.CTkLabel(
    root,
    text="MyDrill",
    font=("Avenir", 38, "bold"),
    text_color=TEXT
)
title.pack(pady=(30, 0))

subtitle = ctk.CTkLabel(
    root,
    text="Find the right drill for your gymnast",
    font=("Avenir", 14),
    text_color=SUBTEXT
)
subtitle.pack(pady=(5, 25))


# ---------------- DROPDOWN STYLE ----------------

style = ttk.Style()
style.configure(
    "TCombobox",
    font=("Avenir", 12)
)


# ---------------- SELECTION CARD ----------------

selection_frame = ctk.CTkFrame(
    root,
    fg_color=CARD,
    corner_radius=20
)

selection_frame.pack(
    padx=50,
    pady=10,
    fill="x"
)


# ---------------- APPARATUS ----------------

ctk.CTkLabel(
    selection_frame,
    text="Apparatus",
    font=("Avenir", 13, "bold"),
    text_color=TEXT
).pack(
    anchor="w",
    padx=30,
    pady=(25, 5)
)

apparatus_var = tk.StringVar()

apparatus_dropdown = ttk.Combobox(
    selection_frame,
    textvariable=apparatus_var,
    state="readonly"
)

apparatus_dropdown["values"] = [
    item.title()
    for item in drills["apparatus"].unique()
]

apparatus_dropdown.pack(
    padx=30,
    fill="x"
)

apparatus_dropdown.bind(
    "<<ComboboxSelected>>",
    update_skills
)


# ---------------- SKILL ----------------

ctk.CTkLabel(
    selection_frame,
    text="Skill",
    font=("Avenir", 13, "bold"),
    text_color=TEXT
).pack(
    anchor="w",
    padx=30,
    pady=(18, 5)
)

skill_var = tk.StringVar()

skill_dropdown = ttk.Combobox(
    selection_frame,
    textvariable=skill_var,
    state="readonly"
)

skill_dropdown.pack(
    padx=30,
    fill="x"
)

skill_dropdown.bind(
    "<<ComboboxSelected>>",
    update_problems
)


# ---------------- PROBLEM ----------------

ctk.CTkLabel(
    selection_frame,
    text="What is the problem?",
    font=("Avenir", 13, "bold"),
    text_color=TEXT
).pack(
    anchor="w",
    padx=30,
    pady=(18, 5)
)

problem_var = tk.StringVar()

problem_dropdown = ttk.Combobox(
    selection_frame,
    textvariable=problem_var,
    state="readonly"
)

problem_dropdown.pack(
    padx=30,
    fill="x"
)


# ---------------- FIND DRILLS BUTTON ----------------

find_button = ctk.CTkButton(
    selection_frame,
    text="Find Drills",
    font=("Avenir", 14, "bold"),
    height=42,
    corner_radius=12,
    fg_color=MAIN_BUTTON,
    hover_color="#93B3A2",
    text_color="white",
    command=find_drills
)

find_button.pack(
    padx=30,
    pady=25,
    fill="x"
)


# ---------------- RESULTS TITLE ----------------

results_title = ctk.CTkLabel(
    root,
    text="Recommendation",
    font=("Avenir", 18, "bold"),
    text_color=TEXT
)

results_title.pack(
    anchor="w",
    padx=55,
    pady=(20, 5)
)


# ---------------- RESULTS CARD ----------------

results_frame = ctk.CTkFrame(
    root,
    fg_color=CARD,
    corner_radius=20
)

results_frame.pack(
    padx=50,
    pady=(0, 20),
    fill="both",
    expand=True
)

# ---------------- VIDEO BUTTON AREA ----------------

video_frame = ctk.CTkFrame(
    results_frame,
    fg_color="transparent"
)

video_frame.pack(
    padx=20,
    pady=(15, 20),
    fill="x"
)


video1_button = ctk.CTkButton(
    video_frame,
    text="Play Video 1",
    font=("Avenir", 12, "bold"),
    fg_color=VIDEO_BUTTON,
    hover_color="#C89F9F",
    text_color=TEXT,
    command=play_video1
)

video1_button.pack(
    side="left",
    expand=True,
    fill="x",
    padx=(0, 5)
)


video2_button = ctk.CTkButton(
    video_frame,
    text="Play Video 2",
    font=("Avenir", 12, "bold"),
    fg_color=VIDEO_BUTTON,
    hover_color="#C89F9F",
    text_color=TEXT,
    command=play_video2
)

video2_button.pack(
    side="left",
    expand=True,
    fill="x",
    padx=(5, 0)
)

# ---------------- OUTPUT AREA ----------------

output = tk.Text(
    results_frame,
    width=60,
    height=12,
    wrap="word",
    font=("Avenir", 12),
    bg=CARD,
    fg=TEXT,
    relief="flat",
    borderwidth=0,
    padx=10,
    pady=10
)

output.pack(
    padx=20,
    pady=(20, 10),
    fill="both",
    expand=True
)

# ---------------- START APPLICATION ----------------

print("Starting MyDrill application...")
root.mainloop()