# import random
# import tkinter as tk
# from tkinter import messagebox
# from tkinter import scrolledtext
# import threading
# import easygu
#
# # 创建全局锁和Text控件引用
# log_text_lock = threading.Lock()
# log_text = None
#
# def log_message(message):
#     '''更新Text控件（如果log_text已初始化）'''
#     try:
#         log_text_lock.acquire()  # 获取锁
#         if log_text:
#             log_text.insert(tk.END, message+'\n')
#             # log_text.insert('\n')
#             log_text.see(tk.END)  # 自动滚动到最底部
#         log_text_lock.release()  # 释放锁
#     except NameError:
#         # 如果log_text还未初始化，则忽略此消息
#         pass
#
# def create_buttons():
#     '''点击按钮的排序'''
#     column = 0
#     buttons = [
#         ("点击开始抽签", random_chooser),
#     ]
#     for text, command in buttons:
#         button = tk.Button(button_frame, text=text,
#                            command=lambda cmd=command: threading.Thread(target=cmd).start())
#         button.grid(row=0, column=column, padx=5, pady=5, sticky=tk.E)  # 水平排列，右对齐
#         column += 1
#
# def random_chooser():
#     """
#     从列表中选中指定人员进行抽签，默认为items列表
#     参数:
#     items (list): 包含要选择的元素的列表。
#     返回:
#     随机选择的元素。
#     """
#     items = ["楚云", "森威", "明宽"]
#     name_list = ["楚云", "森威", "明宽", "冠峰","长春", "永聪", "喜洋", "选好了"]
#     log_message(f'请选择参与抽签的人员，\n默认已有{items}')
#     while True:
#         more_chice = easygui.choicebox('请选择需要进行抽签的人员姓名：', choices=name_list)
#
#         if more_chice != "选好了" and more_chice not in items:
#             items.append(more_chice)
#             log_message(f'{more_chice}已添加到抽签列表')
#         elif more_chice in items:
#             messagebox.showinfo('人员提醒', f'{more_chice}已被选择，请重新选择')
#
#         if more_chice == "选好了":
#             log_message('人员选择结束，开始抽签')
#             break
#     # if not items:
#     #     raise ValueError("列表不能为空")
#
#     log_message(f"参与抽签的人员有：{items}")
#     log_message(f'选中的是{random.choice(items)}')
#     return random.choice(items)
#
# # 示例使用
# if __name__ == "__main__":
#     # options = ["楚云", "森威", "明宽"]
#     # chosen_item = random_chooser(options)
#     # print(f"随机选择的是: {chosen_item}")
#     root = tk.Tk()
#     root.title('随机选择器')
#     log_text_frame = tk.Frame(root)
#     log_text_frame.pack(fill=tk.BOTH, expand=True)
#     log_text = scrolledtext.ScrolledText(log_text_frame, width=80, height=10, font=("微软雅黑", 10), spacing1=2)
#     log_text.pack(fill=tk.BOTH, expand=True)
#
#     button_frame = tk.Frame(root)
#     button_frame.pack(fill=tk.X, padx=10, pady=10)
#
#     create_buttons()
#
#     root.mainloop()