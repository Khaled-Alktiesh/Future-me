from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QCheckBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer
import sys

class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Future Me - Loading...")
        self.setGeometry(500, 200, 400, 300)
        self.setStyleSheet("background-color: #1E1E2E;")

        layout = QVBoxLayout()
        label = QLabel("Future Me", self)
        label.setFont(QFont("Arial", 24, QFont.Bold))
        label.setStyleSheet("color: #00D4FF;")
        label.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Shaping Your Tomorrow", self)
        subtitle.setFont(QFont("Arial", 12))
        subtitle.setStyleSheet("color: #CCCCCC;")
        subtitle.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)
        layout.addWidget(subtitle)
        self.setLayout(layout)

        QTimer.singleShot(3000, self.launch_main)

    def launch_main(self):
        self.main = MainApp()
        self.main.show()
        self.close()

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Future Me - Home Screen")
        self.setGeometry(400, 150, 600, 400)
        self.setStyleSheet("background-color: #282A36;")

        self.container = QWidget()
        self.setCentralWidget(self.container)

        self.layout = QVBoxLayout()
        self.container.setLayout(self.layout)

        # Button to open Mood-Linked Habit Logging
        habit_logging_button = QPushButton("Mood-Linked Habit Logging", self)
        habit_logging_button.setFont(QFont("Arial", 14))
        habit_logging_button.setStyleSheet("background-color: #32CD32; color: white; border-radius: 10px;")
        habit_logging_button.clicked.connect(self.open_habit_logging_screen)

        # Button to open Daily Motivation
        motivation_button = QPushButton("Daily Motivation", self)
        motivation_button.setFont(QFont("Arial", 14))
        motivation_button.setStyleSheet("background-color: #FFD700; color: white; border-radius: 10px;")
        motivation_button.clicked.connect(self.open_motivation_screen)

        # Button to open Challenge Mode
        challenge_button = QPushButton("Challenge Mode", self)
        challenge_button.setFont(QFont("Arial", 14))
        challenge_button.setStyleSheet("background-color: #FF6347; color: white; border-radius: 10px;")
        challenge_button.clicked.connect(self.open_challenge_screen)

        # Button to open Quick Habit Notes
        quick_notes_button = QPushButton("Quick Habit Notes", self)
        quick_notes_button.setFont(QFont("Arial", 14))
        quick_notes_button.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 10px;")
        quick_notes_button.clicked.connect(self.open_quick_notes_screen)

        # Button to choose today's mood
        mood_button = QPushButton("Choose Today's Mood", self)
        mood_button.setFont(QFont("Arial", 14))
        mood_button.setStyleSheet("background-color: #00D4FF; color: white; border-radius: 10px;")
        mood_button.clicked.connect(self.open_emoji_screen)

        # Add buttons to layout
        self.layout.addWidget(habit_logging_button)
        self.layout.addWidget(motivation_button)
        self.layout.addWidget(challenge_button)
        self.layout.addWidget(quick_notes_button)
        self.layout.addWidget(mood_button)

    def open_habit_logging_screen(self):
        self.habit_logging_screen = HabitLoggingScreen(self.show_home_screen)
        self.habit_logging_screen.show()
        self.close()

    def open_motivation_screen(self):
        self.motivation_screen = MotivationScreen(self.show_home_screen)
        self.motivation_screen.show()
        self.close()

    def open_challenge_screen(self):
        self.challenge_screen = ChallengeScreen(self.show_home_screen)
        self.challenge_screen.show()
        self.close()

    def open_quick_notes_screen(self):
        self.quick_notes_screen = QuickNotesScreen(self.show_home_screen)
        self.quick_notes_screen.show()
        self.close()

    def open_emoji_screen(self):
        self.emoji_screen = EmojiScreen(self.show_home_screen)
        self.emoji_screen.show()
        self.close()

    def show_home_screen(self):
        self.show()
        if hasattr(self, 'habit_logging_screen'):
            self.habit_logging_screen.close()
        if hasattr(self, 'motivation_screen'):
            self.motivation_screen.close()
        if hasattr(self, 'challenge_screen'):
            self.challenge_screen.close()
        if hasattr(self, 'quick_notes_screen'):
            self.quick_notes_screen.close()
        if hasattr(self, 'emoji_screen'):
            self.emoji_screen.close()

