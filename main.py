import sys
import os
import base64
import xml.etree.ElementTree as ET
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLineEdit, QTableWidget, 
                             QTableWidgetItem, QFileDialog, QHeaderView, QLabel,
                             QMessageBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QFont, QIcon

class ServerXMLViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FZ Credential Extractor")
        self.resize(1200, 700)
        
        self.headers = ["Host", "Port", "Protocol", "Type", "User", "Pass", 
                        "Logontype", "PasvMode", "EncodingType", "BypassProxy", 
                        "Name", "Colour", "SyncBrowsing", "DirectoryComparison"]

        self.setup_ui()
        self.apply_styles()

    def setup_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(15)

        # Header Section
        header_layout = QHBoxLayout()
        
        self.btn_load = QPushButton("Load XML File")
        self.btn_load.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_load.clicked.connect(self.load_xml)
        self.btn_load.setFixedWidth(200)
        self.btn_load.setHeight = 40
        
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search servers...")
        self.search_input.textChanged.connect(self.filter_table)
        
        header_layout.addWidget(self.btn_load)
        header_layout.addWidget(self.search_input)
        
        self.layout.addLayout(header_layout)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(len(self.headers))
        self.table.setHorizontalHeaderLabels(self.headers)
        
        # Headers styling
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        header.setStretchLastSection(True)
        
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        
        self.layout.addWidget(self.table)
        
        # Status Bar
        self.status_label = QLabel("Ready")
        self.status_label.setStyleSheet("color: #7f849c; font-size: 12px;")
        self.statusBar().addWidget(self.status_label)

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def apply_styles(self):
        try:
            style_path = self.resource_path("styles.qss")
            with open(style_path, "r") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            print("Warning: styles.qss not found. Using default styles.")

    def load_xml(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open XML File", "", "XML Files (*.xml);;All Files (*)")
        if file_name:
            try:
                self.parse_and_display(file_name)
                self.status_label.setText(f"Loaded: {file_name}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to parse XML:\n{str(e)}")

    def parse_and_display(self, file_path):
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            servers = root.findall('.//Server')
            
            if not servers and root.tag == 'Server':
                servers = [root]

            if not servers:
                raise Exception("The XML file does not contain any 'Server' elements or has an invalid structure.")

            self.table.setRowCount(0)
            self.table.setRowCount(len(servers))
            
            for row_idx, server in enumerate(servers):
                for col_idx, key in enumerate(self.headers):
                    item_text = ""
                    # Direct child search
                    child = server.find(key)
                    
                    if child is not None:
                        # Helper text extraction
                        raw_text = child.text if child.text else ""
                        
                        if key == "Pass":
                            # Check encoding attribute
                            encoding = child.get("encoding")
                            if encoding == "base64":
                                try:
                                    decoded_bytes = base64.b64decode(raw_text)
                                    item_text = decoded_bytes.decode('utf-8', errors='replace')
                                except Exception:
                                    item_text = f"[Decode Error: {raw_text}]"
                            else:
                                item_text = raw_text
                        else:
                            item_text = raw_text
                    
                    table_item = QTableWidgetItem(item_text)
                    self.table.setItem(row_idx, col_idx, table_item)
            
            self.table.resizeColumnsToContents()
            
        except ET.ParseError as e:
            raise Exception(f"Invalid XML syntax: {e}")
        except Exception as e:
             raise Exception(f"Processing error: {e}")

    def filter_table(self):
        search_text = self.search_input.text().lower()
        for row in range(self.table.rowCount()):
            match_found = False
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                if item and search_text in item.text().lower():
                    match_found = True
                    break
            self.table.setRowHidden(row, not match_found)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit Confirmation', 
                                     "Are you sure you want to exit the application?", 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

def main():
    app = QApplication(sys.argv)
    window = ServerXMLViewer()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
