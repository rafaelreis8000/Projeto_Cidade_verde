import flet as ft

def login(page: ft.Page):

    #logo do projeto
    logo=ft.Container(
        alignment=ft.alignment.top_center,
        content=ft.Image(src="app/assets\logo.png")
    )

    #inputs do usuario para completar seu cadastro
    info_usuario=ft.Container(
        #alignment=ft.alignment.center,
        padding= 20,
        content=ft.Column(
            controls=[
                ft.Text("FAÇA SEU LOGIN", size=20),
                ft.TextField(label="Insira seu E-mail: "),
                ft.TextField(label="Insira sua Senha: ")
            ],
        ),
        alignment=ft.alignment.center
    )

    #ao clicar no botão, ele te leva para a tela home
    btn_login=ft.Container(
        alignment=ft.alignment.center_right,
        padding=ft.Padding(left=20,right=20,bottom=20,top=0),
        content=ft.TextButton("LOGIN",on_click=lambda _:page.go("/home")),
    )

    tela=ft.Container(
        expand=True,
        bgcolor="#1D3331",
        content=ft.ResponsiveRow(
            col={"xs": 12, "sm": 6, "md": 4},
            controls=[
                logo,
                info_usuario,
                btn_login
            ]
        ) 
    )

    #manda exibir tudo que estiver no container
    return tela