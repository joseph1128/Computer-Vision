# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:40:35 2025

@author: 123
"""

from PyQt5.QtWidgets import *
import sys
import cv2 as cv

class Video(QMainWindow): #GUI 제작 지원하는 Video 클래스 선언
    def __init__(self):   #Video 클래스의 생성자 함수 __init__
        super().__init__()
        self.setWindowTitle('비디오에서 프레임수집') #윈도우 이름과 위치 지정
        self.setGeometry(200,200,500,100)
        
        videoButton=QPushButton('비디오켜기',self) #버튼 셍성
        captureButton=QPushButton('프레임잡기',self)
        saveButton=QPushButton('프레임저장',self)
        quitButton=QPushButton('나가기',self)
        
        videoButton.setGeometry(10,10,100,30) #버튼의 위치와 크기 지정
        captureButton.setGeometry(110,10,100,30)
        saveButton.setGeometry(210,10,100,30)
        quitButton.setGeometry(310,10,100,30)
        #버튼을 클릭했을 때 수행할 콜백함수 지정
        videoButton.clicked.connect(self.videoFunction) #videoFunction을 <비디오 켜기>라는 videoButton의 콜백함수로 등록 
        captureButton.clicked.connect(self.captureFunction) #CaptureFunction을 <프레임잡기>라는 captureButton의 콜백함수로 등록
        saveButton.clicked.connect(self.saveFunction) #saveFunction을 <프레임저장>이라는 saveButton의 콜백함수로 등록
        quitButton.clicked.connect(self.quitFunction) #quitFunction을 <나가기>라는 quitButton의 콜백함수로 등록
        
    def videoFunction(self): #OpenCV함수를 히용하여 웹캠에서 비디오를 입력받아 윈도우에 디스플레이 
        self.cap=cv.VideoCapture(0,cv.CAP_DSHOW) #DirectShow를 사용하여 Windows환경에서 웹캠을 이용하여 비디오 캡처
        if not self.cap.isOpened():self.close() #연결이 안되었을 때 오류메세지 출력 후 프로그램 종료 
        
        while True:    #연결 성공시 
            ret,self.frame=self.cap.read() #웹캠에서 프레임 획득하여 frame변수에 저장,self사용-멤버변수로 선언(다른 함수와의 공유위해)
            if not ret:break
            cv.imshow('video_display',self.frame) #'video_display'라는 윈도우에 표시
            cv.waitKey(1)
            
    def captureFunction(self): 
        self.capturedFrame=self.frame # 비디오 프레임을 저장한 frame을 captureFrame변수에 저장
        cv.imshow('Captured_frame',self.capturedFrame)#'Captured)frame'이라는 윈도우에 디스플레이
        
    def saveFunction(self):# saveFunction은 PyQt가 제공하는 QFileDialog.getSaveFileName함수를 사용하여
        fname=QFileDialog.getSaveFileName(self,'파일저장','./') #사용자가 파일을 저장할 곳을 브라우징하고 파일이름을 지정할 수 있게 함 '파일 저장'-브라우징 윈도우의 제목 지정,'./'-현재 폴더에서 브라우징, 파일 이름을 'fname'으로 저장
        cv.imwrite(fname[0],self.capturedFrame) #사용자가 선택한 파일 경로에 캡처된 이미지 저장
        
    def quitFunction(self):
        self.cap.release() #비디오 연결을 끊고 
        cv.destroyAllWindows() #OpenCV가 연 모든 윈도우를 닫고
        self.close() #프로그램 종료
        
app=QApplication(sys.argv) #PyQt실행에 필요한 객체 app을 생성
win=Video()#Video 클래스의 객체 win을 생성(이때 Video클래스의 생성자함수 __init__이 자동실행-'비디오에서 프레임 수집'제목의 윈도우 생성,위젯4개 만들어지며, 콜백함수 등록됨)
win.show()  #win에 해당하는 윈도우를 실제로 화면에 나타냄
app.exec_() #무한루프를 돌아 프로그램이 끝나는 것 방지
        