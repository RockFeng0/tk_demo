# -*- encoding: utf-8 -*-
'''
Current module: pyrunner.ui.sc

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      pyrunner.ui.sc,v 1.0 2016年3月1日
    FROM:   2016年3月1日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

class Tmp:
    ''' 临时存储， 取出后，清空 '''
    tmp = None
    @classmethod
    def setValue(cls,value):
        cls.tmp = value
        
    @classmethod
    def getValue(cls):
        (tmp,cls.tmp) = (cls.tmp,None)
        return tmp
    
top = None

mapMain = {           
    "frame1" : None,
    "bt_webservice":None,
    "bt_web":None,
    "bt_mobile":None,
    "bt_agent":None,            
}

mapWebService = {
    "menus":{},
        
    "panedwin":None,
    "cases_frame":None,
    "cases_tree":None,
    "cases_scrollbar_x":None,
    "cases_scrollbar_y":None,
    "cases_progressbar":None,        
    
    "status_frame":None,
    "steps_frame":None,
    "steps_listbox":None,
    "steps_scrollbar_x":None,
    "steps_scrollbar_y":None,    
    
    "dataSource_frame":None,
    "dataSource_listbox":None,
    "dataSource_scrollbar_x":None,
    "dataSource_scrollbar_y":None,    
    
    "console_frame":None,
    "console_listbox":None,
    "console_scrollbar_x":None,
    "console_scrollbar_y":None,
    "console_progressbar":None,
    
    "data_cases_tree":""
}

mapWebServicePreference = {
    "top":None,
    
    "frame1":None,
    "project_label":None,
    "project_entry":None,
    "project_entry_variable":None,
    "project_button":None,
        
    "frame2":None,
    "schedule_run_label":None,
    "schedule_run_entry":None,
    "schedule_run_entry_variable":None,
    "schedule_run_button":None,
    
    "project_entry_text":r"D:\auto\python\app-autoApp\demoProject\data",#d:/auto/autoVerify/data
    "schedule_run_entry_text":0,
    "schedule_run_entry_state":"normal",    
    "schedule_run_button_text":"Setup ok.",
            
    "data_autorunn_timmer":None,                     
}

mapWebService_back = {
    "menus":{},
        
    "panedwin":None,
    "cases_frame":None,
    "cases_listbox":None,
    "cases_scrollbar_x":None,
    "cases_scrollbar_y":None,
    "cases_progressbar":None,        
    
    "status_frame":None,
    "steps_frame":None,
    "steps_listbox":None,
    "steps_scrollbar_x":None,
    "steps_scrollbar_y":None,    
    
    "dataSource_frame":None,
    "dataSource_listbox":None,
    "dataSource_scrollbar_x":None,
    "dataSource_scrollbar_y":None,    
    
    "console_frame":None,
    "console_listbox":None,
    "console_scrollbar_x":None,
    "console_scrollbar_y":None,
    "console_progressbar":None,      
}





