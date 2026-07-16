import os
from controller import usuario_controller


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def tela_menu_texto(usuario_logado):

    while True:
        limpar_tela()

        print("\n===================================")
        print("         MENU PRINCIPAL")
        print("===================================")
        print(f"Administrador: {usuario_logado}\n")

        print("1 - Cadastrar evento")
        print("2 - Cadastrar convidado")
        print("3 - Confirmar presença")
        print("4 - Contar participantes")
        print("5 - Remover convidado")
        print("6 - Pesquisar convidado")
        print("7 - Listar convidados")
        print("8 - Logout")
        print("9 - Remover evento")

        opcao = input("\nEscolha uma opção: ")


        if opcao == "1":
            limpar_tela()
            return "cadastrar_evento"


        elif opcao in ["2", "3", "4", "5", "6", "7"]:

            if not usuario_controller.controlador_existe_evento():
                limpar_tela()
                print("\nNenhum evento cadastrado.")
                print("Cadastre um evento primeiro!")
                input("\nPressione Enter para continuar...")
                continue

            limpar_tela()

            if opcao == "2":
                return "inserir"

            elif opcao == "3":
                return "confirmar"

            elif opcao == "4":
                return "contar"

            elif opcao == "5":
                return "remover"

            elif opcao == "6":
                return "pesquisar"

            elif opcao == "7":
                return "listar"


        elif opcao == "8":
            limpar_tela()
            return "logout"


        elif opcao == "9":

            if not usuario_controller.controlador_existe_evento():
                limpar_tela()
                print("\nNenhum evento cadastrado.")
                input("\nPressione Enter para continuar...")
                continue

            limpar_tela()
            return "remover_evento"


        else:
            limpar_tela()
            print("\nOpção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")
