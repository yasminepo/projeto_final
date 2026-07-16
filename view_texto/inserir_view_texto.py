from controller import usuario_controller


def escolher_evento():
    eventos = usuario_controller.controlador_listar_eventos()

    print("\n===== ESCOLHER EVENTO =====")

    for i, evento in enumerate(eventos):
        print(f"{i + 1} - {evento['nome']} ({evento['data']})")

    while True:
        try:
            escolha = int(input("\nEscolha o evento: "))

            if 1 <= escolha <= len(eventos):
                return escolha - 1

            print("Evento inválido.")

        except ValueError:
            print("Digite um número válido.")



def tela_inserir():
    """
    Exibe a tela de cadastro de um convidado.
    """

    print("\n===== CADASTRAR CONVIDADO =====")

    indice_evento = escolher_evento()

    nome = input("Nome do convidado: ")

    sucesso, mensagem = usuario_controller.controlador_cadastrar_convidado(
        indice_evento,
        nome
    )

    print(mensagem)

    input("\nPressione Enter para voltar ao menu...")



def tela_cadastrar_evento():
    """
    Exibe a tela de cadastro de um evento.
    """

    print("\n===== CADASTRAR EVENTO =====")

    nome = input("Nome do evento: ")
    data = input("Data do evento: ")
    local = input("Local do evento: ")

    sucesso, mensagem = usuario_controller.controlador_cadastrar_evento(
        nome,
        data,
        local
    )

    print(mensagem)

    input("\nPressione Enter para voltar ao menu...")
