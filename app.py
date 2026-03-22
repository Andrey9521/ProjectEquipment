import sys
import requests
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTableWidget, QPushButton, QTableWidgetItem,
    QLineEdit, QMessageBox
)

API_URL = "http://127.0.0.1:8000"

class EquipmentApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Управління обладнанням")
        self.resize(900, 600)

        self.layout = QVBoxLayout()

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        control_layout = QHBoxLayout()

        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("ID обладнання")
        control_layout.addWidget(self.id_input)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Назва обладнання")
        control_layout.addWidget(self.name_input)

        self.type_input = QLineEdit()
        self.type_input.setPlaceholderText("Тип обладнання")
        control_layout.addWidget(self.type_input)

        self.status_input = QLineEdit()
        self.status_input.setPlaceholderText("Статус")
        control_layout.addWidget(self.status_input)

        self.room_input = QLineEdit()
        self.room_input.setPlaceholderText("Кабінет")
        control_layout.addWidget(self.room_input)

        self.problem_input = QLineEdit()
        self.problem_input.setPlaceholderText("Опис проблеми")
        control_layout.addWidget(self.problem_input)

        self.layout.addLayout(control_layout)

        button_layout = QHBoxLayout()

        self.load_button = QPushButton("Завантажити список")
        self.load_button.clicked.connect(self.load_equipment)
        button_layout.addWidget(self.load_button)

        self.add_button = QPushButton("Додати обладнання")
        self.add_button.clicked.connect(self.add_equipment)
        button_layout.addWidget(self.add_button)

        self.status_button = QPushButton("Оновити статус")
        self.status_button.clicked.connect(self.update_status)
        button_layout.addWidget(self.status_button)

        self.move_button = QPushButton("Перемістити")
        self.move_button.clicked.connect(self.move_equipment)
        button_layout.addWidget(self.move_button)

        self.problem_button = QPushButton("Додати проблему")
        self.problem_button.clicked.connect(self.add_problem)
        button_layout.addWidget(self.problem_button)

        self.search_button = QPushButton("Пошук за назвою")
        self.search_button.clicked.connect(self.search_equipment)
        button_layout.addWidget(self.search_button)

        self.save_button = QPushButton("Зберегти у файл")
        self.save_button.clicked.connect(self.save_equipment)
        button_layout.addWidget(self.save_button)

        self.layout.addLayout(button_layout)
        self.setLayout(self.layout)

    def load_equipment(self):
        response = requests.get(f"{API_URL}/equipment")
        if response.status_code == 200:
            data = response.json()
            self.table.setRowCount(len(data))
            self.table.setColumnCount(5)
            self.table.setHorizontalHeaderLabels(["ID", "Name", "Type", "Status", "Room"])
            for row, eq in enumerate(data):
                self.table.setItem(row, 0, QTableWidgetItem(str(eq["id"])))
                self.table.setItem(row, 1, QTableWidgetItem(eq["name"]))
                self.table.setItem(row, 2, QTableWidgetItem(eq["type"]))
                self.table.setItem(row, 3, QTableWidgetItem(eq["status"]))
                self.table.setItem(row, 4, QTableWidgetItem(eq["room"]))
            self.table.resizeColumnsToContents()

    def add_equipment(self):
        if self.name_input.text() and self.type_input.text() and self.status_input.text() and self.room_input.text():
            equipment = {
                "name": self.name_input.text(),
                "type": self.type_input.text(),
                "status": self.status_input.text(),
                "room": self.room_input.text()
            }
            response = requests.post(f"{API_URL}/add_equipment", json=equipment)
            QMessageBox.information(self, "Результат", response.json().get("message", "Помилка"))
        else:
            QMessageBox.warning(self, "Помилка", "Заповніть усі поля для додавання обладнання!")

    def update_status(self):
        equipment_id = self.id_input.text()
        status = self.status_input.text()
        if equipment_id and status:
            response = requests.put(f"{API_URL}/equipment/{equipment_id}/status", params={"status": status})
            QMessageBox.information(self, "Результат", response.json().get("message", "Помилка"))

    def move_equipment(self):
        equipment_id = self.id_input.text()
        new_room = self.room_input.text()
        if equipment_id and new_room:
            response = requests.put(f"{API_URL}/equipment/{equipment_id}/move", params={"new_room": new_room})
            QMessageBox.information(self, "Результат", response.json().get("message", "Помилка"))

    def add_problem(self):
        equipment_id = self.id_input.text()
        description = self.problem_input.text()
        if equipment_id and description:
            response = requests.post(f"{API_URL}/equipment/{equipment_id}/problem", params={"description": description})
            QMessageBox.information(self, "Результат", response.json().get("message", "Помилка"))

    def search_equipment(self):
        name = self.name_input.text()
        if name:
            response = requests.get(f"{API_URL}/equipment/search", params={"name": name})
            data = response.json()
            self.table.setRowCount(len(data))
            for row, eq in enumerate(data):
                self.table.setItem(row, 0, QTableWidgetItem(str(eq["id"])))
                self.table.setItem(row, 1, QTableWidgetItem(eq["name"]))
                self.table.setItem(row, 2, QTableWidgetItem(eq["type"]))
                self.table.setItem(row, 3, QTableWidgetItem(eq["status"]))
                self.table.setItem(row, 4, QTableWidgetItem(eq["room"]))

    def save_equipment(self):
        response = requests.post(f"{API_URL}/save")
        QMessageBox.information(self, "Результат", response.json().get("message", "Помилка"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EquipmentApp()
    window.show()
    sys.exit(app.exec())



