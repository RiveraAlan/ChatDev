'''
This is the main file of the AI Generated Children's Book application.
It contains the GUI implementation and handles user inputs and outputs.
'''
import tkinter as tk
from book_generator import BookGenerator
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AI Generated Children's Book")
        # Create input fields
        self.image_input = tk.Entry(self)
        self.name_input = tk.Entry(self)
        self.gender_input = tk.Entry(self)
        self.age_input = tk.Entry(self)
        self.occasion_input = tk.Entry(self)
        self.theme_input = tk.Entry(self)
        self.story_setting_input = tk.Entry(self)
        self.storyline_preferences_input = tk.Entry(self)
        self.notes_input = tk.Text(self)
        # Create submit button
        self.submit_button = tk.Button(self, text="Generate Book", command=self.generate_book)
        # Create output text area
        self.output_text = tk.Text(self, height=10, width=50)
        # Layout input fields, submit button, and output text area
        self.image_input.pack()
        self.name_input.pack()
        self.gender_input.pack()
        self.age_input.pack()
        self.occasion_input.pack()
        self.theme_input.pack()
        self.story_setting_input.pack()
        self.storyline_preferences_input.pack()
        self.notes_input.pack()
        self.submit_button.pack()
        self.output_text.pack()
    def generate_book(self):
        # Get user inputs
        image = self.image_input.get()
        name = self.name_input.get()
        gender = self.gender_input.get()
        age = self.age_input.get()
        occasion = self.occasion_input.get()
        theme = self.theme_input.get()
        story_setting = self.story_setting_input.get()
        storyline_preferences = self.storyline_preferences_input.get()
        notes = self.notes_input.get("1.0", tk.END)
        # Generate book
        book_generator = BookGenerator()
        book = book_generator.generate_book(image, name, gender, age, occasion, theme, story_setting, storyline_preferences, notes)
        # Display book in output text area
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, book)
if __name__ == "__main__":
    app = App()
    app.mainloop()