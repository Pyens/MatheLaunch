from PIL import Image, ImageTk
import tkinter as tk


# Quiz data
questions = (
    "What type of geometry is evident in this image?",
    "What type of geometry is evident in this image?",
    "What type of geometry is evident in this image?",
    "What type of geometry is evident in this image?"
)

# Image file paths for each question 
image_paths = [
    "fractal.jpg",      # Image for question 1
    "hyperbolic.jpg",        # Image for question 2
    "euclidean.jpg",       # Image for question 3
    "spherical.jpeg"     # Image for question 4
]

options = (
    ("A. Fractal", "B. Spherical", "C. Euclidean", "D. Hyperbolic"),
    ("A. Fractal", "B. Spherical", "C. Euclidean", "D. Hyperbolic"),
    ("A. Fractal", "B. Spherical", "C. Euclidean", "D. Hyperbolic"),
    ("A. Fractal", "B. Spherical", "C. Euclidean", "D. Hyperbolic")
)

answers = ("A", "D", "C", "B")
guesses = []
score = 0
question_num = 0

# Create main window
root = tk.Tk()
root.title("Quiz Game")
root.geometry("800x600")

# Image display label
image_label = tk.Label(root)
image_label.pack(pady=10)

# Question label
question_label = tk.Label(root, text="", font=("Arial", 14))
question_label.pack(pady=20)

# Options frame
options_frame = tk.Frame(root)
options_frame.pack(pady=20)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Score label
score_label = tk.Label(root, text=f"Score: {score}/{len(questions)}", font=("Arial", 12))
score_label.pack()

def show_question():
    global question_num
    
    if question_num < len(questions):
        # Display question
        question_label.config(text=questions[question_num])
        
        # Display image
        try:
            img = Image.open(image_paths[question_num])
            img = img.resize((400, 300), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            image_label.config(image=photo)
            image_label.image = photo  # Keep a reference
        except FileNotFoundError:
            image_label.config(text="Image not found", image='')
        
        # Clear previous options
        for widget in options_frame.winfo_children():
            widget.destroy()
            
        # Display options
        for i, option in enumerate(options[question_num]):
            btn = tk.Button(options_frame, text=option, font=("Arial", 12),
                           command=lambda idx=i: check_answer(chr(65 + idx)))
            btn.pack(fill='x', pady=5)
    else:
        show_results()

def check_answer(selected):
    global score, question_num
    
    correct_answer = answers[question_num]
    guesses.append(selected)
    
    if selected == correct_answer:
        score += 1
        result_label.config(text="CORRECT!", fg="green")
    else:
        result_label.config(text=f"INCORRECT! The correct answer is {correct_answer}", fg="red")
    
    question_num += 1
    score_label.config(text=f"Score: {score}/{len(questions)}")
    root.after(1500, show_question)  # Wait 1.5 seconds before next question

def show_results():
    for widget in root.winfo_children():
        widget.destroy()
    
    final_score = int(score / len(questions) * 100)
    
    result_text = (
        f"Quiz Completed!\n\n"
        f"Final Score: {score}/{len(questions)}\n"
        f"Percentage: {final_score}%\n\n"
        f"Correct Answers: {' '.join(answers)}\n"
        f"Your Answers: {' '.join(guesses)}"
    )
    
    tk.Label(root, text="RESULTS", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(root, text=result_text, font=("Arial", 12)).pack(pady=20)
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=10)

# Start the quiz
show_question()
root.mainloop()