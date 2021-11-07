#! python2
# -*- encoding: utf-8 -*-

from com import basic
from com.basic import MSG, FileDilog
from com.ui import Window, Widget, ROOT, Tkconstants
from com.suite import Components

TITLE = u"AiTest自动化测试用例编写工具"

MENUS = [
         {u"执行": [u"运行当前"]},
         {u"导航": [u"接口测试"]},
         ]

Window.widg = ROOT
Window.Top(TITLE, geometry="917x580+179+130", resizable_x=1, resizable_y=1)

menubar = Widget.Menu(ROOT)
Window.Config(menu=menubar)
ROOT.option_add("*Menu.tearOff", 0)


class Menu:
    
    def __init__(self, loop=False):
        self.__main()
        self.__navigator_ui = AiTest()
        basic.mainloop(ROOT, loop=loop)

    def __main(self):
        self.menus = {}
        Components.GenerateMenu(menubar, MENUS, self.menus)
        self.__set_menus_command()

    def __set_menus_command(self):
        node = self.menus.get(u"导航")
        Components.RegisterMenu(node, u"接口测试", self.__navigator, u"clicked 接口测试")
        node = self.menus.get(u"执行")
        Components.RegisterMenu(node, u"运行当前", self.__runner, u"clicked 运行当前")

    def __navigator(self, *args):
        msg = u" 将会重置下面的控件。"
        MSG.Showinfo("usage demo 2", args[0] + msg)
        self.__clean_ui()
        self.__navigator_ui = AiTest()

    def __runner(self, *args):
        msg = u" 打印控台日志"
        MSG.Showinfo("usage demo 2", args[0] + msg)
        self.__navigator_ui.console_output.set(u"运行日志 balabala...")

    def __clean_ui(self):
        if self.__navigator_ui:
            self.__navigator_ui.destroy()
            self.__navigator_ui = None


class AiTest:

    def __init__(self):
        self.__main()

    def __main(self):
        self.frame1         = Widget.Labelframe(ROOT)
        self.frame2         = Widget.Labelframe(ROOT)

        label_caseid        = Widget.Label(self.frame1)
        entry_caseid        = Widget.Entry(self.frame1)

        label_steps         = Widget.Label(self.frame1)
        text_steps          = Widget.Text(self.frame1)

        label_des_name      = Widget.Label(self.frame1)
        text_des_name       = Widget.Text(self.frame1)

        label_precommand    = Widget.Label(self.frame1)
        text_precommand     = Widget.Text(self.frame1)

        label_head          = Widget.Label(self.frame1)
        text_head           = Widget.Text(self.frame1)

        label_data          = Widget.Label(self.frame1)
        text_data           = Widget.Text(self.frame1)

        label_postcommand   = Widget.Label(self.frame1)
        text_postcommand    = Widget.Text(self.frame1)

        label_verify        = Widget.Label(self.frame1)
        text_verify         = Widget.Text(self.frame1)

        label_casetype      = Widget.Label(self.frame1)
        text_casetype       = Widget.Entry(self.frame1)

        label_author        = Widget.Label(self.frame1)
        text_author         = Widget.Entry(self.frame1)

        list_control        = Widget.Listbox(self.frame2)

        text_conf = {"width": 40, "height": 5}
        entry_conf = {"width": 40}
        # frame1
        Window.widg = label_caseid
        Window.Config(text="TestCaseID:")
        Window.Grid(row=0, column=0, sticky="w")
        Window.widg = entry_caseid
        Window.Config(**entry_conf)
        Window.Grid(row=0, column=1, sticky="EW")

        Window.widg = label_casetype
        Window.Config(text="CaseType:")
        Window.Grid(row=1, column=0, sticky="w")
        Window.widg = text_casetype
        Window.Config(**entry_conf)
        Window.Grid(row=1, column=1, sticky="EW")

        Window.widg = label_author
        Window.Config(text="Tester:")
        Window.Grid(row=2, column=0, sticky="w")
        Window.widg = text_author
        Window.Config(**entry_conf)
        Window.Grid(row=2, column=1, sticky="EW")

        Window.widg = label_steps
        Window.Config(text="Steps:")
        Window.Grid(row=3, column=0, sticky="w")
        Window.widg = text_steps
        Window.Config(**text_conf)
        Window.Grid(row=3, column=1, sticky="EW")

        Window.widg = label_des_name
        Window.Config(text="Description:")
        Window.Grid(row=4, column=0, sticky="w")
        Window.widg = text_des_name
        Window.Config(**text_conf)
        Window.Grid(row=4, column=1, sticky="EW")

        Window.widg = label_precommand
        Window.Config(text="PreCommand:")
        Window.Grid(row=5, column=0, sticky="w")
        Window.widg = text_precommand
        Window.Config(**text_conf)
        Window.Grid(row=5, column=1, sticky="EW")

        Window.widg = label_head
        Window.Config(text="Head:")
        Window.Grid(row=6, column=0, sticky="w")
        Window.widg = text_head
        Window.Config(**text_conf)
        Window.Grid(row=6, column=1, sticky="EW")

        Window.widg = label_data
        Window.Config(text="Data:")
        Window.Grid(row=7, column=0, sticky="w")
        Window.widg = text_data
        Window.Config(**text_conf)
        Window.Grid(row=7, column=1, sticky="EW")

        Window.widg = label_postcommand
        Window.Config(text="PostCommand:")
        Window.Grid(row=8, column=0, sticky="w")
        Window.widg = text_postcommand
        Window.Config(**text_conf)
        Window.Grid(row=8, column=1, sticky="EW")

        Window.widg = label_verify
        Window.Config(text="Verify:")
        Window.Grid(row=9, column=0, sticky="w")
        Window.widg = text_verify
        Window.Config(**text_conf)
        Window.Grid(row=9, column=1, sticky="EW")

        Window.widg = self.frame1
        Window.Config(text="Part1")
        Window.Pack(side="left", fill=Tkconstants.X)

        # frame2
        Window.widg = list_control
        self.console_output = Window.ConfigVar("listvariable")
        Window.Pack(side="top", fill=Tkconstants.BOTH, expand="yes")

        Window.widg = self.frame2
        Window.Config(text="Part3")
        Window.Pack(side="left", fill=Tkconstants.BOTH, expand=Tkconstants.YES)

    def destroy(self):
        self.frame1.destroy()
        self.frame2.destroy()


if __name__ == "__main__":
    Menu(loop=True)



