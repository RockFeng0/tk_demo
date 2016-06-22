# -*- encoding: utf-8 -*-
'''
Current module: com.suite

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      com.suite,v 1.0 2016年6月22日
    FROM:   2016年6月22日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''
import basic
from ui import Widget,Window,Tkconstants,Tkinter
from com.ui import Widget


class Components:
        
    @classmethod
    def GenerateMenu(cls,menubar_obj,title_tree,var,leaf=0):
        '''Sample usage:
            from ui import ROOT
            menubar = Widget.Menu(ROOT)
            
            Window.widg = ROOT
            Window.Config(menu = menubar)
            ROOT.option_add("*Menu.tearOff", 0)  
            result = {}
            menus = [
                 {u"执行":[u"运行当前",u"速度"]}, 
                 {u"导航":{u"呃呃":[u"得分",u"很好"]}},         
                 ]
            
            Components.GenerateMenu(menubar, menus, result)
            
            
            def test(*args):
                print args[0]
            node = result.get(u"执行")
            Components.RegisterMenu(node, u"运行当前", test, "webservice")
            node = result.get(u"呃呃")
            Components.RegisterMenu(node, u"得分", test, "current")
        '''
        if isinstance(title_tree,list):
            for i in title_tree:
                cls.GenerateMenu(menubar_obj,i,var,leaf=1);#列表格式，里边放是叶子节点,设置leaf=1
                
        elif isinstance(title_tree,dict):
            # 字典格式，里边的子节点，不是叶子节点，设置leaf=0
            for k,v in title_tree.items():             
                var[k] = Tkinter.Menu();# 记录每一个Menu子节点的实例对象
                menubar_obj.add("cascade",label=k, menu = var[k]);# cascade允许 menu参数，建立 Menu item                    
                cls.GenerateMenu(var[k],v,var,leaf=0)
        else:
            # 叶子节点
            if leaf == 0:
                var[title_tree] = Tkinter.Menu()
                menubar_obj.add("cascade",label=title_tree, menu = var[title_tree])
            else:
                menubar_obj.add("command",label=title_tree);# command没有menu参数,建立叶子节点      
                
    @classmethod
    def RegisterMenu(cls,menu_node,menu_leaf_name,function,*func_args):
        command = basic.register_command(menu_node, function, *func_args)
        leaf_index = menu_node.index(menu_leaf_name)
        menu_node.delete(leaf_index)
        menu_node.insert_command(leaf_index,label=menu_leaf_name,command=command)
        
    @classmethod
    def ListWithScrollbar(cls,master,side = "top", fill="both", expand="yes", **kw):
        '''Sample usage:
            from ui import ROOT    
            frame1 = Widget.Labelframe(ROOT,text = "sssss")
            (l,x,y) = Components.ListWithScrollbar(frame1,side = "top", fill="both", expand="yes",padx = "0.5c")
            elems = ["Don't speculate, measure", "Waste not, want not", "Early to bed and early to rise makes a man healthy, wealthy, and wise", "Ask not what your country can do for you, ask what you can do for your country", "I shall return", "NOT", "A picture is worth a thousand words", "User interfaces are hard to build", "Thou shalt not steal", "A penny for your thoughts", "Fool me once, shame on you;  fool me twice, shame on me", "Every cloud has a silver lining", "Where there's smoke there's fire", "It takes one to know one", "Curiosity killed the cat", "Take this job and shove it", "Up a creek without a paddle", "I'm mad as hell and I'm not going to take it any more", "An apple a day keeps the doctor away", "Don't look a gift horse in the mouth", "Measure twice, cut once"]
            l.insert(0,*elems)
            ROOT.mainloop()
        '''
        lb = Widget.Listbox(master, width = 20, height = 10, setgrid = 1)
        s_x = Widget.Scrollbar(master,orient = Tkconstants.HORIZONTAL, command = lb.xview)
        s_y = Widget.Scrollbar(master,orient = Tkconstants.VERTICAL, command = lb.yview)
          
        Window.widg = lb
        Window.Config(xscrollcommand = s_x.set, yscrollcommand = s_y.set)
        Window.Grid(row =0, column = 0, rowspan = 1, columnspan = 1, sticky = Tkconstants.NSEW)
        
        Window.widg = s_y
        Window.Grid(row =0, column = 1, rowspan = 1, columnspan = 1, sticky = Tkconstants.NSEW)
        
        Window.widg = s_x
        Window.Grid(row =1, column = 0, rowspan = 1, columnspan = 1, sticky = Tkconstants.NSEW)
        
        Window.widg = master
        master.rowconfigure(0,weight =1, minsize = 0)
        master.columnconfigure(0,weight =1, minsize = 0)
        Window.Pack(side = side, fill=fill, expand = expand, **kw)
        return (lb,s_x,s_y)
    
def TextWithScrollbar(master):
    tx = Widget.Text(master, width = 60, height = 24, font = )
    s_x = Widget.Scrollbar(master)
    s_y = Widget.Scrollbar(master)
    
    text $w.text -yscrollcommand "$w.scroll set" -setgrid true -width 60 -height 24 -font $font -wrap word
    scrollbar $w.scroll -command "$w.text yview"
    pack $w.scroll -side right -fill y
    pack $w.text -expand yes -fill both


    
if __name__ == "__main__":
    from ui import ROOT    
        
    ROOT.mainloop()

