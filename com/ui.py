# -*- encoding: utf-8 -*-
'''
Current module: com.ui

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      com.ui,v 1.0 2016年6月6日
    FROM:   2016年6月6日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

import Tkinter,Tkconstants


TOP = Tkinter.Tk()

import basic
class Window:    
    widg = None
    
    @classmethod
    def Top(cls,title,geometry="", resizable_x = 0, resizable_y = 0):
#         geometry = 510x140+200+200
        top = basic.get_widget_toplevel(cls.widg)
        top.title(title)
        top.geometry(geometry)
        top.resizable(resizable_x,resizable_y) 
    
    @classmethod
    def Pack(cls,side = Tkconstants.TOP, fill = Tkconstants.NONE, expand = Tkconstants.NO, pady = 0, padx = 0, **kw):
        cls.widg.pack(side = side,fill = fill, expand = expand, pady = pady, padx = padx, **kw)

    @classmethod
    def Config(cls,**conf):
        keys = basic.get_configuration_keys(cls.widg)
        for k in conf:
            if not k in keys:
                raise Exception("invalide configuration key: %s" %k)
        basic.set_configuration(cls.widg,**conf)
    
    @classmethod
    def ConfigVar(cls,var_key="listvariable"):        
        '''Sample usage:
                var = ConfigVar("textvariable")
                var.set("set values")
                print var.get()
        '''
        confs = {}
        confs[var_key] = Tkinter.StringVar()
        basic.set_configuration(cls.widg,**confs)
        return confs.get(var_key)    
        
    @classmethod  
    def Bind(cls, sequence=None, func=None, add=None, className=None):
        if className == None:
            return cls.widg.bind(sequence, func, add)
        elif className.lower() == "all":
            return cls.widg.bind_all(sequence, func, add)
        else:
            return cls.widg.bind_class(className, sequence, func, add)

    @classmethod
    def UnBind(cls, sequence, className = None):
        if className == None:
            return cls.widg.unbind(sequence)
        elif className.lower() == "all":
            return cls.widg.unbind_all(sequence)
        else:
            return cls.widg.unbind_class(className, sequence)

        
import ttk
class Widget:
    '''"
    Not packing:
        Combobox", "Frame",
       "Menubutton", "Notebook",
       "Scale","Separator", "Sizegrip", "Style",       
    '''
    
    @classmethod
    def Panedwindow(cls,master,**kw):
        return ttk.Panedwindow(master,**kw)
    
    @classmethod
    def Labelframe(cls,master=None, **kw):
        return ttk.Labelframe(master,**kw)
    
    @classmethod
    def Progressbar(cls,master,**kw):
        return ttk.Progressbar(master,**kw)
    
    @classmethod
    def Label(cls,master,**kw):
        return ttk.Label(master,**kw)
    
    @classmethod
    def Entry(cls,master,**kw):
        return ttk.Entry(master,**kw)
    
    @classmethod
    def Radiobutton(cls,master,**kw):
        return ttk.Radiobutton(master,**kw)
    
    @classmethod
    def Checkbutton(cls,master,**kw):
        return ttk.Checkbutton(master,**kw)
    
    @classmethod
    def Scrollbar(cls,master,**kw):
        return ttk.Scrollbar(master,**kw)
    
    @classmethod
    def Treeview(cls,master,**kw):
        return ttk.Treeview(master,**kw)
    
    @classmethod
    def Button(cls,master,**kw):
        return ttk.Button(master,**kw)
    
    @classmethod
    def Text(cls,master=None, cnf={}, **kw):
        return Tkinter.Text(master, cnf, **kw)
        
    @classmethod
    def Listbox(cls,master=None, cnf={}, **kw):
        return Tkinter.Listbox(master, cnf, **kw)    
    
    @classmethod
    def Menu(cls,master=None, cnf={}, **kw):
        return Tkinter.Menu(master, cnf, **kw)
    
    @classmethod
    def GenerateMenu(cls,menubar_obj,title_tree,var,leaf=0):
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
        
        
    
    
    
    
    
                
            