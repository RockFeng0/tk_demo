# -*- encoding: utf-8 -*-
'''
Current module: pyrunner.ui.style

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      pyrunner.ui.style,v 1.0 2016年3月1日
    FROM:   2016年3月1日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''
from Tkinter import Menu,StringVar

class PubStyle:    
    
    @classmethod
    def pack(cls,obj,**opts):
        obj.pack(expand = "yes", fill = "both", pady = 2, padx = "2m",**opts)
    
    @classmethod
    def generate_menu(cls,menubar_obj,title_tree,var,level=0):    
        #Sample usage: 
        #    result={}; menu(obj,[{1:[2,3,4]},{2:{3:[4,5,6]}},3],result)
        
        if isinstance(title_tree,list):
            for i in title_tree:
                cls.generate_menu(menubar_obj,i,var,level)
                
        elif isinstance(title_tree,dict):
            # 子节点
            for k,v in title_tree.items():                                
                var[k] = Menu();# 记录每一个Menu子节点的实例对象
                menubar_obj.add("cascade",label=k, menu = var[k]);# -menu 参数建立 Menu item 
                print "%s%s%s" %("\t"*level,k,repr(var[k]))            
                cls.generate_menu(var[k],v,var,level+1)
                
        else:
            # 叶子节点
            if level == 0:                
                menubar_obj.add("cascade",label=title_tree)
            else:
                menubar_obj.add("command",label=title_tree)
            print "%s%s" %("\t"*level,title_tree)
    
    @classmethod
    def bind_command2config(cls,normal_obj,func,*args_list):
        '''Sample usage:
        def func():
            print "i'm test"
           
        def func2(a,b,c):
            print "i'm test %s %s %s" %(a,b,c)
            
        normal_obj = Button(text = "bt1")
        bind_command2config(normal_obj,func)
        bind_command2config(normal_obj,func2,"1","2","3")
        '''         
        cmd = [normal_obj.register(func)] + list(args_list)
        normal_obj.config(command = tuple(cmd))
    
    @classmethod
    def bind_command2menu(cls,menu_node,menu_leaf_name,function,*func_args):
        '''Sample usage:
        def func():
            print "i'm test"
           
        def func2(a,b,c):
            print "i'm test %s %s %s" %(a,b,c)
            
        node = result.get(u'帮助');得到menu实例对象
        bind_command2menu(node,u"关于",func)
        bind_command2menu(node,u"注册",func2,"1","2","3")
        '''
        cmd = [menu_node.register(function)] + list(func_args)        
        leaf_index = menu_node.index(menu_leaf_name)
        menu_node.delete(leaf_index)        
        menu_node.insert_command(leaf_index,label=menu_leaf_name,command=tuple(cmd))
    
    @classmethod
    def bind_validatecommand2config(cls,normal_obj,func,*args_list):
        '''validate text commannd '''       
        cmd = [normal_obj.register(func)] + list(args_list)
        normal_obj.config(validatecommand = tuple(cmd))
    
    @classmethod
    def bind_invalidcommand2config(cls,normal_obj,func,*args_list):
        '''invalid text command'''       
        cmd = [normal_obj.register(func)] + list(args_list)
        normal_obj.config(invalidcommand = tuple(cmd))
    
    @classmethod
    def bind_variable2config(cls,normal_obj,*opts):
        '''bind text to variable
            Sample usage:
                result = bind_variable2config(entry_obj,"textvariable")
                var = result.get("textvariable")
                var.set("set values")
                print var.get()
        '''        
        confs = {}        
        for k in opts:
            confs[k] = StringVar()
            
        normal_obj.config(**confs)
        
        return confs
                
    @classmethod
    def add_tree_data(cls,tree_obj, value, parent=""):
        print "---> level: %s" %parent
        return tree_obj.insert(parent,"end", text=value, open=True)
    
    @classmethod
    def remove_tree_data(cls,tree_obj):
        # 清空
        for i in tree_obj.get_children():
            tree_obj.delete(i)
            
    @classmethod
    def remove_tree_item(cls,tree_obj):
        # 移除选项
        for i in tree_obj.selection():
            tree_obj.delete(i)
            
    @classmethod            
    def get_tree_process_iid(cls,tree_obj,iid=None):
        # 遍历 
        ll = tree_obj.get_children(iid)
         
        for i in ll:
            yield i
            if tree_obj.get_children(i):
                for j in cls.process_iid(i):
                    yield j
    
    @classmethod
    def get_tree_executor(cls,tree_obj, piece = False):
        # 执行
        if piece:
            datas = tree_obj.selection()            
        else:
            datas = cls.get_tree_process_iid(tree_obj)            
            
        for data in datas:
            yield data      
            
    @classmethod
    def test(cls):
        pass
    
class PyRunnerMain:
    
    @classmethod
    def top(cls,obj):
        obj.title("PyRunner")
        obj.geometry("292x169+524+299")
        obj.resizable(0,0)

class AutoWebService:
    
    @classmethod
    def top(cls,obj):
        obj.title("PyRunner WebService Test")
        obj.geometry("800x600+306+127")
        obj.resizable(1,1)
        
    @classmethod
    def top_preference(cls,obj):
        obj.title("Preference")
        obj.geometry("510x140+200+200")
        obj.resizable(0,0)    
    
    @classmethod
    def pack_progre(cls,list_box_obj,scroll_x_obj,scroll_y_obj,progressbar_obj):
        progressbar_obj.pack(side = "bottom",fill = "x",)
        scroll_x_obj.pack(side = "bottom",fill = "x",)
        scroll_y_obj.pack(side = "right",fill = "y",)
        list_box_obj.pack(side = "top",fill = "both", expand = "yes")
    
    @classmethod
    def pack_scroll(cls,list_box_obj,scroll_x_obj,scroll_y_obj):        
        scroll_x_obj.pack(side = "bottom",fill = "x",)
        scroll_y_obj.pack(side = "right",fill = "y",)
        list_box_obj.pack(side = "top",fill = "both", expand = "yes")
    
        
class AutoWebUI:
    
    @classmethod
    def top(cls,obj):
        obj.title("PyRunner Web UI Test")
        obj.geometry("800x600+306+127")
        obj.resizable(1,1)

class AutoMobileUI:
    
    @classmethod
    def top(cls,obj):
        obj.title("PyRunner Mobile UI Test")
        obj.geometry("800x600+306+127")
        obj.resizable(1,1)
        
class AutoClientUI:
    
    @classmethod
    def top(cls,obj):
        obj.title("PyRunner PC UI Test")
        obj.geometry("800x600+306+127")
        obj.resizable(1,1)
    
    
    