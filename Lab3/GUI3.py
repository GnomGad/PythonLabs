import wx
import os
import datetime
import re

class Window(wx.Frame):
    
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 400))
        self.control = wx.ListBox(self, style=wx.LB_SINGLE)
        self.statusbar = self.CreateStatusBar(2)
        self.statusbar.SetStatusWidths([-6, -4])
        self.Show(True)
        self.check_log()
        menu_file = wx.Menu() 
        open_item = menu_file.Append(wx.ID_OPEN, "Открыть", "Откройте файл")
        menu_log = wx.Menu()
        export_Item = menu_log.Append(wx.ID_SAVE, "Экспорт", "Экспорт файла")
        add_Item = menu_log.Append(wx.ID_ADD, "Добавить в лог", "Обновление лог файла")
        viewItem = menu_log.Append( wx.ID_ABOUT, "Просмотр", "Просмотреть лог файл")
        bar = wx.MenuBar()
        bar.Append(menu_file, "Файл")  
        bar.Append(menu_log, "Лог")
        self.SetMenuBar(bar)
        self.Bind(wx.EVT_MENU, self.open, open_item)
        self.Bind(wx.EVT_MENU, self.export, export_Item)
        self.Bind(wx.EVT_MENU, self.add_log, add_Item)
        self.Bind(wx.EVT_MENU, self.view, viewItem)

    def open(self, e):
        self.dirname = " "
        open_dialog = wx.FileDialog(self, "Выберите файл для открытия", self.dirname, " ", "*.*") 
        if open_dialog.ShowModal() == wx.ID_OK:  
            self.filename = open_dialog.GetFilename()  
            self.dirname = open_dialog.GetDirectory() 
            path = os.path.join(self.dirname, self.filename)
            reg = "(:(-)?[\)]+)|\){3,}"
            with open(path) as file:
                lst = file.readlines()
                self.control.Append("Файл " + path +" был обработан " + datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S") + ":")
                self.control.Append("")
                for i in range(len(lst)):
                    parser = re.search(reg,lst[i])
                    count =0
                    while parser!=None:
                        self.control.Append("Строка, "+str(i+1)+" позиция "+str(parser.regs[0][0]+count+1)+": найдено "+parser.group())
                        count+=parser.regs[0][1]
                        lst[i] = lst[i][parser.regs[0][1]:]
                        parser = re.search(reg,lst[i])
            self.control.Append("")
            size = str(os.path.getsize(path))[::-1]
            size = "".join([size[i]+" " if i%3 == 0 else size[i]  for i in range(len(size))][::-1])
            self.statusbar.SetStatusText("Обработан файл " + path)
            self.statusbar.SetStatusText(size + "байт", 1)

    def add_log(self, e):
        path = os.path.join(os.getcwd(), "script18.log")
        with open(path, "a") as file:
            for line in self.control.GetStrings():
                file.write(line + "\n")

    def export(self, e):
        self.dirname = " "
        open_dialog = wx.FileDialog(self, "Выберите файл для записи",self.dirname, " ", "*.*")  
        if open_dialog.ShowModal() == wx.ID_OK: 
            self.filename,self.dirname = open_dialog.GetFilename(), open_dialog.GetDirectory()  
            path = open_dialog.GetPath()
            with open(path, "w") as file:
                for line in self.control.GetStrings():
                    print(line)
                    file.write(line + "\n")

    def view(self, e):
        dialog = wx.MessageDialog(self, "Вы действительно хотите открыть лог? Данные последних поисков будут потеряны!", "Просмотр лога", wx.YES_NO)  
        if dialog.ShowModal() == wx.ID_YES:
            self.control.Clear()
            path = os.path.join(os.getcwd(), "script18.log")
            with open(path, "r") as file:
                self.control.AppendItems(file.readlines())
            self.statusbar.SetStatusText("Открыт лог")
            self.statusbar.SetStatusText("", 1)
        else:
            dialog.Destroy()

    def check_log(self):
        log_filename = "script18.log"
        path = os.path.join(os.getcwd(), log_filename)
        if not os.path.exists(path):
            dialog = wx.MessageDialog(self, "Файл лога не найден. Файл будет создан автоматически", "Проверка лога", wx.OK)  
            dialog.ShowModal() 

def main():
    app = wx.App()
    wnd = Window(None, "Мамин сыщик")
    app.MainLoop()

if __name__ == "__main__":
    main()
