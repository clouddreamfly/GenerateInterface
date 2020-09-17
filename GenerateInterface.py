#!/usr/bin/python
#-*-coding:utf8-*-



import os
import sys
import uuid
import Tkinter
import tkMessageBox



class GenerateGuid:
    
    @staticmethod
    def generate1(interface):

	guid1=uuid.uuid4()
	guid2=uuid.uuid4()
	guid11=str(guid1).split('-')
	guid21=str(guid2).split('-')
	guid12=[guid11[0], guid11[1], guid11[2], guid11[3][0:2], guid11[3][2:4], guid11[4][0:2], guid11[4][2:4], guid11[4][4:6], guid11[4][6:8], guid11[4][8:10], guid11[4][10:12] ]
	guid22=[guid21[0], guid21[1], guid21[2], guid21[3][0:2], guid21[3][2:4], guid21[4][0:2], guid21[4][2:4], guid21[4][4:6], guid21[4][6:8], guid21[4][8:10], guid21[4][10:12] ]        

	content_format=u'' \
	+ u"////////////////////////////////////////////////////////////////////////////\n"  \
	+ u"\n" \
	+ u"//定义接口标识\n" \
	+ u"// IID { %s }\n" \
	+ u"// IID { %s }\n" \
	+ u"#ifdef _UNICODE\n" \
	+ u"\t#define VER_%s INTERFACE_VERSION(1, 1)\n" \
	+ u"\tstatic const GUID IID_%s = { 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s };\n" \
	+ u"#else\n" \
	+ u"\t#define VER_%s INTERFACE_VERSION(1, 1)\n" \
	+ u"\tstatic const GUID IID_%s = { 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s };\n" \
	+ u"#endif"

	content = content_format % (str(guid1).upper(), str(guid2).upper(), 
	        interface, interface, guid12[0], guid12[1], guid12[2], guid12[3], guid12[4], guid12[5], guid12[6], guid12[7], guid12[8], guid12[9], guid12[10],
	        interface, interface, guid22[0], guid22[1], guid22[2], guid22[3], guid22[4], guid22[5], guid22[6], guid22[7], guid22[8], guid22[9], guid22[10])

	return content
     
    
    @staticmethod
    def generate2(interface):
        
        guid1=uuid.uuid4()
        guid2=uuid.uuid4()
        guid11=str(guid1).split('-')
        guid21=str(guid2).split('-')
        guid12=[guid11[0], guid11[1], guid11[2], guid11[3][0:2], guid11[3][2:4], guid11[4][0:2], guid11[4][2:4], guid11[4][4:6], guid11[4][6:8], guid11[4][8:10], guid11[4][10:12] ]
        guid22=[guid21[0], guid21[1], guid21[2], guid21[3][0:2], guid21[3][2:4], guid21[4][0:2], guid21[4][2:4], guid21[4][4:6], guid21[4][6:8], guid21[4][8:10], guid21[4][10:12] ]        
    
        content_format=u'' \
        + u"////////////////////////////////////////////////////////////////////////////\n"  \
        + u"\n" \
        + u"//定义接口标识\n" \
        + u"// IID { %s }\n" \
        + u"// IID { %s }\n" \
        + u"#ifdef _UNICODE\n" \
        + u"\tstatic const GUID %s_IID = { 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s };\n" \
        + u"#else\n" \
        + u"\tstatic const GUID %s_IID = { 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s };\n" \
        + u"#endif" 
        
        content = content_format % (str(guid1).upper(), str(guid2).upper(), 
                 interface, guid12[0], guid12[1], guid12[2], guid12[3], guid12[4], guid12[5], guid12[6], guid12[7], guid12[8], guid12[9], guid12[10],
                 interface, guid22[0], guid22[1], guid22[2], guid22[3], guid22[4], guid22[5], guid22[6], guid22[7], guid22[8], guid22[9], guid22[10])

        return content

    

