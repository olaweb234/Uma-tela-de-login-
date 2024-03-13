import customtkinter

user=[]
password=[]

def logar():
    
    email_login= email.get()
    senha_login= senha.get()

    if email_login in user and senha_login in password:
        print("LOGADO ")
        janelas=customtkinter.CTk()
        janelas.geometry('300 x 200')
        tex2=customtkinter.CTkLabel(janelas,text='LOGADO')
        tex2.pack(pady=20,padx=20)
        seu_email=customtkinter.CTkLabel(janelas,text='SEU EMAIL É:  ' +email_login)
        seu_email.pack(pady=20,padx=20)
        janelas.mainloop()

    else:
        print('CADASTRE')






def salvar(email,senha):
    user.append(email)
    password.append(senha)
    print('TUDO CERTO')

   



def cadastrar():
    janela_cadastro=customtkinter.CTk()
    janela_cadastro.geometry('300 x 200')
    texto_cadastro=customtkinter.CTkLabel(janela_cadastro,text="CADASTRO")
    texto_cadastro.pack(pady=20,padx=20)
    
    email=customtkinter.CTkEntry(janela_cadastro,placeholder_text='SEU EMAIL')
    email.pack(padx=20,pady=20)

    senha=customtkinter.CTkEntry(janela_cadastro,placeholder_text="SUA SENHA",show='*')
    senha.pack(pady=20,padx=20)

    botao2_cadastro=customtkinter.CTkButton(janela_cadastro,text='SALVAR CADASTRO',command=lambda: salvar(email.get(), senha.get()))
    botao2_cadastro.pack(pady=20,padx=20)

    botao3=customtkinter.CTkButton(janela_cadastro,text='SAIR',command=janela_cadastro.destroy)
    botao3.pack(pady=20,padx=20)
    janela_cadastro.mainloop()





janela=customtkinter.CTk()
janela.geometry("500 x 300")

texto1=customtkinter.CTkLabel(janela,text='TELA DE LOGIN')
texto1.pack(pady=20, padx=20)

email=customtkinter.CTkEntry(janela,placeholder_text='SEU EMAIL')
email.pack(padx=20,pady=20)

senha=customtkinter.CTkEntry(janela,placeholder_text="SUA SENHA",show='*')
senha.pack(pady=20,padx=20)


botao_logar=customtkinter.CTkButton(janela,text='LOGAR',command=logar)
botao_logar.pack(pady=10,padx=10)


botao_cadastrar=customtkinter.CTkButton(janela,text='CADASTRAR',command=cadastrar)
botao_cadastrar.pack(pady=10,padx=10)




janela.mainloop()

