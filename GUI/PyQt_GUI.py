# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PyQt5.QtWidgets import *
import sys
import winsound #삑소리 내는데 사용되는 모듈

class BeepSound(QMainWindow): #삑소리를 내주는 클래스로 'BeepSound'라 칭함, QMainWindow(윈도우를 생성,관리하는 함수를 제공하는 클래스)클래스 상속
    def __init__(self): #BeepSound 클래스를 객체로 생성시 자동으로 실행되는 생성자 함수 __init__정의
        super().__init__()
        self.setWindowTitle('삑소리내기') #윈도우 제목 표시줄에 '삑소리내기'라고 표시
        self.setGeometry(200,200,500,100)#윈도우를 화면의 (200,200)위치에 초기 배치, 너비 500, 높이 100으로 설정
        
        shortBeepButton=QPushButton('짧게삑',self) # '짧게 삑'이라고 표시된 버튼을 만들어 shortBeepButton객체에 저장
        longBeepButton=QPushButton('길게삑',self) #'길게 삑'이라고 표시된 버튼을 만들어 longBeepButton객체에 저장
        quitButton=QPushButton('나가기',self) #'나가기'이라고 표시된 버튼을 만들어 quitButton객체에 저장
        self.label=QLabel('환영합니다',self) #'환영합니다'라고 쓴 레이블을 만들어 label객체에 저장(self-멤버변수)
        #위젯 위치와 크기 지정
        shortBeepButton.setGeometry(10,10,100,30) #shortBeepButton을 윈도우의 (10,10)위치에 배치, 너비100, 높이30으로 지정 
        longBeepButton.setGeometry(110,10,100,30) #longBeepButton를 윈도우의(110,10)위치에 배치, 너비100, 높이30으로 지정
        quitButton.setGeometry(210,10,100,30) #quitButton를 윈도우의(210,10)위치에 배치, 너비100, 높이30으로 지정
        self.label.setGeometry(10,40,500,70) #label를 윈도우의(10,40)위치에 배치, 너비500, 높이70으로 지정
        
        shortBeepButton.clicked.connect(self.shortBeepFunction) # shortBeepButton클릭시 shortBeepFunction함수 실행
        longBeepButton.clicked.connect(self.longBeepFunction) #longBeepButton클릭시 longBeepFunction함수 실행
        quitButton.clicked.connect(self.quitFunction) #quitButton클릭시 quitFunction함수 실행
        
    def shortBeepFunction(self):
        self.label.setText('주파수1000으로 0.5초동안 삑소리를 냅니다') #shortBeepFunction은 label.setText명령어를 이용하여 레이블 위젯에 텍스르 쓴다
        winsound.Beep(1000,500) #주파수 1000인 삑소리를 500밀리초(0.5초)동안 들려준다
        
    def longBeepFunction(self):
        self.label.setText('주파수 1000으로 3초동안 삑소리를 냅니다') #longBeepFunction은 label.setText명령어를 이용하여 레이블 위젯에 텍스트를 쓴다
        winsound.Beep(1000,3000) #주파수 1000인 삑소리를 3000밀리초(3초)동안 들려준다.
        
    def quitFunction(self):
        self.close() #quitButton<나가기>를누르면 quitFunction함수가 호출되며 close함수실행되며 프로그램 종료 
        
app=QApplication(sys.argv) #PyQt실행에 필요한 객체 app을 생성
win=BeepSound() #BeepSound 클래스의 객체 win을 생성(이때 BeepSound클래스의 생성자함수 __init__이 자동실행-'삑소리내기'제목의 윈도우 생성,위젯4개 만들어지며, 콜백함수 등록됨)
win.show() #win에 해당하는 윈도우를 실제로 화면에 나타냄
app.exec_() #무한루프를 돌아 프로그램이 끝나는 것 방지