class GenerateInterface:
    
    @staticmethod
    def generate1(clsid, interface, parent=None):

	if clsid == "interface":
	    
	    content_format=u'' \
	    + u"//接口\n" \
	    + u"%s %s : public %s\n" \
	    + u"{\n" \
	    + u"public:\n" \
	    + u"\n" \
	    + u"};\n" \
	    + u"\n" 
	    
	    content = content_format % (clsid, interface, parent or u"IUnknownEx")
	    
	elif clsid == "class":
	    
	    content_format=u'' \
	    + u"//类\n" \
	    + u"%s %s%s\n" \
	    + u"{\n" \
	    + u"public:\n" \
	    + u"\t//构造函数\n" \
	    + u"\t%s() { }\n" \
	    + u"\t//析构函数\n" \
	    + u"\tvirtual ~%s() { }\n" \
	    + u"\n" \
	    + u"};\n" \
	    + u"\n" 
	    
	    parent = parent and u" : public %s"%(parent)
	    content = content_format % (clsid, interface, parent or u"", interface, interface)
	    
	else:
	    content_format=u'' \
	    + u"//结构\n" \
	    + u"%s %s%s\n" \
	    + u"{\n" \
	    + u"\n" \
	    + u"};\n" \
	    + u"\n" 
	    
	    parent = parent and u" : public %s"%(parent)
	    content = content_format % (clsid, interface, parent or u"")

	return content

    @staticmethod
    def generate2(clsid, interface, parent=None):

	if clsid == "interface":
	    
	    content_format=u'' \
	    + u"//接口\n" \
	    + u"%s %s : public %s\n" \
	    + u"{\n" \
	    + u"public:\n" \
	    + u"\n" \
	    + u"};\n" \
	    + u"\n" 
	    
	    content = content_format % (clsid, interface, parent or u"base::IUnknown")
	    
	elif clsid == "class":
	    
	    content_format=u'' \
	    + u"//类\n" \
	    + u"%s %s%s\n" \
	    + u"{\n" \
	    + u"public:\n" \
	    + u"\t//构造函数\n" \
	    + u"\t%s() { }\n" \
	    + u"\t//析构函数\n" \
	    + u"\tvirtual ~%s() { }\n" \
	    + u"\n" \
	    + u"};\n" \
	    + u"\n" 
	    
	    parent = parent and u" : public %s"%(parent)
	    content = content_format % (clsid, interface, parent or u"", interface, interface)
	    
	else:
	    content_format=u'' \
	    + u"//结构\n" \
	    + u"%s %s%s\n" \
	    + u"{\n" \
	    + u"\n" \
	    + u"};\n" \
	    + u"\n" 
	    
	    parent = parent and u" : public %s"%(parent)
	    content = content_format % (clsid, interface, parent or u"")

	return content    
    
class GenerateInterfaceEx:
    
    @staticmethod
    def generate1(clsid, interface, parent=None):

	guid1=uuid.uuid4()
	guid2=uuid.uuid4()
	guid11=str(guid1).split('-')
	guid21=str(guid2).split('-')
	guid12=[guid11[0], guid11[1], guid11[2], guid11[3][0:2], guid11[3][2:4], guid11[4][0:2], guid11[4][2:4], guid11[4][4:6], guid11[4][6:8], guid11[4][8:10], guid11[4][10:12] ]
	guid22=[guid21[0], guid21[1], guid21[2], guid21[3][0:2], guid21[3][2:4], guid21[4][0:2], guid21[4][2:4], guid21[4][4:6], guid21[4][6:8], guid21[4][8:10], guid21[4][10:12] ]        

	content_format=u'' \
	+ u"////////////////////////////////////////////////////////////////////////////\n"  \
	+ u"\n" \
	+ u"//定义接口标识\n" \
	+ u"// IID { %s }\n" \
	+ u"// IID { %s }\n" \
	+ u"#ifdef _UNICODE\n" \
	+ u"\t#define VER_%s INTERFACE_VERSION(1, 1)\n" \
	+ u"\tstatic const GUID IID_%s = { 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s };\n" \
	+ u"#else\n" \
	+ u"\t#define VER_%s INTERFACE_VERSION(1, 1)\n" \
	+ u"\tstatic const GUID IID_%s = { 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s };\n" \
	+ u"#endif\n" \
	+ u"\n" \
	+ u"//接口\n" \
	+ u"%s %s : public %s\n" \
	+ u"{\n" \
	+ u"public:\n" \
	+ u"\n" \
	+ u"};\n" \
	+ u"\n" 

	content = content_format % (str(guid1).upper(), str(guid2).upper(), 
	                            interface, interface, guid12[0], guid12[1], guid12[2], guid12[3], guid12[4], guid12[5], guid12[6], guid12[7], guid12[8], guid12[9], guid12[10],
	         interface, interface, guid22[0], guid22[1], guid22[2], guid22[3], guid22[4], guid22[5], guid22[6], guid22[7], guid22[8], guid22[9], guid22[10],
	         clsid, interface, parent or u"IUnknownEx")

	return content

    @staticmethod
    def generate2(clsid, interface, parent=None):
        
        guid1=uuid.uuid4()
        guid2=uuid.uuid4()
        guid11=str(guid1).split('-')
        guid21=str(guid2).split('-')
        guid12=[guid11[0], guid11[1], guid11[2], guid11[3][0:2], guid11[3][2:4], guid11[4][0:2], guid11[4][2:4], guid11[4][4:6], guid11[4][6:8], guid11[4][8:10], guid11[4][10:12] ]
        guid22=[guid21[0], guid21[1], guid21[2], guid21[3][0:2], guid21[3][2:4], guid21[4][0:2], guid21[4][2:4], guid21[4][4:6], guid21[4][6:8], guid21[4][8:10], guid21[4][10:12] ]        
    
        content_format=u'' \
        + u"////////////////////////////////////////////////////////////////////////////\n"  \
        + u"\n" \
        + u"//定义接口标识\n" \
        + u"// IID { %s }\n" \
        + u"// IID { %s }\n" \
        + u"#ifdef _UNICODE\n" \
        + u"\tstatic const GUID %s_IID = { 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s };\n" \
        + u"#else\n" \
        + u"\tstatic const GUID %s_IID = { 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s, 0x%s };\n" \
        + u"#endif\n" \
        + u"\n" \
        + u"//接口\n" \
        + u"%s %s : public %s\n" \
        + u"{\n" \
        + u"public:\n" \
        + u"\n" \
        + u"};\n" \
        + u"\n" 
        
        content = content_format % (str(guid1).upper(), str(guid2).upper(), 
                 interface, guid12[0], guid12[1], guid12[2], guid12[3], guid12[4], guid12[5], guid12[6], guid12[7], guid12[8], guid12[9], guid12[10],
                 interface, guid22[0], guid22[1], guid22[2], guid22[3], guid22[4], guid22[5], guid22[6], guid22[7], guid22[8], guid22[9], guid22[10],
                 clsid, interface, parent or u"base::IUnknown")

        return content   


