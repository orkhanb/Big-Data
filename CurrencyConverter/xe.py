import urllib.request
import tkinter as tk
from tkinter import ttk

def open_web(value1, value2):
    web_obj =urllib.request.urlopen("https://free.currencyconverterapi.com/api/v6/convert?q="+value1+"_"+value2+"&compact=ultra&apiKey=98b6c90bb6b683dc7f48")
    results_str = str(web_obj.read())
    web_obj.close()
    result=float(results_str[results_str.index(":")+1:len(results_str)-2])
    return  result

class Currency:
    def __init__(self,value,currencyUnit):
        self.value=value
        self.currencyUnit1=currencyUnit

    def convertTo(self,currencyUnit):
        self.currencyUnit2=currencyUnit
        self.resultCurrency=open_web(self.currencyUnit1,self.currencyUnit2)
        self.result=self.resultCurrency*self.value
        return self.result

    def __str__(self):
        return str(self.value)+"-"+self.currencyUnit1+" Convert To:"+self.currencyUnit2+"="+str(self.result)
    pass


def click():
    print(type(value1.get()))
    try:
        print(value1.get()+" "+value2.get())
        open_web(cmb1.get(), cmb2.get())
        cur = Currency(int(value1.get()), cmb1.get())
        new_cur_1value = cur.convertTo(cmb2.get())
        value2.set(new_cur_1value)
    except:
        print(value1.get() + " " + value2.get())
        open_web(cmb1.get(), cmb2.get())
        cur = Currency(int(1), cmb1.get())
        new_cur_1value = cur.convertTo(cmb2.get())
        value2.set(new_cur_1value)
    pass




window = tk.Tk()
window.title(" Google Finance currency calculator API")
window.geometry("500x200")
window.resizable(0, 0)

amount=ttk.Label(text="Amount")
amount.grid(column=0, row=0)
amount.config(font=("Courier", 10))
value1=tk.StringVar()
txt=ttk.Entry(width=10,textvariable = value1)
txt.grid(column=0, row=1)
txt.config(font=("Courier", 10))

cmb1Text=ttk.Label(text="From")
cmb1Text.grid(column=1, row=0)
cmb1Text.config(font=("Courier", 10))

cmb1 = ttk.Combobox(window,values=[ "USD","EUR", "TRY",  "AZN", "RUB", ],width=5,state="readonly")
cmb1.grid(column=1, row=1)
cmb1.config(font=("Courier", 10))
cmb1.current(0)


cmb2Text=ttk.Label(text="To")
cmb2Text.grid(column=2, row=0)
cmb2Text.config(font=("Courier", 10))
cmb2 = ttk.Combobox(window, values=["USD", "EUR", "TRY", "AZN", "RUB", ],width=5,state="readonly")
cmb2.grid(column=2, row=1)
cmb2.config(font=("Courier", 10))
cmb2.current(0)


value2 = tk.StringVar()
txt2=ttk.Entry(width=10,textvariable = value2, state="readonly")
txt2.grid(column=5,row=1)
txt2.config(font=("Courier", 10))

btn=ttk.Button(text="Calculate",command=click)
btn.grid(column=6, row=1)


window.mainloop()