# Generated script using ChatGPT
# I looked for a tool to display directories and files. I saw an example using
# PyQT5 and had some ideas, so I asked ChatGPT to generate the code ;-)

import sys
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout, QHBoxLayout, QFileDialog, QLabel, QPushButton, QCheckBox


class DirTreeView(QWidget):
    def __init__(self):
        super().__init__()

        # Create a file system model
        self.model = QFileSystemModel()

        # Only display directories in the tree view by default
        self.model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)

        # Create a tree view widget
        self.tree_view = QTreeView()

        # Create a label to display the selected directory path
        self.path_label = QLabel("Selected Path: ")

        # Create a button to select a directory
        self.select_dir_button = QPushButton("Select Directory")
        self.select_dir_button.clicked.connect(self.select_directory)

        # Create a checkbox to show/hide files in the tree view
        self.show_files_checkbox = QCheckBox("Show Files")
        self.show_files_checkbox.stateChanged.connect(self.show_files_changed)

        # Create a button to expand all folders
        self.expand_button = QPushButton("Expand All")
        self.expand_button.clicked.connect(self.expand_all)

        # Create a button to collapse all folders
        self.collapse_button = QPushButton("Collapse All")
        self.collapse_button.clicked.connect(self.collapse_all)

        # Create a layout for the expand/collapse buttons and show files checkbox
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.show_files_checkbox)
        button_layout.addWidget(self.expand_button)
        button_layout.addWidget(self.collapse_button)

        # Add the label, buttons, checkbox, and tree view to the main layout
        layout = QVBoxLayout()
        layout.addWidget(self.path_label)
        layout.addWidget(self.select_dir_button)
        layout.addLayout(button_layout)
        layout.addWidget(self.tree_view)
        self.setLayout(layout)

        # Initialize the file system model and tree view to show all available drives
        self.model.setRootPath('')
        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(''))
        self.tree_view.setSortingEnabled(True)

        # Set the size of the first column of the tree view to 450 pixels
        self.tree_view.header().resizeSection(0, 450)

        # Resize the widget to the desired size
        self.resize(800, 480)

    def select_directory(self):
        # Show a directory dialog to select a directory
        dir_path = QFileDialog.getExistingDirectory(self, "Select Directory")

        if dir_path:
            # Update the file system model and tree view with the new directory path
            self.model.setRootPath(dir_path)
            self.tree_view.setModel(self.model)
            self.tree_view.setRootIndex(self.model.index(dir_path))
            # Update the path label with the selected directory path
            self.path_label.setText(f"Selected Path: {dir_path}")

    def show_files_changed(self, state):
        # Show or hide files in the tree view depending on the checkbox state
        if state == 0:
            self.model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)
        else:
            self.model.setFilter(QDir.AllEntries | QDir.NoDotAndDotDot)
        self.tree_view.setModel(self.model)

    def expand_all(self):
        # Expand all folders and subfolders in the tree view
        self.tree_view.expandAll()

    def collapse_all(self):
        # Collapse all folders and subfolders in the tree view
        self.tree_view.collapseAll()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create the directory tree view widget
    tree_view = DirTreeView()
    tree_view.show()

    sys.exit(app.exec_())
