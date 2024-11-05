import flet as ft

class TelaHome:

    def __init__(self,page):
        self.page=page

    def home(self):

        #Pop-up de alerta. Ao clicar em fazer logoff, uma confirmação é chamada
        alerta_logout=ft.AlertDialog(
            modal=True,
            bgcolor="#2A383E",
            title=ft.Text("CONFIRMAR LOGOUT"),
            content=ft.Text("Você realmente deseja fazer Logoff do aplicativo?"),
            actions=[
                ft.TextButton("Sim", on_click=lambda _:self.page.go("/")),
                ft.TextButton("Não", on_click=lambda e:self.page.close(alerta_logout)),
            ]
        )

        def hover_btn(e):
            e.control.bgcolor="#1C1C1C" if e.data=="true"else None
            e.control.update()

        ###############################################################################
        ###############################################################################

        logo=ft.Image("app/assets\logo3.png")
        icone_sair=ft.Container(
            padding=20,
            on_click=lambda e:self.page.open(alerta_logout),
            content=ft.Image("app/assets\Ícone Sair.svg"),
        )

        appbar=ft.Container(
            height=75,
            bgcolor="#1D3331",
            content=ft.Row(
                [
                    ft.Container(), #container vazio, utilizado somente para espaçar o ícone para o canto direito
                    icone_sair
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            padding=0
        )

        btn_home=ft.Container(
            padding=10,
            bgcolor="#1C1C1C",
            content=ft.Row(
                [
                    ft.Image("app/assets\Ícone Home.svg",width=30,height=30),
                    ft.Text("Usuários")
                ]
            )
        )

        btn_usuarios=ft.Container(
            padding=10,
            on_hover=hover_btn,
            content=ft.Row(
                [
                    ft.Image("app/assets\Ícone Perfil 2.svg",width=30,height=30),
                    ft.Text("Usuários")
                ]
            )
        )

        btn_culturas=ft.Container(
            padding=10,
            on_hover=hover_btn,
            content=ft.Row(
                [
                    ft.Image("app/assets\Ícone Cultura.svg",width=30,height=30),
                    ft.Text("Culturas")
                ]
            )
        )

        btn_plantios=ft.Container(
            padding=10,
            on_hover=hover_btn,
            content=ft.Row(
                [
                    ft.Image("app/assets\Ícone Plantio.svg",width=30,height=30),
                    ft.Text("Plantios")
                ]
            )
        )

        btn_colheitas=ft.Container(
            padding=10,
            on_hover=hover_btn,
            content=ft.Row(
                [
                    ft.Image("app/assets\Ícone Colheita.svg",width=30,height=30),
                    ft.Text("Colheitas")
                ]
            )
        )

        btn_insumos=ft.Container(
            padding=10,
            on_hover=hover_btn,
            content=ft.Row(
                [
                    ft.Image("app/assets\Ícone Insumos.svg",width=30,height=30),
                    ft.Text("Insumos")
                ]
            )
        )

        btn_fornecedores=ft.Container(
            padding=10,
            on_hover=hover_btn,
            content=ft.Row(
                [
                    ft.Image("app\/assets\Ícone Fornecedores.svg",width=30,height=30),
                    ft.Text("Fornecedores")
                ]
            )
        )

        btn_pedidos=ft.Container(
            padding=10,
            on_hover=hover_btn,
            content=ft.Row(
                [
                    ft.Image("app/assets\Ícone Financeiro.svg",width=30,height=30),
                    ft.Text("Pedidos")
                ]
            )
        )

        btn_relatorios=ft.Container(
            padding=10,
            on_hover=hover_btn,
            content=ft.Row(
                [
                    ft.Image("app/assets\Ícone Prancheta.svg",width=30,height=30),
                    ft.Text("Relatórios")
                ]
            )
        )

        sidebar=ft.Container(
            width=160,
            bgcolor="#2E2E2E",
            content=ft.Column(
                [
                    logo,
                    btn_home,
                    btn_usuarios,
                    btn_culturas,
                    btn_plantios,
                    btn_colheitas,
                    btn_insumos,
                    btn_fornecedores,
                    btn_pedidos,
                    btn_relatorios
                ]
            ),
            padding=0
        )

        txt_tela=ft.Container(
            padding=10,
            margin=10,
            content=ft.Column(
                [
                    ft.Text("Bem-vindo ao Sistema de Gerenciamento da Fazenda Urbana",color=ft.colors.BLACK,size=20),
                    ft.Text(
                        "Aqui você pode visualizar um resumo das operações.\nNavegue pelas opções do menu para gerenciar as culturas, plantios, colheitas e mais",
                        color=ft.colors.BLACK
                    )
                ]
            )
        )

        ###############################################################################
        ###############################################################################

        tela = ft.Container(
            expand=True,
            bgcolor="#D9D9D9",
            content=ft.Row(
                [
                    sidebar,
                    ft.Column(
                        [
                            appbar,
                            txt_tela
                            #ft.Container(padding=10, content=txt_tela_titulo),
                            #ft.Container(padding=10, content=txt_tela_subtitulo),
                            # Espaço para o conteúdo principal
                        ],
                        expand=True
                    )
                ],
                spacing=0  # Remove espaçamento entre sidebar e coluna
            )
        )

        return tela