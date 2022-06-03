import sys
import os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
import AVL



class FindYourWord(QDialog):
    def __init__(self):
        super(FindYourWord,self).__init__()
        loadUi("Home.ui",self)
        self.Select.clicked.connect(self.pathcheck)
        self.Exit.clicked.connect(self.exit)
    
    def pathcheck(self):
        global path
        path=self.Pathentry.text()
        if os.path.isfile(path):
            self.Disp()
        else:
            self.Error.setText("(*) Enter existing path.")

    def Disp(self):
        display=Display()
        widget.addWidget(display)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def exit(self):
        exit(0)

class Display(QDialog):
    def __init__(self):
        super(Display,self).__init__()
        loadUi("Display.ui",self)
        file = open(path,"r")
        global read
        read=file.read()
        global ls
        ls=read.split()
        self.Content.setText(read)
        self.SearchBut.clicked.connect(self.getkey)
        self.Exit.clicked.connect(self.exit)
    
    def treeing(self):
        global root
        root=None
        current=0
        for i in range(len(ls)):
            while(read[current]== " "):
                current+=1
            ls[i]=ls[i].lower()
            root=AVL.insert2(root,ls[i],len(ls[i]),current)
            current+=len(ls[i])
        
    def getkey(self):
        global ser_key
        global root
        ser_key=self.SearchKey.text()
        ser_key=ser_key.lower()
        if len(ser_key)!=0:
            self.treeing()
            root2=AVL.search(root,len(ser_key))
            if(AVL.search(root2.tree,ser_key)):
                self.goto_res()
            else:
                self.Error.setText("Key not found")
        else:
            self.Error.setText("(*) Enter Key.")
    
    def goto_res(self):
        res=Result()
        widget.addWidget(res)
        widget.setCurrentIndex(widget.currentIndex()+1)

    
    def exit(self):
        exit(0)

class Result(QDialog):
    def __init__(self):
        super(Result,self).__init__()
        loadUi("Result.ui",self)
        global pos
        pos=self.getpos()
        str_pos=str(pos)
        self.Positions.setText(str_pos)
        str_html=self.makehtml()
        self.Content.setHtml(str_html)
        self.Back.clicked.connect(FindYourWord.Disp)
        self.Exit.clicked.connect(self.exit)
        self.TreeViewBut.clicked.connect(self.goto_Tree)
    
    def goto_Tree(self):
        tree=TreeView()
        widget.addWidget(tree)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def getpos(self):
        root2=AVL.search(root,len(ser_key))
        position=AVL.search(root2.tree,ser_key)
        return position.pos
    
    def makehtml(self):
        str=''
        j=0
        length=len(ser_key)
        start=-99999
        for i in range(len(read)):
            if i in pos:
                start=i
                str+='<u><b>'
            if (i-start)==len(ser_key):
                str+='</u></b>'
            str+=read[i]
            i+=1
        return str


    def exit(self):
        exit(0)

class TreeView(QDialog):
    def __init__(self):
        super(TreeView,self).__init__()
        loadUi("Treeview.ui",self)
        treetxt=self.getTree()
        self.TreeContent.setHtml(treetxt)
        self.Back.clicked.connect(Display.goto_res)
        self.Exit.clicked.connect(self.exit)
    
    def getTree(self):
        AVL.preOrder(root)
        return AVL.preorder_str
    def exit(self):
        exit(0)


app=QApplication(sys.argv)
Home=FindYourWord()
widget=QtWidgets.QStackedWidget()
widget.addWidget(Home)
widget.setFixedHeight(400)
widget.setFixedWidth(400)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")