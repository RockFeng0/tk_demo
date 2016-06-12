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

