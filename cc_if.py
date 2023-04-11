"""
  Students  |  Grades  |  Letters
------------|----------|----------
  George    |  46      |  F
  Michell   |  80      |  B
  Josh      |  12      |  F
  Chloe     |  68      |  D
  Stanley   |  99      |  A
  Annie     |  100     |  A+
"""
import tkinter as tk


def calculate_grade():
    gradeToTest = int(student_grade.get())
    if gradeToTest == 100:
        grade.config(text="A+")
    elif gradeToTest >= 90:
        grade.config(text="A")
    elif gradeToTest >= 80:
        grade.config(text="B")
    elif gradeToTest >= 70:
        grade.config(text="C")
    elif gradeToTest >= 60:
        grade.config(text="D")
    else:
        grade.config(text="F")


# Create a window (top-level widget) using the Tk class
root = tk.Tk()
root.title("Grade Calculator")
root.geometry("400x220")
# Create widgets (labels, buttons, entry boxes) and add them to the window
grade_label = tk.Label(root, text="Enter student grade:")
grade_label.pack()

student_grade = tk.Entry(root)
student_grade.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_grade)
calculate_button.pack()

grade = tk.Label(root, text="")
grade.pack()

# Start the GUI event loop
root.mainloop()
