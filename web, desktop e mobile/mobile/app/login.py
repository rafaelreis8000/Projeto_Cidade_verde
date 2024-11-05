import flet as ft
import requests #requisições do sistema

    ###############################################################################
    ###############################################################################

def login(page: ft.Page):

    #importa a API contendo a lógica de autenticação de usuário
    API="https://api-pim.onrender.com"

    #mensagem de aviso que aparece caso ocorra algum erro na autenticação de usuário
    def snack_erro_login(e):
        page.snack_bar=ft.SnackBar(
            ft.Text(
                "Verifique suas informações de login e tente novamente!",
                text_align=ft.TextAlign.CENTER
            ),
            bgcolor="#DA4E49"
        )
        page.snack_bar.open=True
        page.update()

    #erro de comunicação com a API
    def snack_erro_API(e):
        page.snack_bar=ft.SnackBar(
            ft.Text(
                "Não foi possível se conectar com o servidor!",
                text_align=ft.TextAlign.CENTER
            ),
            bgcolor="#DA4E49"
        )
        page.snack_bar.open=True
        page.update()
    
    #função que realiza a validação de email e senha do usuário
    def autenticar_usuario(e):
        #obtém o email e senha do usuário
        email=input_email.value
        senha=input_senha.value 

        #parâmetro de requisição da API
        dados_requisicao={
            "email":email,
            "senha":senha
        }

        # Fazer a requisição à API
        try:
            response=requests.post(f"{API}/auth/login", json=dados_requisicao)
            response_data=response.json()

            # Verifica se o status da resposta é 200 e se o token foi recebido
            if response.status_code==200 and"token" in response_data:

                #se a autenticação estiver correta, leva o usuário à tela home
                page.go("/home")
            else:
                snack_erro_login(e)
        
        except requests.exceptions.RequestException as ex:
            #caso não seja possível abrir a API, esse erro será exibido
            snack_erro_API(e)

        #atualiza a página para emitir mensagens de erro
        page.update()

    ###############################################################################
    ###############################################################################

    #logo do projeto
    logo=ft.Container(
        alignment=ft.alignment.top_center,
        content=ft.Image("app/assets\logo.png")
    )

    #informações que o usuário escreve no teclado
    input_email=ft.TextField(label="Insira seu E-mail: ")
    input_senha=ft.TextField(label="Insira sua Senha: ",password=True,can_reveal_password=True)
    #inputs do usuario para completar seu cadastro

    #ao clicar no botão, ele tenta a autenticação na API
    btn_login=ft.Container(
        alignment=ft.alignment.center_right,
        padding=ft.Padding(left=20,right=20,bottom=20,top=0),
        content=ft.TextButton("LOGIN",on_click=lambda e:page.go("/home")),
        #content=ft.TextButton("LOGIN",on_click=autenticar_usuario),
    )

    ###############################################################################
    ###############################################################################

    tela=ft.Container(
        expand=True,
        bgcolor="#1D3331",
        content=ft.ResponsiveRow(
            col={"xs":12,"sm":6,"md":4},
            controls=[
                logo,
                input_email,
                input_senha,
                btn_login,
            ]
        ) 
    )

    #manda exibir tudo que estiver no container
    return tela