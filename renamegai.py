import tkinter
import tkinter.filedialog
import tkinter.messagebox
import os,re
from PIL import Image,ImageTk
import ctypes
global photo


class window:
    def __init__(self):

        self.root=root=tkinter.Tk()  #tkinter的第一行
        self.root.title('图片重命名')  #窗口的标题
        self.root.resizable(False, False)  # 固定窗口大小

        # 告诉操作系统使用程序自身的dpi适配
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        # 获取屏幕的缩放因子
        ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
        # 设置程序缩放
        self.root.tk.call('tk', 'scaling', ScaleFactor / 75)

        img = Image.open('image/back233.gif')
        photo = ImageTk.PhotoImage(img)
        label=tkinter.Label(root,image=photo)
        label.place(x=0, y=0)  # 选择文件位置
        label=tkinter.Label(root,text='选择文件:',font=('微软雅黑',12),bg="#9AB8EE")#选择文件标签
        label.place(x=20,y=60)#选择文件位置
        label=tkinter.Label(root,text='示例: 输入image(1) 文件命名为:image1、image2...',font=('微软雅黑',10),bg="#9AB8EE")#注意的标签
        label.place(x=20,y=165)#注意的位置
        label=tkinter.Label(root,text='注意:括号为英文',font=('微软雅黑',10),bg="#9AB8EE")#注意的标签
        label.place(x=20,y=190)#注意的位置



        self.theLB = tkinter.Listbox(root,selectmode='entended',width=50,bg='CornflowerBlue')#建立列表和滚动条
        self.theLB.pack(side='left',fill='both')#显示列表
        self.theLB.place(x=70,y=250)#列表的位置# 垂直滚动条组件

 
        self.buttonview1 = tkinter.Button(root, text='预览', font=('微软雅黑', 15),relief='flat',fg='white',bg='CornflowerBlue',  # 预览按钮
                                             command=self.view)  # 浏览按钮的点击事件
        self.buttonview1.place(x=560, y=340)  # 浏览按钮的位置


        menu=tkinter.Menu(self.root)  #在root创建主目录
        helpmenu= tkinter.Menu(menu, tearoff=False)  #创建子目录tearoff=0菜单不可独立
        menu.add_cascade(label='帮助', menu=helpmenu)  #设置菜单名称label='帮助'，在主目录中添加子目录
        #添加子目录菜单内加名称，以及指令
        helpmenu.add_radiobutton(label='使用说明', command=self.introduct, font=('黑体', 10))#加使用说明和点击事件
        self.root.config(menu=menu)  # 在root中放置主目录

        self.status=tkinter.StringVar()#使用界面编程的时候，有些时候是需要跟踪变量的值的变化，以保证值的变更随时可以显示在界面上
        #self.entry1=tkinter.Entry(root)可以用get()方法，但是self.entry1=tkinter.Entry(root).place(x=150, y=80)不能get()方法
        self.entry1=tkinter.Entry(root,width=45,relief='flat')#添加图片文本框
        self.entry1.place(x=130,y=65)#文本框位置
        self.entry3 = tkinter.Entry(root, width=45, relief='flat',bg='LightSteelBlue')#输入格式文本框
        self.entry3.place(x=130, y=125)#输入格式文本框位置
        self.entry3.insert(0,"()" )
        #命名格式

        label = tkinter.Label(root, text='命名格式：', font=('微软雅黑', 12), bg="#9AB8EE")
        # 文件格式的标签
        label.place(x=20, y=120)
        # 文件格式的位置
        self.buttonbrowser1=tkinter.Button(root,text='浏览',font=('微软雅黑',10),relief='flat',fg='white',bg='CornflowerBlue',    #浏览按钮
                                                                                  command=self.browser)#浏览按钮的点击事件
        self.buttonbrowser1.place(x=560,y=53)#浏览按钮的位置
 
        self.buttonconv=tkinter.Button(root,text='开始',font=('微软雅黑',10),relief='flat',fg='white',bg='CornflowerBlue',#开始按钮
                                        command=self.conv)#开始按钮的点击事件
        self.buttonconv.place(x=560,y=115)#开始按钮的位置
        self.labelstatus = tkinter.Label(root,fg='red',font=('微软雅黑',12), textvariable=self.status,bg="#9AB8EE")  #完成的可变标签
        self.labelstatus.place(x=550, y=190)#完成的标签的位置
 
        self.buttonclear1 = tkinter.Button(root, text='清空', font=('微软雅黑', 15), relief='flat', fg='white',
                                          bg='CornflowerBlue',  # 浏览按钮
                                          command=self.clearall)  # 浏览按钮的点击事件
        self.buttonclear1.place(x=560, y=260)  # 浏览按钮的位置
        self.root.minsize(700, 535)
        self.root.maxsize(700, 535)
        self.root.mainloop()  # mainloop进入到事件（消息）循环 一旦检测到事件，就刷新组件

 
 
    def clearall(self):
         directory = ' '
         savepath = ' '
         self.theLB.delete(0,tkinter.END)
         self.entry1.delete(0, tkinter.END)
         self.entry3.delete(0, tkinter.END)
 
    def introduct(self):#说明显示窗口的函数
         #messagebox弹窗
         tkinter.messagebox.showerror('帮助', '''
        在格式中输入前缀+(标号)
        若格式无输入，则自动标号为1，2，3...
        重命名后请先点击清空按钮

        注意：(1)格式中不能带有‘/’；（2）变量括号为英文括号 ；(3) 命名前先备份好文件
        ''')





    def browser(self):
        '''选择文件浏览框'''
        directory=tkinter.filedialog.askopenfilenames(title='浏览', filetypes=[('JPG', '*.jpg'), ('JPGE', '*.jpge'), ('PNG', '*.png')])#以选择文件对话框的格式选择打开什么文件，返回文件名

        with open('filenames.txt','w') as f:#Python的with语句自动调用try finally结构和close()方法 在filenames.txt存入文件名
            for i in directory:#遍历添加的文件名
                f.write(i)     #写入txt文件中
                f.write('\n')   #写入结束标志\n
                self.theLB.insert(tkinter.END,i)

        if directory:       #判断是否选择
            self.entry1.delete(0,tkinter.END)#先清空浏览文本行的内容
            self.entry1.insert(tkinter.END,set(directory))#在浏览文本行中添加浏览的图片的内容

    def view(self):
        viewimg0=self.theLB.get("active")
        photo = Image.open(viewimg0)
        photo.show()





    def savepath(self):
        '''保存路径浏览框'''

        savepath = tkinter.filedialog.askdirectory(title='浏览', filetypes=[('JPG', '*.jpg'), ('JPGE', '*.jpge'), ('PNG', '*.png')])#以选择文件对话框的格式选择打开什么文件，返回

        if savepath:
            self.entry2.delete(0,tkinter.END)
            self.entry2.insert(tkinter.END,savepath)
    def read_filenames(self):#读取储存的文件名
        with open('filenames.txt','r') as f:#还是那个Python自带简化段落
            for i in f.readlines():#在文件里读取行
                yield i.replace('\n', '')#yield字符 这个循环第一次跳过replace执行，第二次从replace执行再循环
    def renameall(self,examplename):#重命名模块
        i=0
        for c in self.read_filenames():#调用函数生成的
            filenametype =c.split('/')[-1]  #把前面的路径都切掉只保留文件名
            filep = c.replace(filenametype, '')  #这行没看懂
            filetype = filenametype.split('.')[-1]  #切掉文件后缀
            if examplename == '':#如果没有输入重命名的格式
                newname0 = filep + str(i + 1) + "." + filetype  # 那么修改的新文件名是原名+序号（从1开始）+.后缀
                newname = newname0.strip()#把newname0这个字符串中的空格符号都去掉，防止文件名字符串前后有回车或者空格
                os.renames(c, newname)#将遍历的文件c重命名成新文件名
                self.theLB.insert(i + 1, newname)#列表先新增新的
                self.theLB.delete(i)#再删除旧的 这里要新增新的 因为第一行不能删除 bug了好久
            else:
                pat = re.compile("(?<=\()\S+(?=\))")  # (?<=exp)是以exp开头的字符串, 但不包含本身.\S 匹配任何非空白字符
                sn0=re.findall(pat, examplename)[0].replace('(', '').replace(')', '')
                if sn0!=' ':
                    sn = int(sn0)  # 返回带有()字符的列表

                    newname0 = filep + examplename.replace('%d' % sn, '%d' % (sn + i)) + "." + filetype
                    newname = newname0.strip().replace('(', '').replace(')', '')
                    os.rename(c, newname)
                    self.theLB.insert(i + 1, newname)
                    self.theLB.delete(i)
                else:  # 未匹配到数字

                    newname0 = filep + examplename + str(i + 1) + "." + filetype  # 在输入边加序号从1开始
                    newname = newname0.strip()
                    newname = newname.replace('(', '').replace(')', '')  # 把newname0这个字符串中的空格符号都去掉，把括号去掉
                    os.renames(c, newname)  # 重命名操作
                    self.theLB.insert(i + 1, newname)
                    self.theLB.delete(i)
            i+=1#编号+1



    def conv(self):
        filepaths= self.entry1.get()#获得浏览的文件地址
        examplename= self.entry3.get()  #获得输入的模板的字符
        if filepaths == '':#如果entry1为空
            tkinter.messagebox.showerror('Python tkinter', '请选择图片')#提示没选择图片
            return
        try:
            self.renameall(examplename)#执行重命名函数
        except Exception as e:#抛出异常
            print(e)
        self.status.set('命名成功')#可变标签设置为命名成功


#window=window()#显示窗口


