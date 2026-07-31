# ch 5.2.1 main.py
import sys
from ui import View # ui.py의 view 클래스 추가
from ctrl import Control # ctrl.py의 Control 클래스 추가
from PyQt5.QtWidgets import QApplication

def main():
        calc = QApplication(sys.argv)
        view = View()
        con = Control(view=view)
        view.show()
        view.raise_()  # 창을 맨 앞으로 강제로 가져옴
        view.activateWindow()
        sys.exit(calc.exec_())
            
if __name__=='__main__':
    main()