class EmojiScreen(QWidget):
    def __init__(self, back_function):
        super().__init__()
        self.setWindowTitle("Choose Today's Mood")
        self.setGeometry(500, 200, 600, 400)
        self.setStyleSheet("background-color: #282A36; color: white;")
        
        layout = QVBoxLayout()

        # Create emojis as buttons
        emoji_button1 = QPushButton("😀", self)
        emoji_button1.setFont(QFont("Segoe UI Emoji", 48))
        emoji_button1.clicked.connect(lambda: self.on_emoji_click("😀"))

        emoji_button2 = QPushButton("😐", self)
        emoji_button2.setFont(QFont("Segoe UI Emoji", 48))
        emoji_button2.clicked.connect(lambda: self.on_emoji_click("😐"))

        emoji_button3 = QPushButton("😢", self)
        emoji_button3.setFont(QFont("Segoe UI Emoji", 48))
        emoji_button3.clicked.connect(lambda: self.on_emoji_click("😢"))

        emoji_button4 = QPushButton("😡", self)
        emoji_button4.setFont(QFont("Segoe UI Emoji", 48))
        emoji_button4.clicked.connect(lambda: self.on_emoji_click("😡"))

        emoji_button5 = QPushButton("😍", self)
        emoji_button5.setFont(QFont("Segoe UI Emoji", 48))
        emoji_button5.clicked.connect(lambda: self.on_emoji_click("😍"))

        # Add the emoji buttons to the layout
        layout.addWidget(emoji_button1)
        layout.addWidget(emoji_button2)
        layout.addWidget(emoji_button3)
        layout.addWidget(emoji_button4)
        layout.addWidget(emoji_button5)

        # Back button to go back to home screen
        back_button = QPushButton("Back", self)
        back_button.setFont(QFont("Arial", 14))
        back_button.setStyleSheet("background-color: #FF6347; color: white; border-radius: 10px;")
        back_button.clicked.connect(back_function)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def on_emoji_click(self, emoji):
        todo_text = self.get_todo_for_emoji(emoji)
        self.todo_screen = ToDoScreen(emoji, todo_text)
        self.todo_screen.show()
        self.close()

    def get_todo_for_emoji(self, emoji):
        if emoji == "😀":
            return "Have a positive conversation with someone today!"
        elif emoji == "😐":
            return "Take a short break and relax."
        elif emoji == "😢":
            return "Journaling your feelings for today."
        elif emoji == "😡":
            return "Take a deep breath and try a calming exercise."
        elif emoji == "😍":
            return "Do something creative you enjoy today."
        return "Stay active and engaged in your tasks today."

# New Challenge Mode with goal setting and completion feature
class ChallengeScreen(QWidget):
    def __init__(self, back_function):
        super().__init__()
        self.setWindowTitle("Challenge Mode")
        self.setGeometry(500, 200, 600, 400)
        self.setStyleSheet("background-color: #282A36; color: white;")

        self.layout = QVBoxLayout()

        # Label for Challenge Mode
        label = QLabel("Welcome to Challenge Mode!", self)
        label.setFont(QFont("Arial", 18))
        label.setAlignment(Qt.AlignCenter)

        challenge_description = QLabel("Set your goals for today and check them off when done.", self)
        challenge_description.setFont(QFont("Arial", 14))
        challenge_description.setAlignment(Qt.AlignCenter)

        self.goal_input = QLineEdit(self)  # Input field for new goals
        self.goal_input.setFont(QFont("Arial", 14))
        self.goal_input.setPlaceholderText("Enter your goal for today...")
        
        # Button to add the goal
        add_goal_button = QPushButton("Add Goal", self)
        add_goal_button.setFont(QFont("Arial", 14))
        add_goal_button.setStyleSheet("background-color: #32CD32; color: white; border-radius: 10px;")
        add_goal_button.clicked.connect(self.add_goal)

        self.goal_list_layout = QVBoxLayout()  # Layout for displaying goals and checkboxes
        self.layout.addWidget(label)
        self.layout.addWidget(challenge_description)
        self.layout.addWidget(self.goal_input)
        self.layout.addWidget(add_goal_button)
        self.layout.addLayout(self.goal_list_layout)

        # Back button to go back to home screen
        back_button = QPushButton("Back", self)
        back_button.setFont(QFont("Arial", 14))
        back_button.setStyleSheet("background-color: #FF6347; color: white; border-radius: 10px;")
        back_button.clicked.connect(back_function)
        self.layout.addWidget(back_button)

        self.setLayout(self.layout)

    def add_goal(self):
        goal_text = self.goal_input.text()
        if goal_text:
            # Create a new checkbox for the goal
            goal_checkbox = QCheckBox(goal_text, self)
            self.goal_list_layout.addWidget(goal_checkbox)
            self.goal_input.clear()  # Clear the input field

