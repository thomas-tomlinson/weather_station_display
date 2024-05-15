# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from panels.wind_direction import WindDirection

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        MainWindow.setMaximumSize(QtCore.QSize(800, 601))
        MainWindow.setStyleSheet("/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"    background-color: #121212;\n"
"    color: #ffffff;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel::disabled\n"
"{\n"
"    background-color: transparent;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenuBar-----*/\n"
"QMenuBar\n"
"{\n"
"    background-color: #0a0a0a;\n"
"    color: #ffffff;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background-color: #607cff;\n"
"    border: 1px solid #41cd52;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background-color: #4969ff;\n"
"    border: 1px solid #000;\n"
"    margin-bottom: -1px;\n"
"    padding-bottom: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: #121212;\n"
"    border: 1px solid;\n"
"    color: #ffffff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #6d8eff;\n"
"    color: #ffffff;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    min-width : 150px;\n"
"    padding: 3px 20px 3px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: #4969ff;\n"
"    color: #ffffff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #262626;\n"
"}\n"
"\n"
"\n"
"/*-----QToolTip-----*/\n"
"QToolTip\n"
"{\n"
"    border : 1px solid #000000;\n"
"    background-color: #26264f;\n"
"    color: #ffffff;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"    background-color: #607cff;\n"
"    color: #ffffff;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    border-color: #051a39;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: #8399ff;\n"
"    color: #ffffff;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    border-color: #051a39;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: #4969ff;\n"
"    color: #ffffff;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    border-color: #051a39;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton\n"
"{\n"
"    background-color: #607cff;\n"
"    color: #ffffff;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    border-color: #051a39;\n"
"    padding: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::hover\n"
"{\n"
"    background-color: #8399ff;\n"
"    color: #ffffff;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    border-color: #051a39;\n"
"    padding: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::pressed\n"
"{\n"
"    background-color: #4969ff;\n"
"    color: #ffffff;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    border-color: #051a39;\n"
"    padding: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QComboBox-----*/\n"
"QComboBox\n"
"{\n"
"    background-color: #607cff;\n"
"    border: 1px solid;\n"
"    border-radius: 3px;\n"
"    padding-left: 6px;\n"
"    color: #ffffff;\n"
"    height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:hover\n"
"{\n"
"    background-color: #8399ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #4969ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #383838;\n"
"    color: #ffffff;\n"
"    border: 1px solid black;\n"
"    selection-background-color: #4969ff;\n"
"    selection-color: #ffffff;\n"
"    outline: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"\n"
"/*-----QSpinBox & QDoubleSpinBox & QDateTimeEdit-----*/\n"
"QSpinBox,\n"
"QDoubleSpinBox,\n"
"QDateTimeEdit\n"
"{\n"
"    background-color: #525251;\n"
"    color: #ffffff;\n"
"    border: 1px solid #051a39;\n"
"    border-radius: 3px;\n"
"    padding : 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::disabled,\n"
"QDoubleSpinBox::disabled,\n"
"QDateTimeEdit::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox:hover,\n"
"QDoubleSpinBox::hover,\n"
"QDateTimeEdit::hover\n"
"{\n"
"    background-color: #626262;\n"
"    border: 1px solid #607cff;\n"
"    color:  #fff;\n"
"    padding: 2px\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button,\n"
"QDoubleSpinBox::up-button, QDoubleSpinBox::down-button,\n"
"QDateTimeEdit::up-button, QDateTimeEdit::down-button\n"
"{\n"
"    background-color: #607cff;\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::disabled,\n"
"QDoubleSpinBox::disabled,\n"
"QDateTimeEdit::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover,\n"
"QDoubleSpinBox::up-button:hover, QDoubleSpinBox::down-button:hover,\n"
"QDateTimeEdit::up-button:hover, QDateTimeEdit::down-button:hover\n"
"{\n"
"    background-color: #8399ff;\n"
"    border: 1px solid #8399ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:disabled, QSpinBox::down-button:disabled,\n"
"QDoubleSpinBox::up-button:disabled, QDoubleSpinBox::down-button:disabled,\n"
"QDateTimeEdit::up-button:disabled, QDateTimeEdit::down-button:disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed,\n"
"QDoubleSpinBox::up-button:pressed, QDoubleSpinBox::down-button::pressed,\n"
"QDateTimeEdit::up-button:pressed, QDateTimeEdit::down-button::pressed\n"
"{\n"
"    background-color: #4969ff;\n"
"    border: 1px solid #4969ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-arrow,\n"
"QDoubleSpinBox::down-arrow,\n"
"QDateTimeEdit::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-arrow,\n"
"QDoubleSpinBox::up-arrow,\n"
"QDateTimeEdit::up-arrow\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"    background-color: #525251;\n"
"    color: #ffffff;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    border-color: #051a39;\n"
"    padding: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    border-color: #051a39;\n"
"    padding: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTextEdit-----*/\n"
"QTextEdit\n"
"{\n"
"    background-color: #ffffff;\n"
"    color: #010201;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QTextEdit::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QGroupBox-----*/\n"
"QGroupBox\n"
"{\n"
"    border: 1px solid;\n"
"    border-color: #607cff;\n"
"    margin-top: 22px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title\n"
"{\n"
"    background-color: #607cff;\n"
"    color: #ffffff;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox::indicator\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(://checkbox.png);\n"
"    border: 1px solid #607cff;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 1px solid #607cff;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"    background-color: #656565;\n"
"    color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QRadioButton-----*/\n"
"QRadioButton::indicator::unchecked\n"
"{\n"
"    border: 2px inset gray;\n"
"    border-radius: 5px;\n"
"    background-color:  #fff;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked:hover\n"
"{\n"
"    border: 2px solid #607cff;\n"
"    border-radius: 5px;\n"
"    background-color:  #fff;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::checked\n"
"{\n"
"    border: 2px inset darkgray;\n"
"    border-radius: 5px;\n"
"    background-color: #4969ff;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::disabled\n"
"{\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:disabled\n"
"{\n"
"    background-color: #656565;\n"
"    color: #656565;\n"
"    border: 2px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTableView & QTableWidget-----*/\n"
"QTableView\n"
"{\n"
"    background-color: #242526;\n"
"    border: 1px solid #32414B;\n"
"    color: #f0f0f0;\n"
"    gridline-color: #8faaff;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::disabled\n"
"{\n"
"    background-color: #242526;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:hover\n"
"{\n"
"    background-color: #26264f;\n"
"    color: #f0f0f0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected\n"
"{\n"
"    background-color: #1a1b1c;\n"
"    border: 2px solid #4969ff;\n"
"    color: #F0F0F0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected:disabled\n"
"{\n"
"    background-color: #1a1b1c;\n"
"    border: 2px solid #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: #505050;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #525251;\n"
"    color: #fff;\n"
"    text-align: left;\n"
"    padding: 4px;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    color: #fff;\n"
"    background-color: #4969ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked:disabled\n"
"{\n"
"    color: #656565;\n"
"    background-color: #525251;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTabWidget-----*/\n"
"QTabBar::tab\n"
"{\n"
"    background-color: #262626;\n"
"    color: #ffffff;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-color: #051a39;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:disabled\n"
"{\n"
"    background-color: #656565;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane\n"
"{\n"
"    background-color: #262626;\n"
"    color: #ffffff;\n"
"    border: 1px solid;\n"
"    border-color: #607cff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    background-color: #607cff;\n"
"    color: #ffffff;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-color: #051a39;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected:disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    background-color: #262626;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    background-color: #8399ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
"    margin-top: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:bottom:!selected\n"
"{\n"
"    margin-bottom: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom\n"
"{\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top:selected\n"
"{\n"
"    border-bottom-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:bottom:selected\n"
"{\n"
"    border-top-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one\n"
"{\n"
"    margin-right: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left:!selected\n"
"{\n"
"    margin-right: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    margin-left: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right\n"
"{\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left:selected\n"
"{\n"
"    border-left-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:right:selected\n"
"{\n"
"    border-right-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one\n"
"{\n"
"    margin-bottom: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSlider-----*/\n"
"QSlider::groove:horizontal\n"
"{\n"
"    background-color: transparent;\n"
"    height: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal\n"
"{\n"
"    background-color: #607cff;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal\n"
"{\n"
"    background-color: #666765;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal\n"
"{\n"
"    background-color: #607cff;\n"
"    width: 14px;\n"
"    margin-top: -6px;\n"
"    margin-bottom: -6px;\n"
"    border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover\n"
"{\n"
"    background-color: #607cff;\n"
"    border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal:disabled\n"
"{\n"
"    background-color: #bbb;\n"
"    border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal:disabled\n"
"{\n"
"    background-color: #eee;\n"
"    border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:disabled\n"
"{\n"
"    background-color: #eee;\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::groove:vertical\n"
"{\n"
"    background-color: transparent;\n"
"    width: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:vertical\n"
"{\n"
"    background-color: #607cff;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:vertical\n"
"{\n"
"    background-color: #666765;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:vertical\n"
"{\n"
"    background-color: #607cff;\n"
"    height: 14px;\n"
"    margin-left: -6px;\n"
"    margin-right: -6px;\n"
"    border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:vertical:hover\n"
"{\n"
"    background-color: #607cff;\n"
"    border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:vertical:disabled\n"
"{\n"
"    background-color: #bbb;\n"
"    border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:vertical:disabled\n"
"{\n"
"    background-color: #eee;\n"
"    border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:vertical:disabled\n"
"{\n"
"    background-color: #eee;\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QDial-----*/\n"
"QDial\n"
"{\n"
"    background-color: #607cff;\n"
"\n"
"}\n"
"\n"
"\n"
"QDial::disabled\n"
"{\n"
"    background-color: #404040;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: 1px solid #222222;\n"
"    background-color: #3d3d3d;\n"
"    height: 13px;\n"
"    margin: 0px 16px 0 16px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background: #607cff;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #607cff;\n"
"    width: 14px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #607cff;\n"
"    width: 14px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-right.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-left.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #3d3d3d;\n"
"    width: 13px;\n"
"    margin: 16px 0 16px 0;\n"
"    border: 1px solid #222222;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #607cff;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #607cff;\n"
"    height: 14px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #607cff;\n"
"    height: 14px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QProgressBar-----*/\n"
"QProgressBar\n"
"{\n"
"    background-color: #383838;\n"
"    color: #ffffff;\n"
"    border: 1px solid #607cff;\n"
"    border-radius: 3px;\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #607cff;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk:disabled {\n"
"    background-color: #656565;\n"
"    border: 1px solid #aaa;\n"
"    color: #656565;\n"
"}\n"
"\n"
"\n"
"/*-----QStatusBar-----*/\n"
"QStatusBar\n"
"{\n"
"    background-color: #0a0a0a;\n"
"    color: #ffffff;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.in_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.in_label.setObjectName("in_label")
        self.gridLayout.addWidget(self.in_label, 1, 0, 1, 1)
        self.outside_f = QtWidgets.QLabel(parent=self.centralwidget)
        self.outside_f.setStyleSheet("QLabel { font-size: 30pt; font-weight: bold}")
        self.outside_f.setObjectName("outside_f")
        self.gridLayout.addWidget(self.outside_f, 0, 1, 1, 1)
        self.inside_f = QtWidgets.QLabel(parent=self.centralwidget)
        self.inside_f.setStyleSheet("QLabel { font-size: 30pt; font-weight: bold}")
        self.inside_f.setObjectName("inside_f")
        self.gridLayout.addWidget(self.inside_f, 1, 1, 1, 1)
        self.out_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.out_label.setObjectName("out_label")
        self.gridLayout.addWidget(self.out_label, 0, 0, 1, 1)
        self.outside_humidity = QtWidgets.QLabel(parent=self.centralwidget)
        self.outside_humidity.setStyleSheet("QLabel { font-size: 30pt; font-weight: bold}")
        self.outside_humidity.setObjectName("outside_humidity")
        self.gridLayout.addWidget(self.outside_humidity, 0, 2, 1, 1)
        self.inside_humidify = QtWidgets.QLabel(parent=self.centralwidget)
        self.inside_humidify.setStyleSheet("QLabel { font-size: 30pt; font-weight: bold}")
        self.inside_humidify.setObjectName("inside_humidify")
        self.gridLayout.addWidget(self.inside_humidify, 1, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.wind_speed = QtWidgets.QLabel(parent=self.centralwidget)
        self.wind_speed.setObjectName("wind_speed")
        self.gridLayout_2.addWidget(self.wind_speed, 2, 1, 1, 1)
        self.wind_gust = QtWidgets.QLabel(parent=self.centralwidget)
        self.wind_gust.setObjectName("wind_gust")
        self.gridLayout_2.addWidget(self.wind_gust, 3, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 3, 1, 2)
        #self.wind_direction = QtWidgets.QLabel(parent=self.centralwidget)
        self.wind_direction = WindDirection(parent=self.centralwidget)
        self.wind_direction.setMouseTracking(False)
        #self.wind_direction.setStyleSheet("QLabel { font-size: 72pt}")
        self.wind_direction.setObjectName("wind_direction")
        self.gridLayout_3.addWidget(self.wind_direction, 0, 1, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.rel_pressure = QtWidgets.QLabel(parent=self.centralwidget)
        self.rel_pressure.setStyleSheet("QLabel { font-size: 48pt}")
        self.rel_pressure.setObjectName("rel_pressure")
        self.verticalLayout.addWidget(self.rel_pressure)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.rainfall = QtWidgets.QLabel(parent=self.centralwidget)
        self.rainfall.setStyleSheet("QLabel { font-size: 48pt}")
        self.rainfall.setObjectName("rainfall")
        self.verticalLayout.addWidget(self.rainfall)
        self.cur_datetime = QtWidgets.QLabel(parent=self.centralwidget)
        self.cur_datetime.setObjectName("cur_datetime")
        self.verticalLayout.addWidget(self.cur_datetime)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.sat_image = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.sat_image.sizePolicy().hasHeightForWidth())
        self.sat_image.setSizePolicy(sizePolicy)
        self.sat_image.setMinimumSize(QtCore.QSize(300, 300))
        self.sat_image.setMaximumSize(QtCore.QSize(300, 300))
        self.sat_image.setTabletTracking(False)
        self.sat_image.setObjectName("sat_image")
        self.gridLayout_3.addWidget(self.sat_image, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.in_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">In</span></p></body></html>"))
        self.outside_f.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">OutF</span></p></body></html>"))
        self.inside_f.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">InF</span></p><p><br/></p></body></html>"))
        self.out_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">Out</span></p></body></html>"))
        self.outside_humidity.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">OutF</span></p></body></html>"))
        self.inside_humidify.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">InF</span></p><p><br/></p></body></html>"))
        self.wind_speed.setText(_translate("MainWindow", "wind speed"))
        self.wind_gust.setText(_translate("MainWindow", "wind gust"))
        #self.wind_direction.setText(_translate("MainWindow", "<html><head/><body><p>999</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Barometer</span></p></body></html>"))
        self.rel_pressure.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt;\">29.99</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">RainFall</span></p></body></html>"))
        self.rainfall.setText(_translate("MainWindow", "<html><head/><body><p>99.99</p></body></html>"))
        self.cur_datetime.setText(_translate("MainWindow", "Sun Jan 01 00:00:00 2024"))
        self.sat_image.setText(_translate("MainWindow", "sat_image"))