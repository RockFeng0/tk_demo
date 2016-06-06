# -*- encoding: utf-8 -*-
'''
Current module: com.basic

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      com.basic,v 1.0 2016年6月6日
    FROM:   2016年6月6日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

import tkMessageBox
class MSG:
    
    @classmethod
    def Showinfo(cls,title=None, message=None, **options):
        '''Sample usage:
            tkMessageBox.showinfo("Spam", "Egg Information")
        '''
        tkMessageBox.showinfo(title,message,**options)
    
    @classmethod
    def Showwarning(cls,title=None, message=None, **options):
        '''Sample usage:
            tkMessageBox.showwarning("Spam", "Egg Warning")
        '''
        tkMessageBox.showwarning(title,message,**options)
    
    @classmethod
    def Showerror(cls,title=None, message=None, **options):
        '''Sample usage:
            tkMessageBox.showerror("Spam", "Egg Alert")
        '''
        tkMessageBox.showerror(title,message,**options)
    
    @classmethod
    def Askquestion(cls,title=None, message=None, **options):
        '''Sample usage:
            tkMessageBox.askquestion("Spam", "Egg Question?")
        '''
        tkMessageBox.askquestion(title,message,**options)
    
    @classmethod    
    def Askokcancel(cls,title=None, message=None, **options):
        '''Sample usage:
            tkMessageBox.askokcancel("Spam", "Egg Proceed?")
        '''
        tkMessageBox.askokcancel(title,message,**options)
    
    @classmethod    
    def Askyesno(cls,title=None, message=None, **options):
        '''Sample usage:
            tkMessageBox.askyesno("Spam", "Egg Got it?")
        '''
        tkMessageBox.askyesno(title,message,**options)
    
    @classmethod
    def Askyesnocancel(cls,title=None, message=None, **options):
        '''Sample usage:
            tkMessageBox.askyesnocancel("Spam", "Want it?")
        '''
        tkMessageBox.askyesnocancel(title,message,**options)
    
    @classmethod
    def Askretrycancel(cls,title=None, message=None, **options):
        '''Sample usage:
            tkMessageBox.askretrycancel("Spam", "Try again?")
        '''
        tkMessageBox.askretrycancel(title,message,**options)


import tkFileDialog
class FileDilog:
    '''
        options (all have default values):
        
        - defaultextension: added to filename if not explicitly given
        
        - filetypes: sequence of (label, pattern) tuples.  the same pattern
          may occur with several patterns.  use "*" as pattern to indicate
          all files.
        
        - initialdir: initial directory.  preserved by dialog instance.
        
        - initialfile: initial file (ignored by the open dialog).  preserved
          by dialog instance.
        
        - parent: which window to place the dialog on top of
        
        - title: dialog title
        
        - multiple: if true user may select more than one file
        
        options for the directory chooser:
        
        - initialdir, parent, title: see above
        
        - mustexist: if true, user must pick an existing directory
    '''
    
    @classmethod
    def Askopenfilename(cls,**options):
        "Ask for a filename to open"
        tkFileDialog.askopenfilename(**options)
        
    @classmethod
    def Asksaveasfilename(cls,**options):
        "Ask for a filename to save as"
        tkFileDialog.asksaveasfilename(**options)

    @classmethod
    def Askopenfilenames(cls,**options):
        """Ask for multiple filenames and return the open file
        objects
    
        returns a list of open file objects or an empty list if
        cancel selected
        """
        tkFileDialog.askopenfilenames(**options)
        
        
        
        
