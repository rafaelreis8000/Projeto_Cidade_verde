import flet as ft

def home(page: ft.Page):

    return ft.Container(

        expand= True,
        bgcolor= "#1D3331",
        alignment= ft.alignment.center,

        content= ft.Column(

            controls= [

                ft.Container(
                    alignment= ft.alignment.center,
                    content= ft.Text("HOME", size= 40)
                ),

                    ft.Container(
                        alignment= ft.alignment.center_left,
                        content= ft.Text("Bem vindo, usuário!")
                    ),

                #criação dos botões
                ft.Container(
                    alignment= ft.alignment.bottom_center,
                    content= ft.Text ("Gestão Agrícola", size= 12),
                    width= 103,
                    height= 103,
                    bgcolor= "#2A383E",
                    border=ft.border.all(4, "#222D32"),
                    border_radius=ft.border_radius.all(10),
                    padding= 10,
                    margin= 20,
                    on_click=lambda _: page.go("/g_Agricola"), 
                    
                ),

                ft.Container(
                    alignment= ft.alignment.center,
                    content= ft.Text ("Gestão Insumos", size= 12),
                    width= 103,
                    height= 103,
                    bgcolor= "#2A383E",
                    border=ft.border.all(4, "#222D32"),
                    border_radius=ft.border_radius.all(10),
                    padding= 10,
                    margin= 20,
                ),

            ]

        )
    )