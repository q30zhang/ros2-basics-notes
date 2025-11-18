#!/usr/bin/env python3 
# coding=utf-8
#1.编译器声明和2.编码格式声明
#1:为了防止用户没有将python安装在默认的/usr/bin目录，系统会先从env(系统环境变量)里查找python的安装路径，再调用对应路径下的解析器完成操作，也可以指定python3
#2:Python.X 源码文件默认使用utf-8编码，可以正常解析中文，一般而言，都会声明为utf-8编码

import cv2 #引用OpenCV功能包
import numpy as np #引用数组功能包

#读取图片
img_origin = cv2.imread('1.ImageProcess.jpg')
img_height, img_width, img_channels = img_origin.shape #获取图片尺寸高度、宽度、通道数
cv2.imshow("windows_origin", img_origin) #窗口显示图片

#缩小图片尺寸，再次获取图片尺寸
img = cv2.resize(img_origin, (int(img_width/2),int(img_height/2)), interpolation=cv2.INTER_AREA)  
img_height, img_width, img_channels = img.shape 
cv2.imshow("windows", img) #显示图片缩小后的图片

Quit=0 #是否继续运行标志位
#提示停止方法
print ('Press key "Q" to stop.')

while Quit == 0:
    keycode = cv2.waitKey(10) & 0xFF  # 每10ms刷新一次图片，同时读取键盘输入
    if keycode == ord('Q'):  # 如果按下 "Q" 键
        Quit = 1
        break

    ###仿射变换相关处理###
       
    #创建数组，用于仿射变换
    Mat1 = np.array([
        [1.6, 0, -150], #x轴放大1.6倍，并平移-150
        [0, 1.6, -120]  #y轴放大1.6倍，并平移-120
        ], dtype=np.float32)
    img1 = cv2.warpAffine(img, Mat1, (img_width, img_height)) #仿射变换
    cv2.imshow("windows1", img1) #窗口显示图片
    cv2.imwrite('1.ImageProcess1.jpg', img1) #保存图片

    theta = 15 * np.pi / 180 #15度的弧度值
    #创建数组，用于仿射变换
    Mat2 = np.array([
        [1, np.tan(theta), 0], #图片绕上边框逆时针旋转 15 度
        [0, 1, 0]
        ], dtype=np.float32)
    img2 = cv2.warpAffine(img, Mat2, (img_width, img_height)) #仿射变换
    cv2.imshow("windows2", img2) #窗口显示图片
    cv2.imwrite('1.ImageProcess2.jpg', img2) #保存图片

    #创建数组，用于仿射变换
    Mat3 = np.array([
        [np.cos(theta), -np.sin(theta), 0], #绕左上角顺时针旋转15度
        [np.sin(theta), np.cos(theta), 0]
         ], dtype=np.float32)
    img3 = cv2.warpAffine(img, Mat3, (img_width, img_height)) #仿射变换
    cv2.imshow("windows3", img3) #窗口显示图片
    cv2.imwrite('1.ImageProcess3.jpg', img3) #保存图片

    ###仿射变换相关处理###


    ###在图片上画画###

    #画直线 cv2.line(图片, 起点坐标, 终点坐标, BGR, 线条粗细)
    cv2.line(img, (300, 150), (500,150), (255, 255, 0), 2)

    #画圆cv2.circle(图片, 原点坐标, 半径, BGR, 线条粗细)
    cv2.circle(img, (400, 100), 75, (0, 0, 255), 5)

    #画矩形 cv2.rectangle(图片, 矩形左上角坐标, 矩形右下角, BGR, 线条粗细)
    cv2.rectangle(img, (620, 100), (700, 220), (255, 0, 0), 3)

    #创建多边形顶点坐标数组(可以有多个多边形)
    triangles = np.array([
    [(200, 100), (145, 203), (255, 203)],
    [(60, 140), (20, 197), (100, 197)]
     ])
    #画填充多边形 cv2.fillPoly(图片, 多边形顶点坐标数组, BGR)
    cv2.fillPoly(img, triangles, (0, 255, 0))

    #显示文字 cv2.putText(图片，文字，文字左下角坐标，字体显示格式，字体大小，BGR，线条粗细)
    cv2.putText(img, 'WHEELTEC', (1, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("windows_draw", img) #显示画画后的图片

    ###在图片上画画###


    #while循环里循环读取图片
    img_origin = cv2.imread('1.ImageProcess.jpg')
    img_height, img_width, img_channels = img_origin.shape #获取图片尺寸高度、宽度、通道数

    #缩小图片尺寸，再次获取图片尺寸
    img = cv2.resize(img_origin, (int(img_width/2),int(img_height/2)), interpolation=cv2.INTER_AREA)  
    img_height, img_width, img_channels = img.shape 

print ('Quitted!') #提示程序已停止
cv2.destroyAllWindows() #程序停止前关闭所有窗口
