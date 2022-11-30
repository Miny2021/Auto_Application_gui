with open("latestlog.txt",'w') as log:
    import datetime as dt
    print(f"{dt.datetime.now()} 欢迎进入调试模式（开源）")
    log.write(f"{dt.datetime.now()} 欢迎进入调试模式（开源）\n")
    print(f"{dt.datetime.now()} 导入模块tkinter")
    log.write(f"{dt.datetime.now()} 导入模块tkinter\n")
    import tkinter as tk
    print(f"{dt.datetime.now()} 导入模块tkinter中的类messagebox")
    log.write(f"{dt.datetime.now()} 导入模块tkinter中的类messagebox\n")
    import tkinter.messagebox as messagebox
    print(f"{dt.datetime.now()} 导入模块_thread")
    log.write(f"{dt.datetime.now()} 导入模块_thread\n")
    import _thread
    print(f"{dt.datetime.now()} 导入模块os")
    log.write(f"{dt.datetime.now()} 导入模块os\n")
    import os
    print(f"{dt.datetime.now()} 导入模块time")
    log.write(f"{dt.datetime.now()} 导入模块time\n")
    import time as module_time
    print(f"{dt.datetime.now()} 导入模块tqdm")
    log.write(f"{dt.datetime.now()} 导入模块tqdm\n")
    from tqdm import tqdm
    print(f"{dt.datetime.now()} 导入模块random")
    log.write(f"{dt.datetime.now()} 导入模块random\n")
    import random
    print(f"{dt.datetime.now()} 模块导入完成")
    log.write(f"{dt.datetime.now()} 模块导入完成\n")
    # 函数部分
    print(f"{dt.datetime.now()} 定义函数main")
    log.write(f"{dt.datetime.now()} 定义函数main\n")
    def main():
        print(f"{dt.datetime.now()} 定义函数get_user_input")
        log.write(f"{dt.datetime.now()} 定义函数get_user_input\n")
        def get_user_input():
            """获取用户输入并判断"""
            print(f"{dt.datetime.now()} 检测到用户点击\"运行\"按钮")
            log.write(f"{dt.datetime.now()} 检测到用户点击\"运行\"按钮\n")
            print(f"{dt.datetime.now()} 获取用户输入")
            log.write(f"{dt.datetime.now()} 获取用户输入\n")
            cmd = command.get()# 获取用户输入
            print(f"{dt.datetime.now()} 清除输入框")
            log.write(f"{dt.datetime.now()} 清除输入框\n")
            command.delete('0','end')# 清空输入框
            if cmd == 'about': # 如果用户输入了about
                print(f"{dt.datetime.now()} 检测到用户输入about")
                log.write(f"{dt.datetime.now()} 检测到用户输入about\n")
                print(f"{dt.datetime.now()} 在输出框显示Run to about")
                log.write(f"{dt.datetime.now()} 在输出框显示Run to about\n")
                outputtext.set('Run to about')# 输入框显示Run to about
                print(f"{dt.datetime.now()} 定义about窗口")
                log.write(f"{dt.datetime.now()} 定义about窗口\n")
                about = tk.Tk()# 定义about窗口
                print(f"{dt.datetime.now()} 定义about窗口的标题")
                log.write(f"{dt.datetime.now()} 定义about窗口的标题\n")
                about.title('关于 - 自动程序')# 定义about窗口的标题
                # 定义Label文本框
                print(f"{dt.datetime.now()} 定义Label文本显示框")
                log.write(f"{dt.datetime.now()} 定义Label文本显示框\n")
                t = tk.Label(
                    about,
                    text = 'Made by AGS\nabout关于\nhelp查看更多指令')
                print(f"{dt.datetime.now()} 显示文本框")
                log.write(f"{dt.datetime.now()} 显示文本框\n")
                t.pack()
                #显示窗口
                print(f"{dt.datetime.now()} 显示窗口")
                log.write(f"{dt.datetime.now()} 显示窗口\n")
                about.mainloop()
            if cmd == 'help':
                print(f"{dt.datetime.now()} 检测到用户输入help")
                log.write(f"{dt.datetime.now()} 检测到用户输入help\n")
                print(f"{dt.datetime.now()} 在输出框显示Run to help")
                log.write(f"{dt.datetime.now()} 在输出框显示Run to help\n")
                outputtext.set('Run to help')
                print(f"{dt.datetime.now()} 定义help窗口")
                log.write(f"{dt.datetime.now()} 定义help窗口\n")
                helps = tk.Tk()
                print(f"{dt.datetime.now()} 定义help窗口的标题")
                log.write(f"{dt.datetime.now()} 定义help窗口的标题\n")
                helps.title('帮助 - 自动程序')
                print(f"{dt.datetime.now()} 定义Label文本显示框文字")
                log.write(f"{dt.datetime.now()} 定义Label文本显示框文字\n")
                texts =  'help打开帮助'
                texts += '\nabout打开关于'
                texts += '\ntimer close exes打开 \'定时关闭程序\''
                texts += '\n其他功能尽情期待'
                print(f"{dt.datetime.now()} 定义Label文本显示框")
                log.write(f"{dt.datetime.now()} 定义Label文本显示框\n")
                t = tk.Label(
                    helps,
                    text = texts)
                print(f"{dt.datetime.now()} 显示文本框")
                log.write(f"{dt.datetime.now()} 显示文本框\n")
                t.pack()
                print(f"{dt.datetime.now()} 显示窗口")
                log.write(f"{dt.datetime.now()} 显示窗口\n")
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
                        for i in range(0,times):
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
            else:
                print(f"{dt.datetime.now()} 无效输入")
                log.write(f"{dt.datetime.now()} 无效输入\n")
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
        print(f"{dt.datetime.now()} 程序已退出")
        log.write(f"{dt.datetime.now()} 程序已退出")