#! python2
# -*- encoding: utf-8 -*-

from com import basic
from com.suite import Components
from com.basic import MSG, FileDilog
from com.ui import Window, Widget, Tkconstants, ROOT

g = {
     "list1_var": None,
     "tmp_key": [
            "INTF_CipherDES",
            "INTF_Contain",
            "INTF_DBExist",
            "INTF_DBNotExist",
            "INTF_DbContain",
            "INTF_DyData",
            "INTF_DyDataN",
            "INTF_Get",
            "INTF_GetCurrentResp",
            "INTF_Match",
            "INTF_NotJsonData",
            "INTF_NotNull",
            "INTF_SQLD",
            "INTF_SQLL",
            "INTF_Set",
            "INTF_UnCipherDES",
            "INTF_UpdateMemCache",
            "INTF_Upload",
            "INTF_UseCookie",
            "INTF_buf_string",
            "INTF_glob",
            "INTF_vars",
            "PAD_aischool",
            "PAD_checkProperty",
            "PAD_count",
            "PAD_drawable",
            "PAD_getPositionX",
            "PAD_getPositionY",
            "PAD_getProperty",
            "PAD_homePage",
            "PAD_id",
            "PAD_isExist",
            "PAD_isNotExist",
            "PAD_isNotNull",
            "PAD_isNull",
            "PAD_localSql",
            "PAD_move",
            "PAD_name",
            "PAD_notEqual",
            "PAD_onLineSql",
            "PAD_press",
            "PAD_pressBack",
            "PAD_pressXy",
            "PAD_pressXyLong",
            "PAD_prtSc",
            "PAD_pullDown",
            "PAD_pullLeft",
            "PAD_pullRigt",
            "PAD_pullUp",
            "PAD_set",
            "PAD_swipe",
            "PAD_tree",
            "PAD_type",
            "PAD_waitFor",
            "PC_Check",
            "PC_CheckProperty",
            "PC_Clear",
            "PC_ClearAndInput",
            "PC_Click",
            "PC_DataVerify",
            "PC_DataVerifyLocalDb",
            "PC_DataVerifyOnlineDb",
            "PC_DoubleClick",
            "PC_Drag",
            "PC_DragDown",
            "PC_DragLeft",
            "PC_DragRight",
            "PC_DragToTargetControl",
            "PC_DragUp",
            "PC_ErrorReback",
            "PC_ExplorerOpenSuccessAndClose",
            "PC_Find",
            "PC_FindById",
            "PC_FindByName",
            "PC_GetProperty",
            "PC_Input",
            "PC_IsExist",
            "PC_IsNotExist",
            "PC_Move",
            "PC_SaveAs",
            "PC_Screenshot",
            "PC_Scroll",
            "PC_SelectedIndex",
            "PC_SelectedItem",
            "PC_Set",
            "PC_SetFromDb",
            "PC_SetFromFile",
            "PC_SetFromLocalDb",
            "PC_SetFromOnlineDb",
            "PC_SetProperty",
            "PC_StartApp",
            "PC_StopApp",
            "PC_UnCheck",
            "PC_Upload",
            "PC_Wait",
            "PC_WaitForControlExist",
            "PC_WaitForControlNotExist",
            "PC_WaitForControlReady",
            "UI_CallCase",
            "UI_CheckCases",
            "WEB_Close",
            "WEB_Js",
            "WEB_Open",
            "WEB_Quit",
            "WEB_alt",
            "WEB_back",
            "WEB_backspace",
            "WEB_click",
            "WEB_click_attr",
            "WEB_click_text",
            "WEB_ctrl",
            "WEB_double_click",
            "WEB_drag_and_drop",
            "WEB_enter",
            "WEB_escape",
            "WEB_forward",
            "WEB_get",
            "WEB_max_window",
            "WEB_move_to_element",
            "WEB_open_browser",
            "WEB_open_new_window",
            "WEB_refresh",
            "WEB_right_click",
            "WEB_screen_shot",
            "WEB_scroll_bottom",
            "WEB_scroll_top",
            "WEB_set",
            "WEB_set_window",
            "WEB_space",
            "WEB_switch_to_frame",
            "WEB_switch_to_frame_out",
            "WEB_tab",
            "WEB_time_sleep",
            "WEB_type",
            "WEB_upload",
            "WEB_verify_attr",
            "WEB_verify_count",
            "WEB_verify_displayed",
            "WEB_verify_text",
            "WEB_verify_title",
            "WEB_verify_url",
            "WEB_wait",
            ],
     "tmp": "",
     }


Window.widg = ROOT
Window.Top("Demo tk", resizable_x=1, resizable_y=1)

frame1 = Widget.Labelframe(ROOT)
frame2 = Widget.Labelframe(ROOT)


text1 = Widget.Text(frame1)
text2 = Widget.Text(frame1)
    
list1 = Widget.Listbox(frame2)
x_scroll_1 = Widget.Scrollbar(frame2)
y_scroll_1 = Widget.Scrollbar(frame2)    
   

menu0 = Widget.Menu(ROOT)
ROOT.config(menu=menu0)
ROOT.option_add("*Menu.tearOff", 0)
menu_objs = {}
        
        
def set_selection(event):
    global g
    
    if event.char == ".":
        g["tmp"] = ""
        value = " ".join(g.get("tmp_key"))
        g["list1_var"].set(value)
        return    
    
    all_classify_key = list1.get("0", "end")
    all_key = []  
    for k in all_classify_key:
        all_key.append(k.split("_", 1)[1])
    
    g["tmp"] = g["tmp"] + event.char    
    cur = len(g["tmp"])
    
    indx = []
    for k in all_key:
        if len(k) < cur:
            continue
                    
        if k[0:cur] == g["tmp"]:
            indx.append(all_key.index(k))
    
    result =[] 
    for i in indx:
        result.append(all_classify_key[i])
        
    if indx:
        list1.delete("0", "end")
        g["list1_var"].set(" ".join(result))
        list1.selection_clear("0", "end")    
        list1.selection_set(0)
        list1.see(0)


