# Importar as bibliotecas
from tkinter import * # type: ignore
# Importar ttk para usar Entry
from tkinter import messagebox  
from tkinter import ttk
import DataBaser


# Criar Nossa Janela
jan = Tk()
jan.title("DP Systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="icons/LogoIcon.ico")



# =======Criando Imagens====
logo = PhotoImage(file="icons/logo.png")

# =========Widgets=============
LeftFrame = Frame(jan, width=200, height=300, bg="red", relief="raised")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="red", relief="raised")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="red")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Usuario: ", font=("Century Gothic", 20), bg="red", fg="black")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)  # Alterado para Entry
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text="Senha: ", font=("Century Gothic", 20), bg="red", fg="black")
PassLabel.place(x=5, y=150)

PassEntry= ttk.Entry(RightFrame, width=30, show=".")
PassEntry.place(x=150, y=160)

#Botões
LoginButton = ttk.Button(RightFrame, text="Login", width=30)
LoginButton.place(x=100, y=225)

def Register():
   #removendo Widgets de Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    #Inserindo Widgets de Cadastro
    NomeLabel = Label(RightFrame,text="Nome:", font=("Century Gothic",20), bg="red", fg="black")
    NomeLabel.place(x=5, y=5)

    NomeEntry = Entry(RightFrame, width=39)
    NomeEntry.place(x=100,y=16)

    EmailLabel = Label(RightFrame,text="Email:", font=("Century Gothic",20), bg="red", fg="black")
    EmailLabel.place(x=5, y=55)

    EmailEntry = Entry(RightFrame, width=39)
    EmailEntry.place(x=100,y=66)

    Register = ttk.Button(RightFrame, text="Cadastrar", width=30)
    Register.place(x=100, y=225)

    def BackToLogin():
        #Removendo Widgets de Cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)

    Back = ttk.Button(RightFrame, text="Voltar para Login", width=20, command=BackToLogin)
    Back.place(x=125, y=260)



RegisterButton = ttk.Button(RightFrame, text="Registrar", width=20, command=Register)
RegisterButton.place(x=125, y=260)


jan.mainloop()