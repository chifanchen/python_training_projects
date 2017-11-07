#coding:utf-8
from tkinter import *

window = Tk()
window.title('投资收益计算器')
project_frame = Frame(window).grid()
newName=StringVar()
new_name = Entry(project_frame, textvariable= newName).grid(row=1,column=5)
name_label = Label(project_frame, text='项目名称').grid(row=0, column=0)
money_label = Label(project_frame, text='投资金额').grid(row=0, column=1)
rate_label = Label(project_frame, text='年化利率').grid(row=0, column=2)
return_label = Label(project_frame, text='日收益').grid(row=0, column=3)

#内含一个collection，将所有的投资项目收集起来，收集在一个字典中，按照id/invest对象相对应的方式
class invest_dic():
    def __init__(self):
        global newName
        self.newName=newName
        self.collection = {}
        self.id = 1
        print(len(self.collection.values()))
    def jisuan(self):
        for i in self.collection.values():
            i.jisuan()
        print(len(self.collection.values()))
    def createAddtoCol(self):
        if self.newName.get() not in [x.name for x in self.collection.values()]:
            self.collection[self.id] = invest(self.newName.get(),(self.id+1))
            print(len(self.collection.values()))
            self.id+=1
        else:
            pass
    def savetoData(self):
        f=open('Data.txt', 'w')
        for prj in self.collection.values():
            f.write('{}-{}-{}-{}\n'.format(prj.name, prj.money.get(), prj.rateOfReturn.get(), prj.Return.get(),))
        f.close()
investCollection = invest_dic()

Button (window, text='计算', command=investCollection.jisuan).grid(row=0, column=4)
Button (window, text='添加新项目' ,command=investCollection.createAddtoCol).grid(row=0,column=5)
Button (window, text='保存', command=investCollection.savetoData).grid(row=0,column= 6)

class invest():
    '''
    获取并绘制单个投资项目，每个项目的属性有：名称、投资金额、年化率、预计回报
    '''
    def __init__(self, name, rownum):
        global project_frame
        global investCollection
        #self.investCollection = investCollection
        self.name = name
        print (self.name)
        self.rownum = rownum
        self.frame = project_frame
        Label(self.frame, text=self.name).grid(row=rownum, column=0) #添加投资项目名称
        self.money = IntVar()
        Entry(self.frame, textvariable=self.money).grid(row=rownum, column=1)
        self.rateOfReturn = DoubleVar()
        e_rate = Entry(self.frame, textvariable=self.rateOfReturn).grid(row=rownum, column=2)
        self.Return = DoubleVar()
        e_return = Entry(self.frame, textvariable=self.Return).grid(row=rownum, column=3)
    def jisuan(self):
        m = self.money.get()
        rate = self.rateOfReturn.get()
        self.Return.set(m * rate / 100/365)

'''
haha= invest('hah', 5)
haha.add_to_collection()
hehe= invest('heihei', 6)
hehe.add_to_collection()
'''
mainloop()



