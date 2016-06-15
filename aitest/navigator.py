# -*- encoding: utf-8 -*-
'''
Current module: aitest.navigator

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      aitest.navigator,v 1.0 2016年6月15日
    FROM:   2016年6月15日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''
import sc
from com.ui import Window,Widget,ROOT,Tkconstants
from com import basic
from com.basic import MSG,FileDilog

Window.widg = ROOT
Window.Top(sc.TITLE)

menubar = Widget.Menu(ROOT)
Window.Config(menu = menubar)
ROOT.option_add("*Menu.tearOff", 0)

class Menu:
    
    def __init__(self):
        self.__main()
        basic.mainloop(ROOT, loop=True)
    
    def __main(self):            
        self.menus = {}
        Widget.GenerateMenu(menubar, sc.MENUS, self.menus)
        self.__set_menus_command()
        
    def __set_menus_command(self):
        node = self.menus.get(u"导航")
        print node
        Widget.RegisterMenu(node, u"接口测试", self.__test_function, u"clicked 接口测试")
        
    def __test_function(self,*args):
#         MSG.Showinfo("Hi, handsome boy.", str(*args))
        WebService()
        
class WebService:
    
    def __init__(self):
        self.__main()
    
    def __main(self):
        frame1 = Widget.Labelframe(ROOT)
        frame2 = Widget.Labelframe(ROOT)
        label_caseid        = Widget.Label(frame1)
        entry_caseid        = Widget.Entry(frame1)
        label_des           = Widget.Label(frame1)
        entry_des           = Widget.Entry(frame1)
        label_steps         = Widget.Label(frame1)
        entry_steps         = Widget.Entry(frame1)
        label_verify        = Widget.Label(frame1)
        entry_verify        = Widget.Entry(frame1)        
        label_precommand    = Widget.Label(frame2)
        entry_precommand    = Widget.Entry(frame2)
        label_head          = Widget.Label(frame2)
        entry_head          = Widget.Entry(frame2)
        label_data          = Widget.Label(frame2)
        entry_data          = Widget.Entry(frame2)
        label_postcommand   = Widget.Label(frame2)
        entry_postcommand   = Widget.Entry(frame2)
                
        Window.widg = label_caseid
        Window.Config(text = "TestCaseID:")
        Window.Grid(row=0, column=0)                
        Window.widg = entry_caseid
        Window.Grid(row=0, column=1)
        
        Window.widg = label_des
        Window.Config(text = "Description:")
        Window.Grid(row=1, column=0)            
        Window.widg = entry_des
        Window.Grid(row=1, column=1)
        
        Window.widg = label_steps
        Window.Config(text = "Steps:")
        Window.Grid(row=2, column=0)                
        Window.widg = entry_steps
        Window.Grid(row=2, column=1)
        
        Window.widg = label_verify
        Window.Config(text = "Verify:")
        Window.Grid(row=3, column=0)                
        Window.widg = entry_verify
        Window.Grid(row=3, column=1)
        
        Window.widg = frame1
        Window.Config(text = "Part1")
        Window.Grid(row=0, column=0)
        
        Window.widg = label_precommand
        Window.Config(text = "PreCommand:")
        Window.Grid(row=0, column=0)                
        Window.widg = entry_precommand
        Window.Grid(row=0, column=1)
        
        Window.widg = label_head
        Window.Config(text = "Head:")
        Window.Grid(row=1, column=0)                
        Window.widg = entry_head
        Window.Grid(row=1, column=1)
        
        Window.widg = label_data
        Window.Config(text = "Data:")
        Window.Grid(row=2, column=0)                
        Window.widg = entry_data
        Window.Grid(row=2, column=1)
        
        Window.widg = label_postcommand
        Window.Config(text = "PostCommand:")
        Window.Grid(row=3, column=0)                
        Window.widg = entry_postcommand
        Window.Grid(row=3, column=1)
        
        Window.widg = frame2
        Window.Config(text = "Part2")
        Window.Grid(row=0, column=1, sticky= "NSEW")
Menu()         
 
        
        
        
        
        
        