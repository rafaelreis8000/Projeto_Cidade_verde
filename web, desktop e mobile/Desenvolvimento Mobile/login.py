import flet as ft

# Classe da Aplicação de Login
class Login:
    def __init__(self, page: ft.Page):
        # Inicialização da Página
        self.page = page
        self.page.title = "Login App"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.window_width =  300
        self.page.bgimage("C:\Users\master\Documents\GitHub\Projeto_Cidade_verde\web, desktop e mobile\Ícones e vetores\logo\logo\logo")

        # Campos de login
        self.username = ft.TextField(label="Usuário", width=300)
        self.password = ft.TextField(label="Senha", password=True, width=300)

        # Mensagem de status do login
        self.status_message = ft.Text()

        # Botão de login
        self.login_button = ft.ElevatedButton(text="Login", on_click=self.login)

        # Adiciona os elementos na página
        self.page.add(
            ft.Column(
                [
                    ft.Text("Bem-vindo, faça login abaixo:", size=20),
                    self.username,
                    self.password,
                    self.login_button,
                    self.status_message
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

    # Função que realiza o login
    def login(self, e):
        # Verificação de login
        if self.username.value == "admin" and self.password.value == "123":
            self.status_message.value = "Login realizado com sucesso!"
            self.status_message.color = ft.colors.GREEN
        else:
            self.status_message.value = "Usuário ou senha incorretos!"
            self.status_message.color = ft.colors.RED
        
        # Atualiza a página com a mensagem
        self.page.update()

# Função principal para executar o aplicativo
def main(page: ft.Page):
    app = Login(page)

# Execução da aplicação Flet
ft.app(target=main)
