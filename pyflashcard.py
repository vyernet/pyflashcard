import pyttsx3
import tkinter as tk
from tkinter import ttk

# Flashcard data
flashcards = [
    {"question": "AWS Identity and Access Management (IAM) manages access to AWS services and resources such as:", "answer": "users, groups, and roles"},
    {"question": "AWS Cost Explorer lets you:", "answer": "visualize and analyze your AWS costs and usage over time"},
]

review_flashcards = []

total_flashcards = len(flashcards)
current_index = 0

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set the desired voice ID for "Microsoft Zira Desktop"
for voice in engine.getProperty('voices'):
    if "zira" in voice.id.lower():
        engine.setProperty('voice', voice.id)
        break

# Set speech rate to 115% of the default rate
rate = engine.getProperty('rate')
engine.setProperty('rate', int(rate * 1.15))

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to show next flashcard
def next_flashcard():
    global current_index
    if current_index < total_flashcards:
        card = flashcards[current_index]
        question_var.set("Question: " + card["question"])
        answer_var.set("Answer: " + card["answer"])
        root.update_idletasks()  # Ensure the GUI is updated before speaking
        root.after(500, lambda: speak(card["question"]))  # Delay to ensure text is updated before speaking
        root.after(1000, lambda: speak(card["answer"]))  # Additional delay for answer
        current_index += 1
        progress_var.set(f"Progress: {current_index}/{total_flashcards}")
    else:
        question_var.set("No more flashcards!")
        answer_var.set("")
        progress_var.set(f"Progress: {total_flashcards}/{total_flashcards}")

# Function to mark flashcard for review
def mark_for_review():
    if current_index > 0 and current_index <= total_flashcards:
        review_flashcards.append(flashcards[current_index - 1])
        review_var.set(f"Review Queue: {len(review_flashcards)}")

# Function to review flashcards
def review_flashcards_func():
    global current_index
    current_index = 0
    if review_flashcards:
        flashcards.extend(review_flashcards)
        review_flashcards.clear()
        total_flashcards = len(flashcards)
        review_var.set(f"Review Queue: {len(review_flashcards)}")
        next_flashcard()
    else:
        question_var.set("No flashcards to review!")
        answer_var.set("")

# Create GUI
root = tk.Tk()
root.title("Flashcards")
root.geometry("500x300")  # Set a consistent static window size

frame = ttk.Frame(root, padding="20")
frame.pack(expand=True, fill=tk.BOTH)

question_var = tk.StringVar()
answer_var = tk.StringVar()
progress_var = tk.StringVar(value=f"Progress: 0/{total_flashcards}")
review_var = tk.StringVar(value="Review Queue: 0")

question_label = ttk.Label(frame, textvariable=question_var, wraplength=450, anchor="center", font=("Helvetica", 12, "bold"))
question_label.pack(expand=True)

answer_label = ttk.Label(frame, textvariable=answer_var, wraplength=450, anchor="center", font=("Helvetica", 16, "bold"))
answer_label.pack(expand=True)

progress_label = ttk.Label(frame, textvariable=progress_var, anchor="center")
progress_label.pack()

review_label = ttk.Label(frame, textvariable=review_var, anchor="center")
review_label.pack()

next_button = ttk.Button(frame, text="Next", command=next_flashcard)
next_button.pack(pady=(5, 5))

review_button = ttk.Button(frame, text="Mark for Review", command=mark_for_review)
review_button.pack(pady=(5, 5))

start_review_button = ttk.Button(frame, text="Review Marked Flashcards", command=review_flashcards_func)
start_review_button.pack(pady=(5, 5))

root.bind('<Return>', lambda event: next_flashcard())

# Display greeting message
question_var.set("Welcome to Py Flashcards!")
answer_var.set("Press 'Next' to start.")

# Start the GUI loop
root.mainloop()
