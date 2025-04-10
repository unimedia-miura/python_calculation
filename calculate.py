import tkinter as tk
from tkinter import ttk

# 各ボタン定義
BUTTON = [
    ['', 'B', 'C', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['00', '0', '.', '='],
]

SYMBOL = ['+', '-', '*', '/']

class CaluGui(object):
    def __init__(self, app=None):
        # Define
        self.calc_str = '' #計算用文字列

        # Window Setting
        app.title('電卓')
        app.geometry('300x400')

        # Frame Setting
        calc_frame = ttk.Frame(app, width=250, height=50)
        calc_frame.propagate(False)
        calc_frame.pack(side=tk.TOP, padx=10, pady=20)
        button_frame = ttk.Frame(app, width=250, height=350)
        button_frame.propagate(False)
        button_frame.pack(side=tk.BOTTOM)

        # Parts Setting
        self.calc_var = tk.StringVar() # 計算式用の動的変数
        self.ans_var = tk.StringVar() # 結果用の動的変数
        calc_label = tk.Label(calc_frame, textvariable=self.calc_var, font=("",10)) # 計算式用のLabel
        ans_label = tk.Label(calc_frame, textvariable=self.ans_var, font=("",10)) # 結果用のLabel
        calc_label.pack(anchor=tk.E)
        ans_label.pack(anchor=tk.E)

        for y, row in enumerate(BUTTON, 1):
            for x, num in enumerate(row):
                button = tk.Button(button_frame, text=num, font=('', 15), width=3, height=2)
                button.grid(row=y, column=x) # 列や行を指定して配置
                button.bind('<Button-1>', self.click_button) # Buttonが押された場合

    def click_button(self, event):
        check = event.widget['text']

        if check == '=':
            if self.calc_str[-1:] in SYMBOL: #　記号の場合、記号よりも前で計算
                self.calc_str = self.calc_str[:-1]

            res = '= ' + str(eval(self.calc_str))
            self.ans_var.set(res)
        elif check == 'C': # クリア押下時
            self.calc_str = ''
            self.ans_var.set('')
        elif check == 'B': # バック押下時
            self.calc_str = self.calc_str[:-1]
        elif check in SYMBOL:
            if self.calc_str[-1:] not in SYMBOL and self.calc_str[-1:] != '':
                self.calc_str += check
            elif self.calc_str[-1:] in SYMBOL:
                self.calc_str = self.calc_str[:-1] + check
        else: # 数字押下時
            self.calc_str += check

        self.calc_var.set(self.calc_str)

def main():
    app = tk.Tk()
    CaluGui(app)

    app.mainloop()

if __name__ == '__main__':
    main()