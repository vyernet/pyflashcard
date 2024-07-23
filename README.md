# Py Flashcards

Py Flashcards is an interactive study tool designed to help users learn and review concepts through flashcards. Featuring text-to-speech functionality and progress tracking, this application offers a dynamic and engaging way to prepare for certifications and improve your knowledge.

## Features

- **Flashcards**: Review various concepts with flashcards.
- **Text-to-Speech**: Hear the questions and answers read aloud using text-to-speech.
- **Progress Tracking**: Track your progress through the flashcards.
- **Review Mode**: Mark flashcards for review and revisit them later.
- **Customizable Text**: Bold and larger text for improved readability.

## Requirements

- Python 3.x
- `pyttsx3` library
- `tkinter` library (usually included with Python)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/vyernet/pyflashcard.git
    cd pyflashcard
    ```

2. Install the required Python packages:

    ```bash
    pip install pyttsx3
    ```

## Usage

1. Run the application:

    ```bash
    python pyflashcard.py
    ```

2. Use the "Next" button or press the `Enter` key to move to the next flashcard.
3. Click "Mark for Review" to add a flashcard to the review queue.
4. Click "Review Marked Flashcards" to review the flashcards you've marked.

## Customization

You can customize the flashcards by modifying the `flashcards` list in the `pyflashcard` file. Each flashcard should be a dictionary with `question` and `answer` keys.

```python
flashcards = [
    {"question": "AWS Identity and Access Management (IAM) manages access to AWS services and resources such as:", "answer": "users, groups, and roles"},
    {"question": "AWS Cost Explorer lets you:", "answer": "visualize and analyze your AWS costs and usage over time"},
    # Add more flashcards here
]