def set_textformatter(event):    
    text2.delete("0.0", "end")
    tmp = text1.get("0.0", "end").split("\n")
    for i in range(len(tmp)):
        text2.insert("end", "%s.%s\n" % (i+1, tmp[i]))
    
  
def set_textkey(event):
    if list1.curselection():
        indx = list1.curselection()[0]
        value = list1.get(indx).split("_", 1)[1]
        filler = value[len(g["tmp"]):]        
        text1.insert("end", filler)


# UI construction
class Main(object):
    def __init__(self):
        self.__main()        
        basic.mainloop(ROOT, True)
    
    def __main(self):
        self.__get_menu_bar()
        self.__get_frame1()
        self.__get_frame2()
    
    def __get_menu_bar(self):
        menu_tree = [
                {u"文件": [u"打开", u"偏好设置"]},
                {u"运行": [u"停止", u"选中运行", u"全部运行"]},
                {u"报告": [u"查看报告", u"邮件发送报告"]},
                {u"关于": u"版本信息"}
            ]
        Components.GenerateMenu(menu0, menu_tree, menu_objs)
        
        def test_function(*args):
            msg = u"哈喽，Tkinter.\n"
            for i in args:
                print i, type(i)
                msg = msg + " " + i
            MSG.Showinfo("Hi My Demo", msg)
            
        def pop_ui(*args):
            Preference()
        
        node = menu_objs.get(u"关于")
        Components.RegisterMenu(node, u"版本信息", test_function, u"clicked 关于")
        
        node = menu_objs.get(u"运行")
        Components.RegisterMenu(node, u"停止", test_function, u"clicked 停止")
        Components.RegisterMenu(node, u"选中运行", test_function, u"clicked 选中运行")
        Components.RegisterMenu(node, u"全部运行", test_function, u"clicked 全部运行")
        
        node = menu_objs.get(u"报告")
        Components.RegisterMenu(node, u"查看报告", test_function, u"clicked 查看报告")
        Components.RegisterMenu(node, u"邮件发送报告", test_function, u"clicked 邮件发送报告")
        
        node = menu_objs.get(u"文件")
        Components.RegisterMenu(node, u"打开", test_function, u"clicked 打开")
        Components.RegisterMenu(node, u"偏好设置", pop_ui)

    def __get_frame1(self):    
        # text1.window_create("end", window = list1)
        # print basic.get_configuration_keys(frame1)    
    
        text1.insert(0.0, "switch to client automation")
        Window.widg = text1
        Window.Pack(expand = "yes", fill = "both", pady = 2, padx = "2m")
        Window.Config(width = 88,height = 10)
        Window.Bind('<Key>',set_selection)
        Window.Bind('<Key-Return>',set_textformatter)
        Window.Bind('<Key-Tab>',set_textkey)    
        
        Window.widg = text2
        Window.Pack(expand = "yes", fill = "both", pady = 2, padx = "2m")
        Window.Config(width = 88,height = 10)
        
        Window.widg = frame1
        Window.Pack(expand = "yes", side = "left", fill = "both", pady = 2, padx = "2m")
        Window.Config(text = "frame1")

    def __get_frame2(self):
        global g
        Window.widg = x_scroll_1
        Window.Config(orient = "horizontal", command= list1.xview)
        Window.Pack(side = "bottom", fill = "x")
        
        Window.widg = y_scroll_1
        Window.Config(orient = "vertical", command= list1.yview)
        Window.Pack(side = "right", fill = "y")
        
        Window.widg = list1
        Window.Config(selectmode = Tkconstants.SINGLE, xscrollcommand = x_scroll_1.set, yscrollcommand = y_scroll_1.set)
        g["list1_var"] = Window.ConfigVar("listvariable")
        Window.Pack(expand = "yes", fill = "both")
        
        Window.widg = frame2
        Window.Pack(expand = "yes", side = "right", fill = "both")
        Window.Config(text = "frame2")


class Preference:
    def __init__(self,loop=False):           
        self.__main()
        basic.mainloop(self.top, True)
            
    def __main(self):   
        self.top = Widget.NewTop()
        frame = Widget.Labelframe(self.top)
        label = Widget.Label(frame)
        entry = Widget.Entry(frame)
        button1 = Widget.Button(frame)
            
        Window.widg = self.top
        Window.Top("Preference settint")
        
        Window.widg = frame
        Window.Config(text=u"设置偏好")
        Window.Pack()
                
        Window.widg = label
        Window.Config(text = u"文件路径:")
        Window.Pack(side = "left")
        
        Window.widg = entry        
        self.__entry_var = Window.ConfigVar("textvariable")
        Window.Config(state=Tkconstants.DISABLED)
        Window.Pack(side = "left")
        
        Window.widg = button1
        command = basic.register_command(button1, self.__select_dir)
        Window.Config(text = u"打开文件",command = command)        
        Window.Pack(side = "left")
            
    def __select_dir(self):
        pth = FileDilog.Askdirectory()
        self.__entry_var.set(pth)


if __name__ == '__main__':
    Main()
