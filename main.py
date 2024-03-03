import json
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.read_notes()
        self.ui.notes_list.addItems(self.notes)
        self.ui.notes_list.itemClicked.connect(self.show_note)
        self.ui.save_btn.clicked.connect(self.save_note)
        self.ui.create_btn.clicked.connect(self.create_note)
        self.ui.delete_btn.clicked.connect(self.delete_note)

    def show_note(self):
        self.name = self.ui.notes_list.selectedItems()[0].text()
        self.ui.title_edit.setText( self.name)
        self.ui.text_edit.setText(self.notes[self.name]["текст"])

    def save_note(self):
        self.notes[self.ui.title_edit.text()] =  {
                "текст": self.ui.text_edit.toPlainText(),
                "теги": []
        }
        with open("notes.json", "w", encoding="utf-8") as file:
            json.dump(self.notes, file)
        self.ui.notes_list.clear()
        self.ui.notes_list.addItems(self.notes)

    def clear(self):
        self.ui.title_edit.clear()
        self.ui.text_edit.clear()

    def create_note(self):
        self.clear()

    def read_notes(self):
        try:
            with open("notes.json", "r", encoding="utf-8") as file:
                self.notes = json.load(file)
        except:
            self.notes = {
                "Перша замітка":{
                    "текст": "Це текст першої замітки",
                    "теги": []
                }
            }
        
    def delete_note(self):
        try:
            del self.notes[self.name]
            self.clear()
            self.ui.notes_list.clear()
            self.ui.notes_list.addItems(self.notes)
            self.save_note()
        except:
            print("помилка видалення")


    def add_tag(self):
        tag_name = self.ui.tag_edit.text()
        if tag_name!="":
            if ta not




app = QApplication([])
ex = Widget()   
ex.show()
app.exec_()

# python -m PyQt5.uic.pyuic -x untitled.ui -o ui.py
