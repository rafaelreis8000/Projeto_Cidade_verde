import flet as ft

def login(page: ft.Page):
    return ft.Container(
        expand= True,
        bgcolor= "#1D3331",
        alignment= ft.alignment.center,
        content= ft.Column(
            controls= [

                ft.Text("FAÇA SEU LOGIN: "),
                ft.TextField(label="Insira seu E-mail: "),
                ft.TextField(label= "Insira sua senha: "),
                
                    #um container somente para o botão login, com alinhamento diferente
                    ft.Container(
                        alignment= ft.alignment.center_right,
                        content= ft.ElevatedButton("LOGIN")
                    )

            ]
        )
    )