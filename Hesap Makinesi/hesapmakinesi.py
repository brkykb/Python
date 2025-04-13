import tkinter as tk
import re
import operator


#Parser Kısmı: alınan stringin tokenlerine ayrılıp postfix ile işlem önceliği kullanılmasını saglıyor
def tokenize(expr):
    tokens = re.findall(r'\d+\.?\d*|[+\-*/^()]', expr)
    return tokens

precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

def infix_to_postfix(tokens):
    output = []
    stack = []

    for token in tokens:
        if token.isnumeric() or '.' in token:
            output.append(token)
        elif token in precedence:
            while (stack and stack[-1] in precedence and
                   precedence[token] <= precedence[stack[-1]]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # '(' silinir

    while stack:
        output.append(stack.pop())

    return output

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def evaluate_postfix(postfix):
    stack = []
    for token in postfix:
        if token in ops:
            b = float(stack.pop())
            a = float(stack.pop())
            result = ops[token](a, b)
            stack.append(result)
        else:
            stack.append(token)
    return float(stack[0])


def hesapla():
    girilen = text.get("1.0", tk.END).strip()
    tokens = tokenize(girilen)
    postfix = infix_to_postfix(tokens)
    result = evaluate_postfix(postfix)
    text.delete("1.0", tk.END)  # TextBox'ı temizle
    text.insert(tk.END, result)

pencere = tk.Tk()
pencere.title("Hesap Makinesi")
pencere.geometry("200x250")

buton1 = tk.Button(pencere, text ="1", command=lambda : text.insert(tk.END,1))
buton1.place(x=10,y=40)

buton2 = tk.Button(pencere, text="2", command=lambda : text.insert(tk.END,2))
buton2.place(x=50,y=40)

buton3 = tk.Button(pencere, text="3", command=lambda : text.insert(tk.END,3))
buton3.place(x=90,y=40)

buton4 = tk.Button(pencere, text="4", command=lambda : text.insert(tk.END,4))
buton4.place(x=10,y=80)

buton5 = tk.Button(pencere, text="5", command=lambda : text.insert(tk.END,5))
buton5.place(x=50,y=80)

buton6 = tk.Button(pencere, text="6", command=lambda : text.insert(tk.END,6))
buton6.place(x=90,y=80)

buton7 = tk.Button(pencere, text="7", command=lambda : text.insert(tk.END,7))
buton7.place(x=10,y=120)

buton8 = tk.Button(pencere, text="8", command=lambda : text.insert(tk.END,8))
buton8.place(x=50,y=120)

buton9 = tk.Button(pencere, text="9", command=lambda : text.insert(tk.END,9))
buton9.place(x=90,y=120)

buton0 = tk.Button(pencere, text="0", command=lambda : text.insert(tk.END,0))
buton0.place(x=50,y=160)

butonsolparantez = tk.Button(pencere, text="(",command=lambda : text.insert(tk.END,"("))
butonsolparantez.place(x=10,y=160)

butonsagparantez = tk.Button(pencere, text=")", command=lambda : text.insert(tk.END,")"))
butonsagparantez.place(x=90,y=160)

butoncarp = tk.Button(pencere, text="*", command=lambda : text.insert(tk.END,"*"))
butoncarp.place(x=130,y=40)

butonbol = tk.Button(pencere, text="/", command=lambda : text.insert(tk.END,"/"))
butonbol.place(x=130,y=80)

butoncikarma = tk.Button(pencere, text="-",command=lambda : text.insert(tk.END,"-"))
butoncikarma.place(x=130,y=120)

butontoplama = tk.Button(pencere, text="+",command=lambda : text.insert(tk.END,"+"))
butontoplama.place(x=130,y=160)

butonhesapla = tk.Button(pencere, text="=",command=lambda : hesapla()) 
butonhesapla.place(x=130,y=200)

butonsil = tk.Button(pencere, text="C",command=lambda : text.delete("1.0", tk.END))
butonsil.place(x=10,y=200)

text = tk.Text(pencere,height=2,width=22)
text.place(x=10,y=5)

pencere.mainloop()