# -*- encoding: utf-8 -*-
'''
Current module: pyrunner.ui.navigator

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      pyrunner.ui.navigator,v 1.0 2016年3月1日
    FROM:   2016年3月1日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

import os,Tkinter,ttk,tkMessageBox,tkFileDialog
import sc,style,data
from Tkconstants import *

# ##############################################    基础功能   #########################################
VERSION = "1.0" 

def mainloop(obj,loop = False):
    if loop:
        obj.mainloop()
        
def pop_info_message(title,message):
    tkMessageBox.showinfo(title,message)

def pop_eror_message(title,message):
    tkMessageBox.showerror(title,message)
    
def pop_warning_message(title,message):
    tkMessageBox.showwarning(title,message)

def open_file_dialog(**opts):
    return tkFileDialog.askopenfilename(multiple = True,initialdir=os.environ.get("systemdrive"),**opts)    

def save_file_dialog(**opt):
    value = tkFileDialog.asksaveasfilename(initialdir=os.environ.get("systemdrive"),**opt)
    sc.Tmp.setValue(value)
                
# ##############################################    自动化界面 导航   #########################################

class Switcher:
    destroyer = None
    
    @classmethod
    def to_home(cls):        
        cls.__destroy()
        PyRunnerMain() 
    
    @classmethod
    def to_web_service(cls):        
        cls.__destroy()
        AutoWebService()
    
    @classmethod
    def to_ui_web(cls):
        cls.__destroy()
        AutoWebUI()        
    
    @classmethod
    def to_ui_mobile(cls):
        cls.__destroy()
        AutoMobileUI()        
    
    @classmethod
    def to_ui_client(cls):
        cls.__destroy()
        AutoClientUI()        
    
    @classmethod
    def __destroy(cls):
        cls.destroyer.destroy()
        
class PyRunnerMain():
    def __init__(self, loop = False):
        self.__main()
        mainloop(sc.top,loop)
    
    def __main(self):
        sc.top             = Tkinter.Tk()
        style.PyRunnerMain.top(sc.top)
        
        sc.mapMain["frame1"]          = ttk.LabelFrame(sc.top, text = "Selections.")
        sc.mapMain["bt_webservice"]   = Tkinter.Button(sc.mapMain["frame1"], text = "Web Service Test")
        sc.mapMain["bt_web"]          = Tkinter.Button(sc.mapMain["frame1"], text = "Web Test")
        sc.mapMain["bt_mobile"]       = Tkinter.Button(sc.mapMain["frame1"], text = "Mobile App Test")
        sc.mapMain["bt_agent"]        = Tkinter.Button(sc.mapMain["frame1"], text = "UI Client")
        
        for i in ("bt_webservice","bt_web","bt_mobile","bt_agent","frame1"):
            style.PubStyle.pack(sc.mapMain[i],side = "top")
        
        style.PubStyle.bind_command2config(sc.mapMain["bt_webservice"],self.__guider,"to_web_service")
        style.PubStyle.bind_command2config(sc.mapMain["bt_web"],self.__guider,"to_ui_web")
        style.PubStyle.bind_command2config(sc.mapMain["bt_mobile"],self.__guider,"to_ui_mobile")
        style.PubStyle.bind_command2config(sc.mapMain["bt_agent"],self.__guider,"to_ui_client")
    
    def __guider(self,name):
        Switcher.destroyer = sc.mapMain["frame1"]
        getattr(Switcher, name)()    


# ##############################################    Web Service 自动化界面    #########################################    
class AutoWebService_back():
    def __init__(self,loop = False):
        self.__main()        
        mainloop(sc.top,loop)
    
    def __main(self):
        
        ### top whether exists.
        if not sc.top:
            sc.top = Tkinter.Tk()
        style.AutoWebService.top(sc.top)
    
        ### Menu
        m = Tkinter.Menu()
        sc.top.configure(menu = m)  
        sc.top.option_add("*Menu.tearOff", 0)
        web_service_menu = [{
                u"文件": [u"加载",u"自动加载",u"偏好设置"]
            },
            {
                u"编辑": [u"移除选中项",u"列表清空"]
            },
            {
                u"运行": [u"停止",u"选中运行",u"全部运行"]
            },
            {
                u"报告": [u"查看报告",u"邮件发送报告"]
            },
            {
                u"关于": u"版本信息"
            }]
        style.PubStyle.generate_menu(m, web_service_menu,sc.mapWebService["menus"])
        for k,v in sc.mapWebService["menus"].items():
            print k,repr(v)
            
        ### panedwindow and frame 
        sc.mapWebService["panedwin"] = Tkinter.PanedWindow(sc.top)
        sc.mapWebService["panedwin"].config(orient = HORIZONTAL)
        
        for i in ("cases","status","steps","dataSource","console"):
            if i == "cases":
                sc.mapWebService[i + "_frame"]         = ttk.LabelFrame(sc.mapWebService["panedwin"],text = i.capitalize())
            elif i == "status":
                sc.mapWebService[i + "_frame"]         = ttk.LabelFrame(sc.mapWebService["panedwin"],text = i.capitalize())
                continue
            else:
                sc.mapWebService[i + "_frame"]         = ttk.LabelFrame(sc.mapWebService["status_frame"],text = i.capitalize())
            sc.mapWebService[i + "_listbox"]       = Tkinter.Listbox(sc.mapWebService[i + "_frame"])
            sc.mapWebService[i + "_scrollbar_x"]   = Tkinter.Scrollbar(sc.mapWebService[i + "_frame"], orient = HORIZONTAL, command = sc.mapWebService[i + "_listbox"].xview)
            sc.mapWebService[i + "_scrollbar_y"]   = Tkinter.Scrollbar(sc.mapWebService[i + "_frame"], orient = VERTICAL, command = sc.mapWebService[i + "_listbox"].yview)
            sc.mapWebService[i + "_listbox"].config(xscrollcommand = sc.mapWebService[i + "_scrollbar_x"].set, yscrollcommand = sc.mapWebService[i + "_scrollbar_y"].set)
            
        sc.mapWebService["cases_progressbar"]   = ttk.Progressbar(sc.mapWebService["cases_frame"], mode = "determinate")
        sc.mapWebService["console_progressbar"]   = ttk.Progressbar(sc.mapWebService["console_frame"], mode = "indeterminate")
        
        style.AutoWebService.pack_progre(sc.mapWebService["cases_listbox"], sc.mapWebService["cases_scrollbar_x"],sc.mapWebService["cases_scrollbar_y"], sc.mapWebService["cases_progressbar"])
        style.AutoWebService.pack_scroll(sc.mapWebService["steps_listbox"], sc.mapWebService["steps_scrollbar_x"],sc.mapWebService["steps_scrollbar_y"])
        style.AutoWebService.pack_scroll(sc.mapWebService["dataSource_listbox"], sc.mapWebService["dataSource_scrollbar_x"],sc.mapWebService["dataSource_scrollbar_y"])
        style.AutoWebService.pack_progre(sc.mapWebService["console_listbox"], sc.mapWebService["console_scrollbar_x"],sc.mapWebService["console_scrollbar_y"], sc.mapWebService["console_progressbar"])
        style.PubStyle.pack(sc.mapWebService["console_frame"],side = "bottom")
        style.PubStyle.pack(sc.mapWebService["dataSource_frame"],side = "bottom")
        style.PubStyle.pack(sc.mapWebService["steps_frame"],side = "bottom")
        
        sc.mapWebService["panedwin"].add(sc.mapWebService["cases_frame"])
        sc.mapWebService["panedwin"].add(sc.mapWebService["status_frame"])
        style.PubStyle.pack(sc.mapWebService["panedwin"],side = "top")
        
class AutoWebService():
    def __init__(self,loop = False):
        self.wbs_menu = [{
                u"文件": [u"加载",u"自动加载",u"偏好设置"]
            },
            {
                u"编辑": [u"移除选中项",u"列表清空"]
            },
            {
                u"运行": [u"停止",u"选中运行",u"全部运行"]
            },
            {
                u"报告": [u"查看报告",u"邮件发送报告"]
            },
            {
                u"模式切换": [u"首页",u"页面测试",u"客户端测试",u"移动应用测试",u"网络服务测试"]
            },
            {
                u"帮助": u"关于"
            },]
        self.__main()   
        mainloop(sc.top,loop)
    
    def __main(self):        
        ### top whether exists.
        try:
            sc.top.state()
        except:
            sc.top = Tkinter.Tk()
        finally:
            style.AutoWebService.top(sc.top)
    
        ### Menu
        m = Tkinter.Menu()
        sc.top.configure(menu = m)  
        sc.top.option_add("*Menu.tearOff", 0)        
        style.PubStyle.generate_menu(m, self.wbs_menu,sc.mapWebService["menus"])
        self.__add_menu_item_command()
            
        ### panedwindow and frame 
        sc.mapWebService["panedwin"] = Tkinter.PanedWindow(sc.top)        
        sc.mapWebService["panedwin"].config(orient = HORIZONTAL)
        
        sc.mapWebService["cases_frame"]         = ttk.LabelFrame(sc.mapWebService["panedwin"],text = "Cases")
        sc.mapWebService["cases_tree"]          = ttk.Treeview(sc.mapWebService["cases_frame"])
        sc.mapWebService["cases_scrollbar_x"]   = Tkinter.Scrollbar(sc.mapWebService["cases_frame"], orient = HORIZONTAL, command = sc.mapWebService["cases_tree"].xview)
        sc.mapWebService["cases_scrollbar_y"]   = Tkinter.Scrollbar(sc.mapWebService["cases_frame"], orient = VERTICAL, command = sc.mapWebService["cases_tree"].yview)
        sc.mapWebService["cases_tree"].config(xscrollcommand = sc.mapWebService["cases_scrollbar_x"].set, yscrollcommand = sc.mapWebService["cases_scrollbar_y"].set)
        sc.mapWebService["cases_tree"].heading("#0",text='Path', anchor='w')
            
        for i in ("status","steps","dataSource","console"):  
            if i == "status":
                sc.mapWebService[i + "_frame"]         = ttk.LabelFrame(sc.mapWebService["panedwin"],text = i.capitalize())
                continue
            else:
                sc.mapWebService[i + "_frame"]         = ttk.LabelFrame(sc.mapWebService["status_frame"],text = i.capitalize())
            
            sc.mapWebService[i + "_listbox"]       = Tkinter.Listbox(sc.mapWebService[i + "_frame"])
            sc.mapWebService[i + "_scrollbar_x"]   = Tkinter.Scrollbar(sc.mapWebService[i + "_frame"], orient = HORIZONTAL, command = sc.mapWebService[i + "_listbox"].xview)
            sc.mapWebService[i + "_scrollbar_y"]   = Tkinter.Scrollbar(sc.mapWebService[i + "_frame"], orient = VERTICAL, command = sc.mapWebService[i + "_listbox"].yview)
            sc.mapWebService[i + "_listbox"].config(xscrollcommand = sc.mapWebService[i + "_scrollbar_x"].set, yscrollcommand = sc.mapWebService[i + "_scrollbar_y"].set)

        sc.mapWebService["cases_progressbar"]   = ttk.Progressbar(sc.mapWebService["cases_frame"], mode = "determinate")
        sc.mapWebService["console_progressbar"]   = ttk.Progressbar(sc.mapWebService["console_frame"], mode = "indeterminate")
        
        style.AutoWebService.pack_progre(sc.mapWebService["cases_tree"], sc.mapWebService["cases_scrollbar_x"],sc.mapWebService["cases_scrollbar_y"], sc.mapWebService["cases_progressbar"])
        style.AutoWebService.pack_scroll(sc.mapWebService["steps_listbox"], sc.mapWebService["steps_scrollbar_x"],sc.mapWebService["steps_scrollbar_y"])
        style.AutoWebService.pack_scroll(sc.mapWebService["dataSource_listbox"], sc.mapWebService["dataSource_scrollbar_x"],sc.mapWebService["dataSource_scrollbar_y"])
        style.AutoWebService.pack_progre(sc.mapWebService["console_listbox"], sc.mapWebService["console_scrollbar_x"],sc.mapWebService["console_scrollbar_y"], sc.mapWebService["console_progressbar"])
        style.PubStyle.pack(sc.mapWebService["console_frame"],side = "bottom")
        style.PubStyle.pack(sc.mapWebService["dataSource_frame"],side = "bottom")
        style.PubStyle.pack(sc.mapWebService["steps_frame"],side = "bottom")
        
        sc.mapWebService["panedwin"].add(sc.mapWebService["cases_frame"])
        sc.mapWebService["panedwin"].add(sc.mapWebService["status_frame"])
        style.PubStyle.pack(sc.mapWebService["panedwin"],side = "top")
                
        
    def __add_menu_item_command(self):
        node = sc.mapWebService["menus"].get(u"文件")
        style.PubStyle.bind_command2menu(node, u'加载', self.__load_tree_file)
        style.PubStyle.bind_command2menu(node, u'自动加载', self.__auto_load_tree_file)
        style.PubStyle.bind_command2menu(node, u'偏好设置', self.__open_preference)
        
        node = sc.mapWebService["menus"].get(u"编辑")
        style.PubStyle.bind_command2menu(node, u'移除选中项', self.__remove_tree_item)
        style.PubStyle.bind_command2menu(node, u'列表清空', self.__remove_tree_data)
        
        node = sc.mapWebService["menus"].get(u"运行")
        style.PubStyle.bind_command2menu(node, u'停止', self.__run_stop)
        style.PubStyle.bind_command2menu(node, u'选中运行', self.__run_tree_item)
        style.PubStyle.bind_command2menu(node, u'全部运行', self.__run_tree_all)
        
        node = sc.mapWebService["menus"].get(u"报告")
        style.PubStyle.bind_command2menu(node, u'查看报告', self.__view_report)
        style.PubStyle.bind_command2menu(node, u'邮件发送报告', self.__send_report_mail)
        
        node = sc.mapWebService["menus"].get(u"模式切换")
        Switcher.destroyer = sc.top
        style.PubStyle.bind_command2menu(node, u"首页", Switcher.to_home)  
        style.PubStyle.bind_command2menu(node, u"页面测试", Switcher.to_ui_web)        
        style.PubStyle.bind_command2menu(node, u"客户端测试", Switcher.to_ui_client)
        style.PubStyle.bind_command2menu(node, u"移动应用测试", Switcher.to_ui_mobile)        
        style.PubStyle.bind_command2menu(node, u"网络服务测试", Switcher.to_web_service)
        
        node = sc.mapWebService["menus"].get(u"帮助")
        style.PubStyle.bind_command2menu(node, u"关于", pop_info_message,"AutoApp Version %s" %VERSION, "Automation test tool-autoApp. \n\nAutoApp Version %s \n\nAuthor-Bruce Luo" %VERSION)
    
    def __load_tree_file(self):
        value = open_file_dialog(filetypes = [("Excel",".xlsx"),("Excel",".xls"),("All","*")])
        all_files = value.split()
        for i in all_files:
            parent = style.PubStyle.add_tree_data(sc.mapWebService["cases_tree"], i)
            result = data.getWebServiceTreeData(i)
            if result:
                for j in result:
                    style.PubStyle.add_tree_data(sc.mapWebService["cases_tree"], j, parent)
    
    def __auto_load_tree_file(self):
        auto_load_dir = sc.mapWebServicePreference.get("project_entry_text")
        
        if not auto_load_dir:            
            pop_info_message(u"提示信息", u"自动加载前，请优先设置偏好.")
            return
        
#         auto_load_dir = string_var.get()
        if not os.path.isdir(auto_load_dir):            
            pop_info_message(u"提示信息", u"无效的自动加载路径，请设置正确的偏好.")
            return
        
        all_files = os.listdir(auto_load_dir)        
        for i in all_files:
            if i.endswith(".xlsx") or i.endswith(".xls"):
                file_abs_path = os.path.join(auto_load_dir,i)
                parent = style.PubStyle.add_tree_data(sc.mapWebService["cases_tree"], file_abs_path)
                result = data.getWebServiceTreeData(file_abs_path)
                if result:
                    for j in result:
                        style.PubStyle.add_tree_data(sc.mapWebService["cases_tree"], j, parent)
        
    def __open_preference(self):
        AutoWebServicePreference()
        
    def __remove_tree_item(self):
        style.PubStyle.remove_tree_item(sc.mapWebService["cases_tree"])
    
    def __remove_tree_data(self):
        style.PubStyle.remove_tree_data(sc.mapWebService["cases_tree"])
    
    def __run_tree_all(self):
        st = style.PubStyle.get_tree_executor(sc.mapWebService["cases_tree"])
        self.__run_start(st)         
        
    def __run_tree_item(self):
        st = style.PubStyle.get_tree_executor(sc.mapWebService["cases_tree"],True)
        self.__run_start(st)
    
    def __run_stop(self):
        sc.Tmp.setValue(True)
    
    def __run_start(self,st):
        for i in st:            
            if sc.Tmp.getValue():
                break
            sc.mapWebService["cases_tree"].selection_set(i) 
            print sc.mapWebService["cases_tree"].item(i).get("text")
        
    def __send_report_mail(self):
        print "send mail report todo."
        
    def __view_report(self):
        print "view report todo."
                    
    def __add_variables_relation(self):
        sc.mapWebService["cases_tree"]
        sc.mapWebService["data_cases_tree"]
        pass    
            
    def __cases_tree(self):
        pass
    
class AutoWebServicePreference():
    def __init__(self,loop=False):
        self.__main()
        mainloop(sc.mapWebServicePreference.get("top"), loop)
            
    def __main(self):
        ### top whether exists.
        try:
            sc.top.state()
        except:
            sc.mapWebServicePreference["top"] = Tkinter.Tk()
        else:
            sc.mapWebServicePreference["top"] = Tkinter.Toplevel(sc.top)
        finally:
            style.AutoWebService.top_preference(sc.mapWebServicePreference["top"])
            
        sc.mapWebServicePreference["frame1"]            = ttk.LabelFrame(sc.mapWebServicePreference["top"],text="Project path")
        sc.mapWebServicePreference["project_label"]     = Tkinter.Label(sc.mapWebServicePreference["frame1"],text = "Project load from:", width = 16, anchor = "w")
        sc.mapWebServicePreference["project_entry"]     = Tkinter.Entry(sc.mapWebServicePreference["frame1"], width = 40, state = "disable")
        sc.mapWebServicePreference["project_button"]    = Tkinter.Button(sc.mapWebServicePreference["frame1"], text = "Select dir.")
        sc.mapWebServicePreference["project_label"].pack(side = "left")
        sc.mapWebServicePreference["project_entry"].pack(side = "left")
        sc.mapWebServicePreference["project_button"].pack(side = "left", pady = 5, padx = 10)
        sc.mapWebServicePreference["frame1"].pack(side = "top", expand = "no", fill = "both", pady = 2, padx = "2m")
            
        sc.mapWebServicePreference["frame2"]                = ttk.LabelFrame(sc.mapWebServicePreference["top"],text="Run time setup")
        sc.mapWebServicePreference["scheduleRunLabel"]      = Tkinter.Label(sc.mapWebServicePreference["frame2"],text = "Run after(minutes):", width = 16, anchor = "w")        
        sc.mapWebServicePreference["scheduleRunAllEntry"]   = Tkinter.Entry(sc.mapWebServicePreference["frame2"], state = sc.mapWebServicePreference["schedule_run_entry_state"], width = 40, validate = "key")
        sc.mapWebServicePreference["scheduleRunAllButton"]  = Tkinter.Button(sc.mapWebServicePreference["frame2"], text = sc.mapWebServicePreference["schedule_run_button_text"])          
        sc.mapWebServicePreference["scheduleRunLabel"].pack(side = "left")
        sc.mapWebServicePreference["scheduleRunAllEntry"].pack(side = "left")
        sc.mapWebServicePreference["scheduleRunAllButton"].pack(side = "left", pady = 5, padx = 10)
        sc.mapWebServicePreference["frame2"].pack(side = "top", expand = "no", fill = "both", pady = 2, padx = "2m")        
        self.__add_bind_relation()
    
    def __add_bind_relation(self):
        sc.mapWebServicePreference["project_entry_variable"] = style.PubStyle.bind_variable2config(sc.mapWebServicePreference["project_entry"], "textvariable")
        sc.mapWebServicePreference["project_entry_variable"].get("textvariable").set(sc.mapWebServicePreference["project_entry_text"]);#定义初始值
        style.PubStyle.bind_command2config(sc.mapWebServicePreference["project_button"], self.__select_dir)

        sc.mapWebServicePreference["schedule_run_entry_variable"] = style.PubStyle.bind_variable2config(sc.mapWebServicePreference["scheduleRunAllEntry"], "textvariable")
        sc.mapWebServicePreference["schedule_run_entry_variable"].get("textvariable").set(sc.mapWebServicePreference["schedule_run_entry_text"]);#定义初始值
        style.PubStyle.bind_invalidcommand2config(sc.mapWebServicePreference["scheduleRunAllEntry"], self.__invalid_msg)
        style.PubStyle.bind_validatecommand2config(sc.mapWebServicePreference["scheduleRunAllEntry"], self.__valid_num,'%P')
        style.PubStyle.bind_command2config(sc.mapWebServicePreference["scheduleRunAllButton"], self.__schedule_run)
                                                                                                    
    def __select_dir(self):
        pth = tkFileDialog.askdirectory()
        sc.mapWebServicePreference["project_entry_variable"].get("textvariable").set(pth)
        sc.mapWebServicePreference["project_entry_text"] = pth
    
    def __valid_num(self,P):
        if len(P) == 0 or P.isdigit() and len(P) <10:
            return True        
        return False
        
    def __invalid_msg(self):
        pop_info_message("Invalid number", "String should be integer and lenth <10")
        
    def __schedule_run(self):        
        swt_text = ["Setup ok.","Reset time."]
        current_text = sc.mapWebServicePreference["scheduleRunAllButton"].cget("text")
        
        if swt_text.index(current_text) == 0:
            sc.mapWebServicePreference["schedule_run_entry_state"] = "disable"
            sc.mapWebServicePreference["schedule_run_button_text"] = "Reset time."
            sc.mapWebServicePreference["scheduleRunAllEntry"].config(state = sc.mapWebServicePreference["schedule_run_entry_state"])            
            sc.mapWebServicePreference["scheduleRunAllButton"].config(text = sc.mapWebServicePreference["schedule_run_button_text"])

            str_time = sc.mapWebServicePreference["scheduleRunAllEntry"].get()
            
            def f():
                tmp_obj = sc.mapWebService["menus"].get(u"运行")
                if tmp_obj:
                    tmp_obj.invoke(u"全部运行")
                else:
                    print "Timmer not effect."
            
            if str_time:
                mtime = int(str_time) * 1000
            else:
                mtime = 0
            sc.mapWebServicePreference["data_autorunn_timmer"] = sc.mapWebServicePreference["top"].after(mtime,f)
            sc.mapWebServicePreference["schedule_run_entry_text"] = int(str_time)
            
        if swt_text.index(current_text) == 1:
            sc.mapWebServicePreference["top"].after_cancel(sc.mapWebServicePreference["data_autorunn_timmer"])
            sc.mapWebServicePreference["schedule_run_entry_state"] = "normal"
            sc.mapWebServicePreference["schedule_run_button_text"] = "Setup ok."
            sc.mapWebServicePreference["scheduleRunAllEntry"].config(state = sc.mapWebServicePreference["schedule_run_entry_state"]) 
            sc.mapWebServicePreference["scheduleRunAllButton"].config(text = sc.mapWebServicePreference["schedule_run_button_text"])
        
        
        
# ##############################################    Web UI 自动化界面    #########################################
class AutoWebUI:
    def __init__(self,loop = False):
        self.__main()        
        mainloop(sc.top,loop)
        
    def __main(self):        
        ### top whether exists.
        try:
            sc.top.state()
        except:
            sc.top = Tkinter.Tk()
        style.AutoWebUI.top(sc.top)
        t = Tkinter.Text(sc.top)
        t.insert(0.0, "switch to web automation")        
        style.PubStyle.pack(t)

        
# ##############################################    Mobile UI 自动化界面    #########################################

class AutoMobileUI:
    def __init__(self,loop = False):
        self.__main()        
        mainloop(sc.top,loop)
    
    def __main(self):        
        ### top whether exists.
        try:
            sc.top.state()
        except:
            sc.top = Tkinter.Tk()
        style.AutoMobileUI.top(sc.top)
        t = Tkinter.Text(sc.top)
        t.insert(0.0, "switch to mobile automation")        
        style.PubStyle.pack(t)


# ##############################################    客户端  UI 自动化界面    #########################################
class AutoClientUI:
    def __init__(self,loop = False):
        self.__main()        
        mainloop(sc.top,loop)

    def __main(self):        
        ### top whether exists.
        try:
            sc.top.state()
        except:
            sc.top = Tkinter.Tk()
        style.AutoClientUI.top(sc.top)
        t = Tkinter.Text(sc.top)
        t.insert(0.0, "switch to client automation")        
        style.PubStyle.pack(t)

if __name__ == "__main__":
    PyRunnerMain(loop = True)
#     AutoWebServicePreference(loop=True)
        
        
        
        
        
        
        
        
        