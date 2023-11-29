'''
This file contains the BookGenerator class that generates a custom children's book based on user inputs.
'''
class BookGenerator:
    def generate_book(self, child_image, child_name, child_gender):
        # Generate the book based on user inputs
        # Add your implementation here
        # Replace the following code with your implementation
        book = []
        book.append(Page(1, "Once upon a time", child_image))
        book.append(Page(2, "There was a child named " + child_name, child_image))
        book.append(Page(3, "The child was " + child_gender, child_image))
        return book
class Page:
    def __init__(self, page_number, text, child_image):
        self.page_number = page_number
        self.text = text
        self.child_image = child_image