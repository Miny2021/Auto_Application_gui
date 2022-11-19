import tkinter as tk
import tkinter.messagebox as messagebox
import _thread
import os
import time as module_time
from tqdm import tqdm
import random
# 函数部分

def main():
    def get_user_input():
        """获取用户输入并判断"""
        cmd = command.get()# 获取用户输入
        command.delete('0','end')# 清空输入框
        if cmd == 'about': # 如果用户输入了about
            outputtext.set('Run to about')# 输入框显示Run to about
            about = tk.Tk()# 定义about窗口
            about.title('关于 - 自动程序')# 定义about窗口的标题
            # 定义Label文本框
            t = tk.Label(
                about,
                text = 'Made by AGS\nabout关于\nhelp查看更多指令')
            t.pack()
            #显示窗口
            about.mainloop()
        if cmd == 'help':
            outputtext.set('Run to help')
            helps = tk.Tk()
            helps.title('帮助 - 自动程序')
            texts =  'help打开帮助'
            texts += '\nabout打开关于'
            texts += '\ntimer close exes打开 \'定时关闭程序\''
            texts += '\nmyself打开第二个主界面'
            texts += '\nquitcmd cmd脱离程序'
            texts += '\n其他功能尽情期待'
            t = tk.Label(
                helps,
                text = texts)
            t.pack()
            helps.mainloop()
        if cmd == 'timer close exes':
            outputtext.set('Run to TIMER_CLOSE_EXES')
            def do_time():
                times = time.get()
                try:
                    times = int(times)
                except TypeError and ValueError:
                    pass
                else:
                    for i in tqdm(range(0,times)):
                        module_time.sleep(1)
                    while os.system(f'taskkill /f /im {name.get()}') == 0:
                        pass
            def run_do_time():
                _thread.start_new_thread(do_time,())
                        
            timer_ce = tk.Tk()
            timer_ce.title('定时关闭程序 - 自动程序')
            timer_ce.geometry('300x118')
            tk.Label(
                timer_ce,
                width = 300,
                height = 1,
                text = '进程名称(如taskmgr.exe为任务管理器)').pack()
            name = tk.Entry(
                timer_ce,
                width = 300)
            name.pack()
            tk.Label(
                timer_ce,
                width = 300,
                height = 1,
                text = '几秒钟后关闭').pack()
            time = tk.Entry(
                timer_ce,
                width = 300)
            time.pack()
            timer_cetext = tk.StringVar()
            runbutton = tk.Button(
                timer_ce,
                width = 300,
                text = '运行',
                command = run_do_time)
            runbutton.pack()
            timer_ce.mainloop()
        if cmd == 'quitcmd':
            outputtext.set('Run to quitcmd.')
            def quit():
                os.system("taskkill /f /im taskkill.exe")
            warningtext ='\n脱离的好处:'
            warningtext+='\n- 几乎没有'
            warningtext+='\n脱离的坏处:'
            warningtext+='\n- \'定时关闭程序\'模块失效'
            warningtext+='\n- (几率小)可能将某些东西搞异常'
            warningtext+='\n如果执行脱离程序后cmd没有关闭，但是卡住了，就直接关闭cmd'
            warningtext+='\n如果不生效，请执行多次(只在配置好的电脑上出现)'
            warningtext+='\n如果出现"启动程序失败"纯属正常现象（暗示脱离成功）'
            if messagebox.askokcancel("脱离程序",warningtext):
                for i in range(100):
                    _thread.start_new_thread(quit,())
        else:
            outputtext.set('Unknow command.\nplease input \'help\'to looking for commands.')
    
    def run_get_user_input():
        _thread.start_new_thread(get_user_input,())
    # 定义主窗口
    window = tk.Tk()
    window.title('主界面 - 自动程序')
    window.geometry('320x180')
    
    # 代码部分
    # 输入框
    command = tk.Entry(
        window,
        width = 300)
    command.pack()
    # 运行按钮
    g_input=tk.Button(
        window,
        width = 300,
        height = 1,
        text = "运行",
        command = run_get_user_input)
    g_input.pack()
    #输出框
    outputtext = tk.StringVar()
    output = tk.Label(
        window,
        width = 300,
        height = 300,
        textvariable = outputtext)
    output.pack()
    #显示窗口
    window.mainloop()
   
if __name__ == '__main__':
    main()