# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WaterMark.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os
import os.path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QFontDialog, QMainWindow
from PyQt5.QtGui import QFontMetrics, QFontInfo
from PyQt5.QtGui import QBrush,QPixmap
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()

        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(626, 615)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/friendly icons.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: rgb(242, 247, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 270, 551, 271))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 51, 16))
        self.label_3.setObjectName("label_3")
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(70, 120, 161, 22))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.horizontalSlider.setFont(font)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(260, 100, 281, 61))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 31, 20))
        self.label_4.setObjectName("label_4")
        self.x = QtWidgets.QLineEdit(self.groupBox_4)
        self.x.setGeometry(QtCore.QRect(60, 20, 71, 21))
        self.x.setStyleSheet("background-color: rgb(148, 182, 255);")
        self.x.setObjectName("x")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(150, 20, 31, 16))
        self.label_5.setObjectName("label_5")
        self.y = QtWidgets.QLineEdit(self.groupBox_4)
        self.y.setGeometry(QtCore.QRect(180, 20, 81, 21))
        self.y.setStyleSheet("background-color: rgb(148, 182, 255);")
        self.y.setObjectName("y")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 180, 511, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.t2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.t2.setGeometry(QtCore.QRect(20, 30, 371, 31))
        self.t2.setStyleSheet("background-color: rgb(148, 182, 255);")
        self.t2.setObjectName("t2")
        self.b2 = QtWidgets.QPushButton(self.groupBox_3)
        self.b2.setGeometry(QtCore.QRect(420, 30, 71, 28))
        self.b2.setStyleSheet("background-color: rgb(100, 149, 237);\n"
"color: rgb(246, 243, 255);")
        self.b2.setObjectName("b2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 40, 72, 15))
        self.label.setObjectName("label")
        self.t1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.t1.setGeometry(QtCore.QRect(80, 40, 141, 21))
        self.t1.setStyleSheet("background-color: rgb(148, 182, 255);")
        self.t1.setText("")
        self.t1.setObjectName("t1")
        self.b1 = QtWidgets.QPushButton(self.groupBox_2)
        self.b1.setGeometry(QtCore.QRect(250, 40, 71, 31))
        self.b1.setStyleSheet("background-color: rgb(100, 149, 237);\n"
"color: rgb(246, 243, 255);")
        self.b1.setObjectName("b1")
        self.bc = QtWidgets.QPushButton(self.centralwidget)
        self.bc.setGeometry(QtCore.QRect(500, 560, 81, 31))
        self.bc.setStyleSheet("background-color: rgb(100, 149, 237);\n"
"color: rgb(246, 243, 255);")
        self.bc.setObjectName("bc")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(40, 20, 551, 231))
        self.groupBox_5.setObjectName("groupBox_5")
        self.b = QtWidgets.QPushButton(self.groupBox_5)
        self.b.setGeometry(QtCore.QRect(432, 40, 101, 41))
        self.b.setStyleSheet("background-color: rgb(100, 149, 237);\n"
"color: rgb(246, 243, 255);")
        self.b.setObjectName("b")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_5)
        self.listWidget.setGeometry(QtCore.QRect(30, 31, 381, 181))
        self.listWidget.setStyleSheet("background-color: rgb(148, 182, 255);")
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage('准备就绪…… ')  # 设置状态栏默认值
        MainWindow.setStatusBar(self.statusbar)

        palette = QtGui.QPalette()
        # 设置窗体背景自适应
        palette.setBrush(MainWindow.backgroundRole(), QBrush(
            QPixmap("image/Markback.png").scaled(MainWindow.size(), QtCore.Qt.IgnoreAspectRatio,
                                             QtCore.Qt.SmoothTransformation)))
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(True)  # 设置自动填充背景

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "添加水印"))
        self.groupBox_2.setTitle(_translate("MainWindow", "水印设置"))
        self.label_3.setText(_translate("MainWindow", "透明度"))
        self.groupBox_4.setTitle(_translate("MainWindow", "水印位置"))
        self.label_4.setText(_translate("MainWindow", "x轴"))
        self.label_5.setText(_translate("MainWindow", "y轴"))
        self.groupBox_3.setTitle(_translate("MainWindow", "存储位置"))
        self.b2.setText(_translate("MainWindow", "浏览"))
        self.label.setText(_translate("MainWindow", "水印内容"))
        self.b1.setText(_translate("MainWindow", "字体设置"))
        self.bc.setText(_translate("MainWindow", "保存"))
        self.groupBox_5.setTitle(_translate("MainWindow", "添加图片"))
        self.b.setText(_translate("MainWindow", "添加图片"))

        # 关联添加图片
        self.b.clicked.connect(self.getFiles)
        # 关联字体设置
        self.b1.clicked.connect(self.setFont)
        # 关联存储位置浏览
        self.b2.clicked.connect(self.msg)
        # 关联保存水印图片
        self.bc.clicked.connect(self.addMark)
        # 关联列表图片预览
        self.listWidget.itemClicked.connect(self.itemClick)

    # 判断是否为图片
    def isImg(self, file):
        file = file.lower()
        if file == '.jpg':
            return True
        elif file == '.png':
            return True
        elif file == '.jpeg':
            return True
        elif file == '.bmp':
            return True
        else:
            return False

        # 获取图片路径
    def getFiles(self):
        try:
            # 选择图片文件夹路径
            self.img_path = QFileDialog.getExistingDirectory(None, "选择图片文件夹路径", os.getcwd())
            self.list = os.listdir(self.img_path)  # 遍历选择的文件夹
            num = 0  # 记录图片数量
            self.listWidget.clear()  # 清空列表项
            for i in range(0, len(self.list)):
                    # 遍历图片列表
                filepath = os.path.join(self.img_path, self.list[i])  # 记录遍历到的文件名
                if os.path.isfile(filepath):  # 判断是否是文件
                    imgType = os.path.splitext(filepath)[1]  # 获取扩展名
                    if self.isImg(imgType):  # 判断是否为图片
                        num += 1  # 图片数量加1
                        self.item = QtWidgets.QListWidgetItem(self.listWidget)  # 创建列表项
                        self.item.setText(self.list[i])  # 显示图片列表
            self.statusbar.showMessage('共有图片' + str(num) + '张')  # 状态栏显示图片总数
        except Exception:
            QMessageBox.warning(None, '警告', '请选择一个有效路径...')

    # 预览图片
    def itemClick(self, item):
        os.startfile(self.img_path + '\\' + item.text())

    # 设置字体
    def setFont(self):
        self.waterfont, ok = QFontDialog.getFont()  # 显示字体对话框
        if ok:  # 判断是否选择了字体
            self.t1.setFont(self.waterfont)  # 设置水印文字的字体
            self.fontSize = QFontMetrics(self.waterfont)  # 获取字体尺寸
            self.fontInfo = QFontInfo(self.waterfont)  # 获取字体信息

    # 设置存储路径
    def msg(self):
        try:
            # dir_path即为选择的文件夹的绝对路径，第二个参数为对话框标题，第三个为对话框打开后默认的路径
            self.dir_path = QFileDialog.getExistingDirectory(None, "选择路径", os.getcwd())
            self.t2.setText(self.dir_path)  # 显示选择的的保存路径
        except Exception as e:
            print(e)

    # 添加文字水印
    def textMark(self, img, newImgPath):
        try:
            im = Image.open(img).convert('RGBA')  # 打开原始图片，并转换为RGBA
            newImg = Image.new('RGBA', im.size, (255, 255, 255, 0))  # 存储添加水印后的图片
            fonttype = 'Font\\' + self.fontInfo.family() + '.ttf'  # 'simkai.ttf'
            font = ImageFont.truetype(fonttype, self.fontInfo.pointSize(), encoding="utf-8")
            #print("通过")
            imagedraw = ImageDraw.Draw(newImg)  # 创建绘制对象
                #       imagewidth,imageheight = im.size    #记载图片大小
                #      txtwidth = self.fontSize.maxWidth()*len(self.t1.text())     #获取字体宽度
                #     txtheight = self.fontSize.height()  #获取字体高度

                # 设置水印文字位置
            X = eval(self.x.text())
            Y = eval(self.y.text())
            position = (X, Y)

            imagedraw.text(xy=position, text=self.t1.text(), font=font, fill=(255, 255, 255, 60))

            # 设置透明度
            alpha = newImg.split()[3]
            alpha = ImageEnhance.Brightness(alpha).enhance(int(self.horizontalSlider.value()) / 10.0)
            newImg.putalpha(alpha)
            # 保存图片
            out = Image.alpha_composite(im, newImg)
            out = out.convert('RGB')
            out.save(newImgPath)


        except Exception as e1:
            print(e1)
            QMessageBox.warning(None, '错误', '图片格式有误，请重新选择...', QMessageBox.Ok)

    # 添加水印
    def addMark(self):
        if self.t2.text() == '':  # 判断是否选择了保存路径
            QMessageBox.warning(None, '警告', '请选择保存路径', QMessageBox.Ok)
            return
        else:
            num = 0  # 记录图片数量
            for i in range(0, self.listWidget.count()):  # 遍历图片列表
                   # 设置原图片路径（包括文件名）
                filepath = os.path.join(self.img_path, self.listWidget.item(i).text())
                    # 设置水印图片保存路径（包括文件名）
                newfilepath = os.path.join(self.t2.text(), self.listWidget.item(i).text())
                if self.t1.text() == '':  # 判断是否输入了水印文字
                    QMessageBox.warning(None, '警告', '请输入水印文字', QMessageBox.Ok)
                    return
                else:
                    self.textMark(filepath, newfilepath)  # 调用textMark方法添加文字水印
                    num += 1  # 处理图片数量加一
            self.statusbar.showMessage('任务完成，此次共处理 ' + str(num) + ' 张图片')  # 显示处理图片总数
