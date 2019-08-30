# PyQt5 Example

This project gives an overview of a PyQt5 working environment.

## Getting Started

### Prerequisites

*None*

### Installation

Clone this repository on your local machine.

## Usage  

- Double-click **run.bat** located in your cloned repository.  
   *Alternatively* execute **run.bat** from the command window:
   ```
   run.bat
   ```
### Options

- The optional arguments **{options}** can be passed as follows:  
   ```
   run.bat {options}
   ```
- List of options:
   ```
   -h, --help            show this help message and exit
   -v, --verbose         display debug messages in console
   ```
- Show available options:  
   ```
   run.bat -h
   ```

### Using Qt Designer

Qt Designer is installed as part of [pyqt5-tools](https://github.com/altendky/pyqt5-tools)  
[A Quick Start to Qt Designer](https://doc.qt.io/archives/qt-4.8/designer-quick-start.html)  
[The inpiration for this project](https://relentlesscoding.com/2017/08/25/tutorial-rapid-gui-development-with-qt-designer-and-pyqt/)  

- Start **Qt Designer**:
   ```
   pyqt5designer.exe
   ```
- **Qt Designer** saves files in the **.ui** format.

### Import Widgets and Forms designed in Qt Designer

- Import **.ui** files directly in your Python code:
   ```
	from PyQt5 import uic
	my_dialog = uic.loadUi("my_dialog.ui", self)
   ```
   See **pyqt5_example\pyqt5_example.py** for a working example.