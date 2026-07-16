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



def tela_pesquisar():
    """
    Exibe a tela de pesquisa de convidado.
    """

    print("\n===== PESQUISAR CONVIDADO =====")

    indice_evento = escolher_evento()

    nome = input("Nome do convidado: ")

    encontrado, mensagem = usuario_controller.controlador_pesquisar_convidado(
        indice_evento,
        nome
    )

    print(mensagem)

    input("\nPressione Enter para voltar ao menu...")
