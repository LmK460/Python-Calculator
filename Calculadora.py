from tkinter import *
from math import*
class calculadora:
    def __init__(self,root):
        self.main = root
        self.cont = Frame(root, borderwidth = '2')
        self.cont2 = Frame(root, borderwidth = '2')
        self.cont.grid()
        self.cont2.grid()

        # operadores
        self.v1 = ''
        self.op = ''
        self.v2 = ''
        self.click=0
        self.click2=0
        self.aux=0

        # criando visores
        self.visor = Label(self.cont,font = ("Arial", "13"),width =9,anchor=E)
        self.visor.grid(row=0, column=0,columnspan=2)
        self.visor2 = Label(self.cont,font = ("Arial", "13"),width =9,anchor=W)
        self.visor2.grid(row=0, column=3,columnspan=2)
        self.visor3 = Label(self.cont,font = ("Arial", "13"),width =2)
        self.visor3.grid(row=0, column=2)
        self.visor4 = Label(self.cont,height = 2,font = ("Arial", "15", "bold"),width =9,anchor=E)
        self.visor4.grid(row=2,column=3,columnspan=3)

        # criando operações

        #configurando operações
        op1= Button(self.cont2, text = "+",height =4, width = 5,command=self.soma,bg="#7093DB",fg="#E6E8FA",bd =3)
        op1.grid(row=6,column=3)
        op2= Button(self.cont2, text = "-",height =4, width = 5,command=self.subt,bg="#7093DB",fg="#E6E8FA",bd =3)
        op2.grid(row=7,column=3)
        op3= Button(self.cont2, text=  "/",height =4, width = 5,command=self.div,bg="#7093DB",fg="#E6E8FA",bd =3)
        op3.grid(row=8,column=3)
        op4= Button(self.cont2, text = "*",height =4, width = 5,command=self.mult,bg="#7093DB",fg="#E6E8FA",bd =3)
        op4.grid(row=6,column=4)
        op5= Button(self.cont2, text = "^",height =4, width = 5,command=self.pot,bg="#7093DB",fg="#E6E8FA",bd =3)
        op5.grid(row=7,column=4)
        op6= Button(self.cont2, text = "√",height =4, width = 5,command=self.raiz,bg="#7093DB",fg="#E6E8FA",bd =3)
        op6.grid(row=8,column=4)
        op7 = Button(self.cont2, text="C", height=2, width=18,command=self.clear,bg="#7093DB",fg="#E6E8FA",bd =4)
        op7.grid(row=5, column=0, columnspan=3)
        op8=Button(self.cont2, text="DEL", height=2, width=12,command=self.delet,bg="#7093DB",fg="#E6E8FA",bd =4)
        op8.grid(row=5, column=3, columnspan=2)
        op9= Button(self.cont2, text="=", height=2, width=12,command=self.result,bg="#7093DB",fg="#E6E8FA",bd =3)
        op9.grid(row=9, column=3, columnspan=2)

        # criando botões
        b0 = Button(self.cont2, height=2, width=12, text="0", command=self.button0,bg = "#8F8FBD",fg="#E6E8FA",bd =3)
        b0.grid(row=9, column=0, columnspan=2)
        b1 = Button(self.cont2, height=4, width=5, text="1", command=self.button1,bg = "#8F8FBD",fg="#E6E8FA",bd =3)
        b1.grid(row=8, column=0)
        b2 = Button(self.cont2, height=4, width=5, text="2", command=self.button2,bg = "#8F8FBD",fg="#E6E8FA",bd =3)
        b2.grid(row=8, column=1)
        b3 = Button(self.cont2, height=4, width=5, text="3", command=self.button3,bg = "#8F8FBD",fg="#E6E8FA",bd =3)
        b3.grid(row=8, column=2)
        b4 = Button(self.cont2, height=4, width=5, text="4", command=self.button4,bg = "#8F8FBD",fg="#E6E8FA",bd =3)
        b4.grid(row=7, column=0)
        b5 = Button(self.cont2, height=4, width=5, text="5", command=self.button5,bg = "#8F8FBD",fg="#E6E8FA",bd =3)
        b5.grid(row=7, column=1)
        b6 = Button(self.cont2, height=4, width=5, text="6", command=self.button6,bg = "#8F8FBD",fg="#E6E8FA",bd =3)
        b6.grid(row=7, column=2)
        b7 = Button(self.cont2, height=4, width=5, text="7", command=self.button7,bg = "#8F8FBD",fg="#E6E8FA",bd =3)
        b7.grid(row=6, column=0)
        b8 = Button(self.cont2, height=4, width=5, text="8", command=self.button8,bg = "#8F8FBD",fg="#E6E8FA",bd =3)
        b8.grid(row=6, column=1)
        b9 = Button(self.cont2, height=4, width=5, text="9", command=self.button9,bg = "#8F8FBD",fg="#E6E8FA",bd =3)
        b9.grid(row=6, column=2)
        b10 = Button(self.cont2, text='.', height=2, width=5, command=self.button10,bg = "#8F8FBD",fg="#E6E8FA",bd =3)
        b10.grid(row=9, column=2)

    def button0(self):
        if self.op == '':
            self.v1 = self.v1 + '0'
            self.visor.configure(text=self.v1)
        else:
            self.v2 = self.v2 + '0'
            self.visor2.configure(text=self.v2)
    def button1(self):
        if self.op == '':
            self.v1 = self.v1 + '1'
            self.visor.configure(text=self.v1)
        else:
            self.v2 = self.v2 + '1'
            self.visor2.configure(text=self.v2)
    def button2(self):
        if self.op == '':
            self.v1 = self.v1 + '2'
            self.visor.configure(text=self.v1)
        else:
            self.v2 = self.v2 + '2'
            self.visor2.configure(text=self.v2)
    def button3(self):
        if self.op == '':
            self.v1 = self.v1 + '3'
            self.visor.configure(text=self.v1)
        else:
            self.v2 = self.v2 + '3'
            self.visor2.configure(text=self.v2)
    def button4(self):
        if self.op == '':
            self.v1 = self.v1 + '4'
            self.visor.configure(text=self.v1)
        else:
            self.v2 = self.v2 + '4'
            self.visor2.configure(text=self.v2)
    def button5(self):
        if self.op == '':
            self.v1 = self.v1 + '5'
            self.visor.configure(text=self.v1)
        else:
            self.v2 = self.v2 + '5'
            self.visor2.configure(text=self.v2)
    def button6(self):
        if self.op == '':
            self.v1 = self.v1 + '6'
            self.visor.configure(text=self.v1)
        else:
            self.v2 = self.v2 + '6'
            self.visor2.configure(text=self.v2)
    def button7(self):
        if self.op == '':
            self.v1 = self.v1 + '7'
            self.visor.configure(text=self.v1)
        else:
            self.v2 = self.v2 + '7'
            self.visor2.configure(text=self.v2)
    def button8(self):
        if self.op == '':
            self.v1 = self.v1 + '8'
            self.visor.configure(text=self.v1)
        else:
            self.v2 = self.v2 + '8'
            self.visor2.configure(text=self.v2)
    def button9(self):
        if self.op == '':
            self.v1 = self.v1 + '9'
            self.visor.configure(text=self.v1)
        else:
            self.v2 = self.v2 + '9'
            self.visor2.configure(text=self.v2)
    def button10(self):
        if self.op=='':
            self.v1 = self.v1 + '.'
            self.visor.configure(text=self.v1)
        else:
            self.v2 = self.v2 + '.'
            self.visor2.configure(text=self.v2)

    #definindo operações
    def clear(self):
        self.click=0
        self.v1=''
        self.v2=''
        self.op=''
        self.aux=''
        self.visor.configure(text=self.v1)
        self.visor2.configure(text=self.v2)
        self.visor3.configure(text=self.op)
        self.visor4.configure(text='')

    def soma (self):
        self.click+=1
        if self.click>=1 and self.op=='+':
            self.aux=float(self.v1)+ float(self.v2)
            self.v2=''
            self.visor2.configure(text=self.v2)
            self.visor.configure(text=self.aux)
            self.v1=self.aux
        if self.op != '+':
            if self.op == '':
                self.op='+'
                self.visor3.configure(text=self.op)
                self.aux = float(self.v1) + float(self.v2)
                self.visor4.configure(text=self.aux)
            if self.op == '-':
                self.aux = float(self.v1) - float(self.v2)
                self.v2 = ''
                self.visor2.configure(text=self.v2)
                self.visor.configure(text=self.aux)
                self.op='+'
                self.visor3.configure(text=self.op)
                self.v1 = self.aux
            if self.op == '*':
                self.aux = float(self.v1) * float(self.v2)
                self.v2 = ''
                self.visor2.configure(text=self.v2)
                self.visor.configure(text=self.aux)
                self.op = '+'
                self.visor3.configure(text=self.op)
                self.v1 = self.aux
            if self.op== '/':
                if self.v2==0:
                    self.visor4.configure(text="Error")
                    pass
                else:
                    self.aux = float(self.v1) / float(self.v2)
                    self.v2 = ''
                    self.visor2.configure(text=self.v2)
                    self.visor.configure(text=self.aux)
                    self.op = '+'
                    self.visor3.configure(text=self.op)
                    self.v1 = self.aux
            elif self.v1=='' and self.v2=='':
                self.v1+='-'
                self.visor.configure(text=self.v1)
        if self.v1=='' and self.v2=='' and self.op=='':
            self.op = '+'
            self.visor3.configure(text=self.op)
    def subt(self):
        self.click2+=1
        if self.click2>=1 and self.op== '-':
            self.v1 = self.aux
            self.aux = float(self.v1) - float(self.v2)
            self.v2 = ''
            self.visor2.configure(text=self.v2)
            self.visor.configure(text=self.aux)
            self.visor3.configure(text=self.op)
        if self.op != '-':
            if self.op == '':
                self.op='-'
                self.visor3.configure(text=self.op)
                self.aux = float(self.v1) - float(self.v2)
                self.visor4.configure(text=self.aux)
            if self.op == '+':
                self.aux = float(self.v1) + float(self.v2)
                self.v2 = ''
                self.visor2.configure(text=self.v2)
                self.visor.configure(text=self.aux)
                self.op='-'
                self.visor3.configure(text='-')
                self.v1 = self.aux
            if self.op == '*':
                self.aux = float(self.v1) * float(self.v2)
                self.v2 = ''
                self.visor2.configure(text=self.v2)
                self.visor.configure(text=self.aux)
                self.op = '-'
                self.visor3.configure(text='-')
                self.v1 = self.aux
            if self.op== '/':
                if self.v2==0:
                    self.visor4.configure(text="Error")
                    pass
                else:
                    self.aux = float(self.v1) / float(self.v2)
                    self.v2 = ''
                    self.visor2.configure(text=self.v2)
                    self.visor.configure(text=self.aux)
                    self.op = '-'
                    self.visor3.configure(text='-')
                    self.v1 = self.aux
            elif self.v1=='' and self.v2=='':
                self.v1+='-'
                self.visor.configure(text=self.v1)
        else:
            self.op = '-'
            self.visor3.configure(text=self.op)
    def mult (self):
        self.click += 1
        self.op='*'
        self.visor3.configure(text=self.op)
    def div (self):
        self.click += 1
        self.op='/'
        self.visor3.configure(text=self.op)
    def raiz (self):
        self.click += 1
        self.op='√'
        self.visor3.configure(text=self.op)
    def pot(self):
        self.click += 1
        self.op = '^'
        self.visor3.configure(text=self.op)
    def delet(self):
        if self.v1 != '' and self.op=='':
            self.v1= self.v1[:len(self.v1) - 1]
            self.visor.configure(text=self.v1)
        if self.v1 !='' and self.op !='' and self.v2 == '':
            self.op=self.op[:len(self.op) - 1]
            self.visor3.configure(text=self.op)
        else :
            self.v2=self.v2[:len(self.v2) - 1]
            self.visor2.configure(text=self.v2)
    def result(self):
        self.click =0
        if self.op=='+':
            self.aux= float(self.v1) + float(self.v2)
            self.visor4.configure(text="%.2f"%self.aux)
        elif self.op=='-':
            self.aux= float(self.v1) - float(self.v2)
            self.visor4.configure(text="%.2f"%self.aux)
        elif self.op=='*':
            self.aux= float(self.v1)*float(self.v2)
            self.visor4.configure(text="%.2f"%self.aux)
        elif self.op=='/':
            if self.v2 != '0' and self.v2 != '':
                self.aux= float(self.v1)/float(self.v2)
                self.visor4.configure(text="%.2f"%self.aux)
            else:
                self.visor4.configure(text="Error")
                pass
        elif self.op=='^':
            self.op='^'
            self.aux= pow(float(self.v1),float(self.v2))
            self.visor4.configure(text="%.2f"%self.aux)
        elif self.op=='√':
            if self.v1=='':
                self.aux=sqrt(float(self.v2))
                self.visor4.configure(text="%.4f"%self.aux)
            else:
                self.aux=float(self.v1)*(sqrt(float(self.v2)))
                self.visor4.configure(text="%.4f"%self.aux)



root=Tk()
root.resizable(width=FALSE, height=FALSE)
root.title('Calculadora')
calc=calculadora(root)
mainloop()
