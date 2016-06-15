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
        MSG.Showinfo("Hi, handsome boy.", str(*args))
        
        
        
Menu()
        
        
        
        
        
        
        
        