import flet as ft

def login(page: ft.Page):
    return ft.Container(

        #define a cor e alinhamento dos elementos da tela
        expand= True,
        bgcolor= "#1D3331",
        alignment= ft.alignment.center,
        
        content= ft.Column(
            controls= [

                ft.Container(
                    alignment= ft.alignment.top_center,
                    content= ft.Text("FAÇA SEU LOGIN:", size= 40)
                ),


                    ft.TextField(label="Insira seu E-mail: ",),
                    ft.TextField(label= "Insira sua senha: ",),
                
                        #um container somente para o botão login, com alinhamento diferente
                        ft.Container(
                            alignment= ft.alignment.center_right,
                            content= ft.ElevatedButton("LOGIN", on_click=lambda _: page.go("/home")),
                        ),

            ]
        )
    )