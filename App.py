import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

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

        # Button to choose today's mood
        mood_button = QPushButton("Choose Today's Mood", self)
        mood_button.setFont(QFont("Arial", 14))
        mood_button.setStyleSheet("background-color: #00D4FF; color: white; border-radius: 10px;")
        mood_button.clicked.connect(self.open_emoji_screen)

        # Add buttons to layout
        self.layout.addWidget(habit_logging_button)
        self.layout.addWidget(motivation_button)
        self.layout.addWidget(challenge_button)
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
        if hasattr(self, 'emoji_screen'):
            self.emoji_screen.close()


class HabitLoggingScreen(QWidget):
    def __init__(self, back_function):
        super().__init__()
        self.setWindowTitle("Mood-Linked Habit Logging")
        self.setGeometry(500, 200, 600, 400)
        self.setStyleSheet("background-color: #282A36; color: white;")

        layout = QVBoxLayout()

        label = QLabel("Log your mood-linked habits for today", self)
        label.setFont(QFont("Arial", 18))
        label.setAlignment(Qt.AlignCenter)

        # ComboBox for selecting mood
        self.mood_combo = QComboBox(self)
        self.mood_combo.addItems(["😀 Happy", "😐 Neutral", "😢 Sad", "😡 Angry", "😍 Loved"])
        self.mood_combo.setFont(QFont("Arial", 14))

        # Text field for entering habit note
        self.habit_note_input = QLineEdit(self)
        self.habit_note_input.setFont(QFont("Arial", 14))
        self.habit_note_input.setPlaceholderText("Enter your habit note for today...")

        # Button to save the habit log
        save_button = QPushButton("Save Habit Log", self)
        save_button.setFont(QFont("Arial", 14))
        save_button.setStyleSheet("background-color: #32CD32; color: white; border-radius: 10px;")
        save_button.clicked.connect(self.save_habit_log)

        # Back button to go back to home screen
        back_button = QPushButton("Back", self)
        back_button.setFont(QFont("Arial", 14))
        back_button.setStyleSheet("background-color: #FF6347; color: white; border-radius: 10px;")
        back_button.clicked.connect(back_function)

        layout.addWidget(label)
        layout.addWidget(self.mood_combo)
        layout.addWidget(self.habit_note_input)
        layout.addWidget(save_button)
        layout.addWidget(back_button)
        self.setLayout(layout)

    def save_habit_log(self):
        mood = self.mood_combo.currentText()
        habit_note = self.habit_note_input.text()

        if habit_note:
            print(f"Logged Habit for {mood}: {habit_note}")
            self.habit_note_input.clear()  # Clear the input field after saving
        else:
            print("Please enter a habit note.")


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
        mood_message = self.get_mood_message(emoji)
        self.mood_message_screen = MoodMessageScreen(mood_message)
        self.mood_message_screen.show()
        self.close()

    def get_mood_message(self, emoji):
        if emoji == "😀":
            return "You are feeling great today! Keep spreading positivity!"
        elif emoji == "😐":
            return "You're feeling neutral, take it easy and relax."
        elif emoji == "😢":
            return "It looks like you're feeling sad. Take care of yourself."
        elif emoji == "😡":
            return "You're angry. Try to calm down with some breathing exercises."
        elif emoji == "😍":
            return "You're in love with life today! Enjoy the moment."


class MoodMessageScreen(QWidget):
    def __init__(self, message):
        super().__init__()
        self.setWindowTitle("Mood Message")
        self.setGeometry(500, 200, 600, 400)
        self.setStyleSheet("background-color: #282A36; color: white;")
        layout = QVBoxLayout()

        # Display the mood message
        label = QLabel(message, self)
        label.setFont(QFont("Arial", 16))
        label.setAlignment(Qt.AlignCenter)

        # Button to go back
        back_button = QPushButton("Back", self)
        back_button.setFont(QFont("Arial", 14))
        back_button.setStyleSheet("background-color: #FF6347; color: white; border-radius: 10px;")
        back_button.clicked.connect(self.close)

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

        # List of motivational quotes
        quotes = [
            "The only way to do great work is to love what you do.",
            "Success is not final, failure is not fatal: It is the courage to continue that counts.",
            "The only limit to our realization of tomorrow is our doubts of today.",
            "It always seems impossible until it’s done.",
            "Don’t watch the clock; do what it does. Keep going."
        ]

        # Randomly choose a quote
        motivational_quote = random.choice(quotes)

        # Display the motivational quote
        label = QLabel(motivational_quote, self)
        label.setFont(QFont("Arial", 18))
        label.setAlignment(Qt.AlignCenter)

        # Button to go back
        back_button = QPushButton("Back", self)
        back_button.setFont(QFont("Arial", 14))
        back_button.setStyleSheet("background-color: #FF6347; color: white; border-radius: 10px;")
        back_button.clicked.connect(back_function)

        layout.addWidget(label)
        layout.addWidget(back_button)
        self.setLayout(layout)


class ChallengeScreen(QWidget):
    def __init__(self, back_function):
        super().__init__()
        self.setWindowTitle("Challenge Mode")
        self.setGeometry(500, 200, 600, 400)
        self.setStyleSheet("background-color: #282A36; color: white;")
        
        self.layout = QVBoxLayout()

        self.challenge_list = []
        
        # Label to guide user
        label = QLabel("Enter your challenges below:", self)
        label.setFont(QFont("Arial", 18))
        label.setAlignment(Qt.AlignCenter)

        # Text field for entering challenge
        self.challenge_input = QLineEdit(self)
        self.challenge_input.setFont(QFont("Arial", 14))
        self.challenge_input.setPlaceholderText("Enter a challenge")

        # Button to save the challenge
        save_button = QPushButton("Save Challenge", self)
        save_button.setFont(QFont("Arial", 14))
        save_button.setStyleSheet("background-color: #32CD32; color: white; border-radius: 10px;")
        save_button.clicked.connect(self.save_challenge)

        # Display list of challenges
        self.challenge_display = QLabel("Challenges will appear here", self)
        self.challenge_display.setFont(QFont("Arial", 14))
        self.challenge_display.setAlignment(Qt.AlignCenter)

        # Button to go back
        back_button = QPushButton("Back", self)
        back_button.setFont(QFont("Arial", 14))
        back_button.setStyleSheet("background-color: #FF6347; color: white; border-radius: 10px;")
        back_button.clicked.connect(back_function)

        self.layout.addWidget(label)
        self.layout.addWidget(self.challenge_input)
        self.layout.addWidget(save_button)
        self.layout.addWidget(self.challenge_display)
        self.layout.addWidget(back_button)
        self.setLayout(self.layout)

    def save_challenge(self):
        challenge_text = self.challenge_input.text()

        if challenge_text:
            self.challenge_list.append(challenge_text)
            self.challenge_display.setText("\n".join(self.challenge_list))
            self.challenge_input.clear()  # Clear the input field after saving


if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash_screen = SplashScreen()
    splash_screen.show()
    sys.exit(app.exec_())
