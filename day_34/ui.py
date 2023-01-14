from tkinter import *
THEME_COLOR = "#375362"

class QuizUI:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzzes")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR).grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text= "Text",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        true_image = PhotoImage(file="day_34/images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, border=0)
        self.true_button.grid(row=2, column=0)
        
        false_image = PhotoImage(file="day_34/images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, border=0)
        self.false_button.grid(row=2, column=1)
        
        
        
        
        
        
        
        
        self.window.mainloop()