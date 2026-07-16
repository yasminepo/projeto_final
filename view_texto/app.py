import os

from view_texto.login_view_texto import tela_login_texto
from view_texto.menu_view_texto import tela_menu_texto
from view_texto.inserir_view_texto import tela_inserir, tela_cadastrar_evento
from view_texto.pesquisar_view_texto import tela_pesquisar
from view_texto.remover_view_texto import tela_remover, tela_remover_evento
from view_texto.listar_view_texto import (
    tela_listar,
    tela_confirmar_presenca,
    tela_contar_participantes
)


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def main():

    while True:

        limpar_tela()

        while not tela_login_texto():
            limpar_tela()

        usuario_logado = "admin"

        while True:

            opcao = tela_menu_texto(usuario_logado)

            limpar_tela()

            if opcao == "cadastrar_evento":
                tela_cadastrar_evento()

            elif opcao == "inserir":
                tela_inserir()

            elif opcao == "confirmar":
                tela_confirmar_presenca()

            elif opcao == "contar":
                tela_contar_participantes()

            elif opcao == "pesquisar":
                tela_pesquisar()

            elif opcao == "remover":
                tela_remover()

            elif opcao == "remover_evento":
                tela_remover_evento()

            elif opcao == "listar":
                tela_listar()

            elif opcao == "logout":
                print("\nLogout realizado!")
                input("\nPressione Enter para voltar ao login...")
                break


if __name__ == "__main__":
    main()
