# main.py

import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from database import init_db  # Import at the top as usual
from app import ExpenseApp

def main():
    # Initialize the application
    app = QApplication(sys.argv)

    # Initialize Database after QApplication instance is created
    if not init_db("expense.db"):
        QMessageBox.critical(None, "Error", "Could not open your database")
        sys.exit(1)

    # Create and show the main window
    window = ExpenseApp()
    window.show()

    # Start the application's event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
