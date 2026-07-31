# ch 5.2.1 ctrl.py
class Control:
    
    def __init__(self, view):
        self.view = view
        self.connectSignals()
        
    def calculate(self):
        pass    
        
    def connectSignals(self):
        self.view.btn1.clicked.connect(self.view.setDisplay)
        self.view.btn2.clicked.connect(self.view.clearMessage)
    
    def setDisplay(self):
        self.te1.appendPlainText("Button clicked!")
        
    def clear(self):
        self.view.clearMessage()
