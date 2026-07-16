from controller import usuario_controller


def tela_login_texto():
    """
    Exibe a tela de login do administrador.
    """
    print("===================================")
    print("      SISTEMA PARA EVENTOS")
    print("===================================")
    print("Login do Administrador\n")

    login = input("Login: ")
    senha = input("Senha: ")

    login_valido = usuario_controller.controlador_login(login, senha)

    if login_valido:
        print("\nLogin realizado com sucesso!")
        return True

    else:
        print("\nLogin ou senha incorretos.")
        input("\nPressione Enter para tentar novamente...")
        return False