class MainDialog:
    
    def __init__(self):
        
        self.dialog = dialog = Tkinter.Tk()
        dialog.title("接口生成")
        dialog.geometry("640x480")
        #dialog.resizable(0,0)
        dialog.minsize(640, 480)
        
        paned = Tkinter.PanedWindow(dialog, orient=Tkinter.VERTICAL) 
        paned.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=Tkinter.YES)  
        
        frame = Tkinter.Frame(paned)  
        frame.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=Tkinter.YES)
        frame_sb_x = Tkinter.Scrollbar(frame, orient=Tkinter.HORIZONTAL)
        frame_sb_y = Tkinter.Scrollbar(frame, orient=Tkinter.VERTICAL)
        frame_sb_x.pack(side=Tkinter.BOTTOM, fill=Tkinter.X)  
        frame_sb_y.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)  
        self.txt_content = txt_content = Tkinter.Text(frame, state=Tkinter.DISABLED, wrap=Tkinter.NONE)
        txt_content.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=Tkinter.YES)
        txt_content.configure(xscrollcommand = frame_sb_x.set)
        txt_content.configure(yscrollcommand = frame_sb_y.set)
        frame_sb_x.configure(command = txt_content.xview)  
        frame_sb_y.configure(command = txt_content.yview)   
    
        frame1 = Tkinter.Frame(paned)
        frame1.pack(side=Tkinter.TOP)
        
        lab_inerface_clsid = Tkinter.Label(frame1, text = "接口标识符:")
        lab_inerface_clsid.pack(side=Tkinter.LEFT, padx = 0, pady = 10)
        self.txt_inerface_clsid = Tkinter.StringVar(frame1, value="interface")
        self.txt_inerface_menu = Tkinter.OptionMenu(frame1, self.txt_inerface_clsid, "interface", "class", "struct")
        self.txt_inerface_menu.pack(side=Tkinter.LEFT, padx = 4, pady = 10)        
        
        lab_inerface_name = Tkinter.Label(frame1, text = "接口名称:")
        lab_inerface_name.pack(side=Tkinter.LEFT, padx = 0, pady = 10)
        self.txt_inerface_name = Tkinter.Entry(frame1)
        self.txt_inerface_name.pack(side=Tkinter.LEFT, padx = 4, pady = 10)
        
        lab_parent_inerface_name = Tkinter.Label(frame1, text = "父类接口名称:")
        lab_parent_inerface_name.pack(side=Tkinter.LEFT, padx = 0, pady = 10)        
        self.txt_parent_inerface_name = Tkinter.Entry(frame1)
        self.txt_parent_inerface_name.pack(side=Tkinter.LEFT, padx = 4,  pady = 10)   

        frame2 = Tkinter.Frame(paned)
        frame2.pack()
	
	self.radio_value1 = Tkinter.IntVar()
	btn_generate_old = Tkinter.Radiobutton(frame2, text = "旧接口", variable=self.radio_value1, value=1, width = 6, height = 1)
	btn_generate_new = Tkinter.Radiobutton(frame2, text = "新接口", variable=self.radio_value1, value=2, width = 6, height = 1)
	btn_generate_old.pack(side=Tkinter.LEFT, padx = 2, pady = 2)
	btn_generate_new.pack(side=Tkinter.LEFT, padx = 2, pady = 2)
	btn_generate_new.select()	
        
        self.radio_value2 = Tkinter.IntVar()
        btn_generate_all = Tkinter.Radiobutton(frame2, text = "全部", variable=self.radio_value2, value=1, width = 6, height = 1)
	btn_generate_define = Tkinter.Radiobutton(frame2, text = "定义", variable=self.radio_value2, value=2, width = 6, height = 1)
	btn_generate_guid = Tkinter.Radiobutton(frame2, text = "GUID", variable=self.radio_value2, value=3, width = 6, height = 1)
        btn_generate_all.pack(side=Tkinter.LEFT, padx = 2, pady = 2)
	btn_generate_define.pack(side=Tkinter.LEFT, padx = 2, pady = 2)
	btn_generate_guid.pack(side=Tkinter.LEFT, padx = 2, pady = 2)
	btn_generate_all.select()
        
        frame3 = Tkinter.Frame(paned)
        frame3.pack(side=Tkinter.BOTTOM)
        
        btn_generate = Tkinter.Button(frame3, text = "生成", width = 16, height = 2, command = self.OnBtnGenerate)
        btn_copy = Tkinter.Button(frame3, text = "复制", width = 16, height = 2, command = self.OnBtnCopy)
        btn_generate.pack(side=Tkinter.LEFT, padx = 10, pady = 10)
        btn_copy.pack(side=Tkinter.LEFT, padx = 10, pady = 10)
		
		
    def OnBtnGenerate(self):
        
        interface_clsid = self.txt_inerface_clsid.get()
        inerface_name = self.txt_inerface_name.get()
	if not inerface_name:
	    if interface_clsid == u"interface": inerface_name = u"IClassName"
	    if interface_clsid == u"class": inerface_name = u"ClassName"
	    if interface_clsid == u"struct": inerface_name = u"StructName"
	
        parent_inerface_name = self.txt_parent_inerface_name.get() or None
        self.txt_inerface_name.delete(0, Tkinter.END)
        self.txt_inerface_name.insert(Tkinter.END, inerface_name)
	
	if self.radio_value1.get() == 1:
	    if self.radio_value2.get() == 1:
		content = GenerateInterfaceEx.generate1(interface_clsid, inerface_name, parent_inerface_name)
	    elif self.radio_value2.get() == 2:
		content = GenerateInterface.generate1(interface_clsid, inerface_name, parent_inerface_name)		
	    else:
		content = GenerateGuid.generate1(inerface_name)      
	else:
	    if self.radio_value2.get() == 1:
		content = GenerateInterfaceEx.generate2(interface_clsid, inerface_name, parent_inerface_name)
	    elif self.radio_value2.get() == 2:
		content = GenerateInterface.generate2(interface_clsid, inerface_name, parent_inerface_name)
	    else:
		content = GenerateGuid.generate2(inerface_name)
        
        self.txt_content.configure(state = Tkinter.NORMAL)
        self.txt_content.delete(1.0, Tkinter.END)
        self.txt_content.insert(Tkinter.END, content)
        self.txt_content.configure(state = Tkinter.DISABLED)
    
    def OnBtnCopy(self):
        
        self.dialog.clipboard_clear()
        self.dialog.clipboard_append(self.txt_content.get(1.0, Tkinter.END))
        
        
    def runloop(self):
        
        self.dialog.mainloop()


def main():
    
    dialog = MainDialog()
    dialog.runloop()

    
if __name__ == "__main__":
    main()

