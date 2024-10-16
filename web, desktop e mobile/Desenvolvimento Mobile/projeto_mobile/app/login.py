import flet as ft

def login(page: ft.Page):
    return ft.Container(
        bgcolor= "#1D3331",
        alignment= ft.alignment.center,
        content= ft.Column(
            controls= [
                ft.Text("FAÇA SEU LOGIN: ", size=40),
                ft.TextField(label="Insira seu E-mail: ")
            ]
        )
    )