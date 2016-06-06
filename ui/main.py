# -*- encoding: utf-8 -*-
'''
Current module: pyrunner.ui.main

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      pyrunner.ui.main,v 1.0 2016年2月29日
    FROM:   2016年2月29日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

from Tkinter import *
import ttk

class UIMain():
    def __init__(self):
        self.mapMain = {
            "top" : None,
            "menuBar" : None,
            "menuCasFile" : None,
            "menuCasEdit" : None,
            "menuCasRun" : None,
            "menuCasReport" : None,
            "menuCasALM" : None,
            "menuCasHelp" : None,
            "panedWin" : None,
            "frame1" : None,
            "leftListbox" : None,
            "leftXScrollbar" : None,
            "leftYScrollbar" : None,
            "leftProgressbar" : None,
            "frame2" : None,
            "rightListboxUp" : None,
            "rightXScrollbarUp" : None,
            "rightYScrollbarUp" : None,
            "rightListboxDown" : None,
            "rightXScrollbarDown" : None,
            "rightYScrollbarDown" : None,
            "r_progressbar" : None,
        }
        self.__ui_main()
        self.__mainloop()
    
    def __mainloop(self):
        if self.mapMain.get("top"):
            self.mapMain.get("top").mainloop()
            
    def __ui_main(self):
        self.mapMain["top"] = Tk()
        self.mapMain["top"].title("Automation Test App");self.mapMain["top"].geometry("800x600");
        self.mapMain["top"].option_add("*Menu.tearOff", 0)
        
        #### Menus 
        self.mapMain["menuBar"] = Menu()
        self.mapMain["menuCasFile"] = Menu()
        self.mapMain["menuCasEdit"] = Menu()
        self.mapMain["menuCasRun"] = Menu()
        self.mapMain["menuCasReport"] = Menu()
        self.mapMain["menuCasALM"] = Menu()
        self.mapMain["menuCasHelp"] = Menu()        
        
        self.mapMain["top"].configure(menu = self.mapMain["menuBar"])        
        self.mapMain["menuBar"].add("cascade",label = u"文件",menu = self.mapMain["menuCasFile"])
        self.mapMain["menuBar"].add("cascade",label = u"编辑",menu = self.mapMain["menuCasEdit"])
        self.mapMain["menuBar"].add("cascade",label = u"执行",menu = self.mapMain["menuCasRun"])
        self.mapMain["menuBar"].add("cascade",label = u"分析报告",menu = self.mapMain["menuCasReport"])
        self.mapMain["menuBar"].add("cascade",label = u"ALM",menu = self.mapMain["menuCasALM"])
        self.mapMain["menuBar"].add("cascade",label = u"帮助",menu = self.mapMain["menuCasHelp"])
        
        self.mapMain["menuCasFile"].add_command(label = u"加载",command="fun1")
        self.mapMain["menuCasFile"].add_command(label = u"自动加载",command="fun2")
        self.mapMain["menuCasFile"].add_command(label = u"偏好设置",command="fun3")
        
        self.mapMain["menuCasEdit"].add_command(label = u"移除选中项", command = "fun4")
        self.mapMain["menuCasEdit"].add_command(label = u"列表清空", command = "fun5")
        
        self.mapMain["menuCasRun"].add_command(label = u"停止",command="fun1")
        self.mapMain["menuCasRun"].add_command(label = u"单项运行",command="fun2")
        self.mapMain["menuCasRun"].add_command(label = u"全部运行",command="fun3")
        
        self.mapMain["menuCasReport"].add_command(label = u"查看原始报告数",command="fun1")
        self.mapMain["menuCasReport"].add_command(label = u"生成html统计报告",command="fun2")
        self.mapMain["menuCasReport"].add_command(label = u"邮件发送html报告",command="fun3")
        
        self.mapMain["menuCasALM"].add_command(label = u"连接ALM/QC服务器",command="fun3")
        
        self.mapMain["menuCasHelp"].add_command(label = u"版本信息",command="fun3")    
        
        ### PanedWindow
        self.mapMain["panedWin"] = PanedWindow()
        self.mapMain["panedWin"].pack(side = "top",expand="yes",fill = "both",pady = 2,padx = "2m")
        self.mapMain["panedWin"].config(orient = "horizontal")
        self.mapMain["panedWin"].pack(side="top", expand = "yes", fill = "both", pady = 2, padx = "2m")    
        
        ### Frames
        # left frame
        self.mapMain["frame1"] = ttk.LabelFrame(self.mapMain["panedWin"], text = "Scripts")
        self.mapMain["leftListbox"] = Listbox(self.mapMain["frame1"],listvariable = "fun3")
        self.mapMain["leftXScrollbar"] = Scrollbar(self.mapMain["frame1"],orient = "horizontal", command = self.mapMain["leftListbox"].xview)
        self.mapMain["leftYScrollbar"] = Scrollbar(self.mapMain["frame1"],orient = "vertical", command = self.mapMain["leftListbox"].yview)
        self.mapMain["leftListbox"].config(xscrollcommand = self.mapMain["leftXScrollbar"].set, yscrollcommand = self.mapMain["leftYScrollbar"].set)
        self.mapMain["leftProgressbar"] = ttk.Progressbar(self.mapMain["frame1"],mode = "determinate")
         
        self.mapMain["leftProgressbar"].pack(side = "bottom",fill = "x")
        self.mapMain["leftXScrollbar"].pack(side = "bottom",fill = "x")
        self.mapMain["leftYScrollbar"].pack(side = "right",fill = "y")
        self.mapMain["leftListbox"].pack(fill = "both",expand = 1)
        self.mapMain["panedWin"].add(self.mapMain["frame1"])        
        
        # right frame
        self.mapMain["frame2"] = ttk.LabelFrame(self.mapMain["panedWin"],text = "Debugging And Output Info")
        self.mapMain["frame2"].columnconfigure(0,weight = 1)
        self.mapMain["frame2"].rowconfigure(0,weight = 1)
        self.mapMain["rightListboxUp"] = Listbox(self.mapMain["frame2"],listvariable = "fun3",height = 20)
        self.mapMain["rightXScrollbarUp"] = Scrollbar(self.mapMain["frame2"],orient = "horizontal", command = self.mapMain["rightListboxUp"].xview)
        self.mapMain["rightYScrollbarUp"] = Scrollbar(self.mapMain["frame2"],orient = "vertical", command = self.mapMain["rightListboxUp"].yview)
        self.mapMain["rightListboxUp"].config(xscrollcommand = self.mapMain["rightXScrollbarUp"].set, yscrollcommand = self.mapMain["rightYScrollbarUp"].set) 
        
        self.mapMain["rightListboxUp"].grid(row=0, column=0, sticky=NSEW)
        self.mapMain["rightYScrollbarUp"].grid(row=0, column=1, sticky=NSEW)
        self.mapMain["rightXScrollbarUp"].grid(row=1, column=0, sticky=NSEW)
        
        self.mapMain["rightListboxDown"] = Listbox(self.mapMain["frame2"],listvariable = "fun3",height = 20)
        self.mapMain["rightXScrollbarDown"] = Scrollbar(self.mapMain["frame2"],orient = "horizontal", command = self.mapMain["rightListboxDown"].xview)
        self.mapMain["rightYScrollbarDown"] = Scrollbar(self.mapMain["frame2"],orient = "vertical", command = self.mapMain["rightListboxDown"].yview)        
        self.mapMain["r_progressbar"] = ttk.Progressbar(self.mapMain["frame2"],mode = "determinate")
        self.mapMain["rightListboxDown"].config(xscrollcommand = self.mapMain["rightXScrollbarDown"].set, yscrollcommand = self.mapMain["rightYScrollbarDown"].set) 
         
        self.mapMain["rightListboxDown"].grid(row=2, column=0, sticky=N+S+E+W)
        self.mapMain["rightYScrollbarDown"].grid(row=2, column=1, sticky=N+S+E+W)
        self.mapMain["rightXScrollbarDown"].grid(row=3, column=0, sticky=N+S+E+W)
        self.mapMain["r_progressbar"].grid(row=4, column=0, sticky=N+S+E+W)
        self.mapMain["panedWin"].add(self.mapMain["frame2"])        
        
        

class PreferenceGUI():
    def __init__(self):
        self.mapPre = {"top":None,
                  "frame1":None,
                  "scriptLabel":None,
                  "scriptEntry":None,
                  "scriptButton":None,
                  "frame2":None,
                  "logLabel":None,
                  "logEntry":None,
                  "logButton":None,
                  "frame3":None,
                  "reportLabel":None,
                  "reportEntry":None,
                  "reportButton":None,
                  "frame4":None,
                  "scheduleRunLabel":None,
                  "scheduleRunAllEntry":None,
                  "scheduleRunAllButton":None,
                  }
        self.__preferenceGUI()
        self.__mainloop()
    
    def __mainloop(self):
        if self.mapPre.get("top"):
            self.mapPre.get("top").mainloop()
    
    def __valid_num(self,P):
        if P.isdigit() and len(P)<10:
            return True        
        return False
        
    def __invalid_msg(self):
        print "String should be integer and lenth <10"
        
    def __preferenceGUI(self):
        self.mapPre["top"] = Tk();
        self.mapPre["top"].title("Preference");self.mapPre["top"].geometry("510x260");self.mapPre["top"].resizable(0,0)
        
        self.mapPre["frame1"]  = ttk.LabelFrame(self.mapPre["top"],text="Autoload path")
        self.mapPre["scriptLabel"]  = Label(self.mapPre["frame1"],text = "Script load from:", width = 16, anchor = "w")
        self.mapPre["scriptEntry"]  = Entry(self.mapPre["frame1"], width = 40, state = "disable")
        self.mapPre["scriptButton"] = Button(self.mapPre["frame1"], text = "Select dir.")    
        self.mapPre["scriptLabel"].pack(side = "left")
        self.mapPre["scriptEntry"].pack(side = "left")
        self.mapPre["scriptButton"].pack(side = "left", pady = 5, padx = 10)
        self.mapPre["frame1"].pack(side = "top", expand = "no", fill = "both", pady = 2, padx = "2m")
            
        self.mapPre["frame2"]  = ttk.LabelFrame(self.mapPre["top"],text="Logs path")
        self.mapPre["logLabel"]  = Label(self.mapPre["frame2"],text = "Logs save to:", width = 16, anchor = "w")
        self.mapPre["logEntry"]  = Entry(self.mapPre["frame2"], width = 40, state = "disable")
        self.mapPre["logButton"] = Button(self.mapPre["frame2"], text = "Select dir.")    
        self.mapPre["logLabel"].pack(side = "left")
        self.mapPre["logEntry"].pack(side = "left")
        self.mapPre["logButton"].pack(side = "left", pady = 5, padx = 10)
        self.mapPre["frame2"].pack(side = "top", expand = "no", fill = "both", pady = 2, padx = "2m")
        
        self.mapPre["frame3"]  = ttk.LabelFrame(self.mapPre["top"],text="Report path")
        self.mapPre["reportLabel"]  = Label(self.mapPre["frame3"],text = "Analysis from:", width = 16, anchor = "w")
        self.mapPre["reportEntry"]  = Entry(self.mapPre["frame3"], width = 40, state = "disable")
        self.mapPre["reportButton"] = Button(self.mapPre["frame3"], text = "Select dir.")    
        self.mapPre["reportLabel"].pack(side = "left")
        self.mapPre["reportEntry"].pack(side = "left")
        self.mapPre["reportButton"].pack(side = "left", pady = 5, padx = 10)
        self.mapPre["frame3"].pack(side = "top", expand = "no", fill = "both", pady = 2, padx = "2m") 
    
        self.mapPre["frame4"]  = ttk.LabelFrame(self.mapPre["top"],text="Run time setup")
        self.mapPre["scheduleRunLabel"]  = Label(self.mapPre["frame4"],text = "Run after(minutes):", width = 16, anchor = "w")        
        self.mapPre["scheduleRunAllEntry"]  = Entry(self.mapPre["frame4"], width = 40, state = "normal",validate = "key")        
        self.mapPre["scheduleRunAllEntry"].config(vcmd = (self.mapPre["scheduleRunAllEntry"].register(self.__valid_num),'%P'),invalidcommand = (self.mapPre["scheduleRunAllEntry"].register(self.__invalid_msg)))
        
        self.mapPre["scheduleRunAllButton"] = Button(self.mapPre["frame4"], text = "ssss")    
        self.mapPre["scheduleRunLabel"].pack(side = "left")
        self.mapPre["scheduleRunAllEntry"].pack(side = "left")
        self.mapPre["scheduleRunAllButton"].pack(side = "left", pady = 5, padx = 10)
        self.mapPre["frame4"].pack(side = "top", expand = "no", fill = "both", pady = 2, padx = "2m")
        

if __name__ == "__main__":
#     UIMain()
    PreferenceGUI()
    
    
    
