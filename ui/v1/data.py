# -*- encoding: utf-8 -*-
'''
Current module: pyrunner.ui.data

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      pyrunner.ui.data,v 1.0 2016年3月7日
    FROM:   2016年3月7日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

source = None

def getWebServiceTreeData(xlsfile):
    from pyrunner.common import p_common
    result = []
    from demoCode.twsm_dpc import TwsmDPC
    import sys
    reload(sys)
    getattr(sys, "setdefaultencoding")("utf-8")
    try:
        source = TwsmDPC(xlsfile).getCases()
        caseids = source.keys()
        for caseid in caseids:
            tree_leaf = "%s[%s]" %(caseid,unicode(source[caseid]["description"]))
            print tree_leaf
            result.append(tree_leaf)
        return sorted(result)
    except Exception,e:
        print "oh No:",e
        return

if __name__ == "__main__":
    print getWebServiceTreeData(r"D:\auto\python\app-autoApp\demoProject\data\Data_Verify.xlsx")
    