class HabitLoggingScreen(QWidget):
    def __init__(self, back_function):
        super().__init__()
        self.setWindowTitle("Mood-Linked Habit Logging")
        self.setGeometry(500, 200, 600, 400)
        self.setStyleSheet("background-color: #282A36; color: white;")

        layout = QVBoxLayout()

        # Display the habit logging screen
        label = QLabel("Log your mood-linked habits for today", self)
        label.setFont(QFont("Arial", 18))
        label.setAlignment(Qt.AlignCenter)

        # Back button to go back to home screen
        back_button = QPushButton("Back", self)
        back_button.setFont(QFont("Arial", 14))
        back_button.setStyleSheet("background-color: #FF6347; color: white; border-radius: 10px;")
        back_button.clicked.connect(back_function)
        
        layout.addWidget(label)
        layout.addWidget(back_button)
        self.setLayout(layout)

class MotivationScreen(QWidget):
    def __init__(self, back_function):
        super().__init__()
        self.setWindowTitle("Daily Motivation")
        self.setGeometry(500, 200, 600, 400)
        self.setStyleSheet("background-color: #282A36; color: white;")

        layout = QVBoxLayout()

        # Display the motivation screen
        label = QLabel("Here's your daily motivation!", self)
        label.setFont(QFont("Arial", 18))
        label.setAlignment(Qt.AlignCenter)

        motivation_quote = QLabel("You are capable of achieving anything you set your mind to.", self)
        motivation_quote.setFont(QFont("Arial", 14))
        motivation_quote.setAlignment(Qt.AlignCenter)

        # Back button to go back to home screen
        back_button = QPushButton("Back", self)
        back_button.setFont(QFont("Arial", 14))
        back_button.setStyleSheet("background-color: #FF6347; color: white; border-radius: 10px;")
        back_button.clicked.connect(back_function)

        layout.addWidget(label)
        layout.addWidget(motivation_quote)
        layout.addWidget(back_button)
        self.setLayout(layout)

class QuickNotesScreen(QWidget):
    def __init__(self, back_function):
        super().__init__()
        self.setWindowTitle("Quick Habit Notes")
        self.setGeometry(500, 200, 600, 400)
        self.setStyleSheet("background-color: #282A36; color: white;")

        layout = QVBoxLayout()

        # Display the quick habit notes screen
        label = QLabel("Write quick habit notes", self)
        label.setFont(QFont("Arial", 18))
        label.setAlignment(Qt.AlignCenter)

        quick_notes_field = QLabel("Note down any thoughts or habits you'd like to track.", self)
        quick_notes_field.setFont(QFont("Arial", 14))
        quick_notes_field.setAlignment(Qt.AlignCenter)

        # Back button to go back to home screen
        back_button = QPushButton("Back", self)
        back_button.setFont(QFont("Arial", 14))
        back_button.setStyleSheet("background-color: #FF6347; color: white; border-radius: 10px;")
        back_button.clicked.connect(back_function)

        layout.addWidget(label)
        layout.addWidget(quick_notes_field)
        layout.addWidget(back_button)
        self.setLayout(layout)

class ToDoScreen(QWidget):
    def __init__(self, emoji, todo_text):
        super().__init__()
        self.setWindowTitle(f"To-Do for {emoji}")
        self.setGeometry(500, 200, 600, 400)
        self.setStyleSheet("background-color: #282A36; color: white;")

        layout = QVBoxLayout()

        emoji_label = QLabel(f"Emoji: {emoji}", self)
        emoji_label.setFont(QFont("Arial", 24))
        todo_label = QLabel(todo_text, self)
        todo_label.setFont(QFont("Arial", 18))

        layout.addWidget(emoji_label)
        layout.addWidget(todo_label)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Initialize the QApplication
    splash = SplashScreen()  # Show splash screen
    splash.show()  # Show splash screen window
    sys.exit(app.exec_())  # Start the application event loop
