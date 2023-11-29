'''
This is the main file that handles the user interface and coordinates the different components of the software.
'''
from tkinter import Tk, Label, Button, Entry, OptionMenu, messagebox
from book_generator import BookGenerator, Page
from quality_department import QualityDepartment
from art_department import ArtDepartment
class CustomChildrensBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Children's Book App")
        # Create labels and entry fields for user input
        self.child_image_label = Label(root, text="Child Image:")
        self.child_image_label.pack()
        self.child_image_entry = Entry(root)
        self.child_image_entry.pack()
        self.child_name_label = Label(root, text="Child Name:")
        self.child_name_label.pack()
        self.child_name_entry = Entry(root)
        self.child_name_entry.pack()
        self.child_gender_label = Label(root, text="Child Gender:")
        self.child_gender_label.pack()
        self.child_gender_entry = Entry(root)
        self.child_gender_entry.pack()
        # Add more labels and entry fields for other user inputs
        self.generate_button = Button(root, text="Generate Book", command=self.generate_book)
        self.generate_button.pack()
    def generate_book(self):
        # Get user inputs
        child_image = self.child_image_entry.get()
        child_name = self.child_name_entry.get()
        child_gender = self.child_gender_entry.get()
        # Create a book generator instance
        book_generator = BookGenerator()
        # Generate the book based on user inputs
        book = book_generator.generate_book(child_image, child_name, child_gender)
        # Create a quality department instance
        quality_department = QualityDepartment()
        # Verify the story meets requirements
        if quality_department.verify_story(book):
            # Create an art department instance
            art_department = ArtDepartment()
            # Generate AI images for each page of the book
            book_with_images = art_department.generate_images(book)
            # Verify the images match the story and the child
            if quality_department.verify_images(book_with_images):
                # Display a success message
                messagebox.showinfo("Success", "Custom children's book has been generated successfully!")
            else:
                # Display an error message
                messagebox.showerror("Error", "Images do not match the story and the child.")
        else:
            # Display an error message
            messagebox.showerror("Error", "Story does not meet requirements.")
# Create the main window
root = Tk()
# Create an instance of the custom children's book app
app = CustomChildrensBookApp(root)
# Run the application
root.mainloop()