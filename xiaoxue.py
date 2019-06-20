#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import tkinter as tk
import random
from math import ceil
import tkinter.messagebox
from time import sleep
root = tk.Tk()
root.title('作业')
root.geometry('1024x400')
tk.Label(root, text='请输入5 - 100的数值: ', font=('Arial', 20)).place(x=10, y=15)
int_num = tk.StringVar()
num = tk.Entry(root, textvariable=int_num, font=('Arial', 20),width=5).place(x=280, y=15)

input_result = {}
for i in range(20):
    input_result['result' + str(i)] = tk.StringVar()


def exercises():
    nums = int(int_num.get())
    if 5 > nums or nums > 100:
        tkinter.messagebox.showerror('数值错误', '请输入5 - 100的数值！')
    else:
        exercises_list = []
        for i in range(0,20):
            opt = random.choice('+-')
            if opt == '+':
                exercises = (random.randint(1, int(nums/2)),opt,random.randint(1, ceil(nums/2)))
            else:
                exercises = (random.randint(3, nums),opt,random.randint(4, nums))
                if exercises[2] > exercises[0]:
                    exercises = (exercises[2], exercises[1], exercises[0])
            exercises_list.append(exercises)

        exer_x = [10, 210,410,610, 810]
        result_x = [120, 320, 520, 720, 920]
        y = 0
        for i in range(20):
            if i % 5 == 0:
                y += 80
            locals()['exer_' + str(i)] = tk.Label(root, text=exercises_list[i], font=('Arial', 20)).place(x=exer_x[i % 5], y=y)
            locals()['result_' + str(i)] = tk.Entry(root, textvariable=input_result['result' + str(i)], font=('Arial', 18),width=5).place(x=result_x[i % 5], y=y)

        def result_cmp():
            sucess = 0
            error = 0
            show = False
            for i in range(20):
                try:
                    result = int(input_result['result' + str(i)].get())
                    if exercises_list[i][1] == '+':
                        if exercises_list[i][0] + exercises_list[i][2] == result:
                            sucess += 1
                            input_result['result' + str(i)].set(str(result) + ' √')
                        else:
                            error += 1
                            input_result['result' + str(i)].set(str(result) + ' X')
                    else:
                        if exercises_list[i][0] - exercises_list[i][2] == result:
                            sucess += 1
                            input_result['result' + str(i)].set(str(result) + ' √')
                        else:
                            error += 1
                            input_result['result' + str(i)].set(str(result) + ' X')
                    if i == 19:
                        show = True
                except ValueError:
                    tkinter.messagebox.showerror('错误','请做完所有的题目再提交')
                    break
            if show:
                tk.messagebox.showinfo('测试结果','正确{0}题， 错误{1}题. 5秒后清空答案，请重新生成题目'.format(sucess, error))
                sleep(5)
                for i in range(20):
                    input_result['result' + str(i)].set('')


        result = tk.Button(text='提交核验', width=10, height=1, command=result_cmp, font=('Arial', 18))
        result.place(x=530, y=10)


exerc = tk.Button(text='生成题目', width=10, height=1, command=exercises,font=('Arial', 18))
exerc.place(x=370, y=10)

root.mainloop()

