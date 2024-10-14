import flet as ft

#Função principal Main onde os elementos, botões e inputs serão adicionados
def main(page: ft.Page):

    #Define o nome, cor e orientação dos elementos da página
    page.title = "Teste de Login"
    page.bgcolor = "#1D3331"
    page.window_width = 360
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #Elementos presentes na página
    txt_titulo = ft.Text("Faça seu Login: ")
    email = ft.TextField(label="Insina seu e-mail: ", text_align=ft.TextAlign.CENTER)
    senha = ft.TextField(label="Insira sua senha: ", text_align=ft.TextAlign.CENTER)
    
    #O botão de login está dentro de um container para deixá-lo com alinhamento diferente do restante dos elementos
    btn_container_login = ft.Container(
        content=ft.ElevatedButton("LOGIN"),
        alignment=ft.alignment.center_right,
        width= 360, #utiliza o tamanho da tela para alinhar corretamente
    )

    #adiciona os elementos para aparecerem na tela
    page.add (txt_titulo, 
              email, 
              senha, 
              btn_container_login,)

#Inicializa um aplicativo que roda a interface main
ft.app(target=main)