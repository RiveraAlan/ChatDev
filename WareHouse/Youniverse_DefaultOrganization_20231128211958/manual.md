# Custom Children's Book App User Manual

## Introduction

The Custom Children's Book App is a software application that allows an agency to take Shopify orders from a store that creates custom children's books. The app uses AI agents to generate a personalized children's book based on user-provided information such as the child's image, name, gender, age, book theme, story setting, storyline preferences, favorite colors, and additional customization options. The app also includes a quality department that verifies the story and images of the book to ensure they meet the requirements. The art department generates AI images for each page of the book using the child's image as the main character.

This user manual provides detailed instructions on how to install the app's dependencies and how to use the app to generate custom children's books.

## Installation

To install the Custom Children's Book App, follow these steps:

1. Ensure that Python is installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Open a terminal or command prompt and navigate to the directory where you want to install the app.

3. Clone the ChatDev repository from GitHub by running the following command:

   ```
   git clone https://github.com/ChatDev/CustomChildrensBookApp.git
   ```

4. Navigate to the `CustomChildrensBookApp` directory:

   ```
   cd CustomChildrensBookApp
   ```

5. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary packages, including `numpy`, `pandas`, and `tkinter`.

6. Once the installation is complete, you are ready to use the Custom Children's Book App.

## Usage

To use the Custom Children's Book App, follow these steps:

1. Open a terminal or command prompt and navigate to the `CustomChildrensBookApp` directory.

2. Run the following command to start the app:

   ```
   python main.py
   ```

   This will launch the app's user interface.

3. In the app's user interface, you will see several input fields for the user-provided information. Fill in the required information, such as the child's image, name, gender, age, book theme, story setting, storyline preferences, and favorite colors. You can also provide any additional customization options.

4. Once you have filled in all the required information, click the "Generate Book" button.

5. The app will generate a custom children's book based on the provided information. The book will be displayed in the app's user interface.

6. The quality department will verify the story to ensure it meets the requirements. If the story passes the verification, the art department will generate AI images for each page of the book using the child's image as the main character.

7. The quality department will then verify the images to ensure they match the story and the child. If the images pass the verification, a success message will be displayed. Otherwise, an error message will be displayed.

8. You can close the app's user interface once you have generated and verified the custom children's book.

## Conclusion

The Custom Children's Book App provides an easy-to-use interface for generating personalized children's books based on user-provided information. By following the installation and usage instructions in this user manual, you can successfully use the app to create custom children's books tailored to each child's preferences.