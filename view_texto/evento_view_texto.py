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



def tela_remover_evento():

    print("\n===== REMOVER EVENTO =====")

    indice_evento = escolher_evento()

    sucesso, mensagem = usuario_controller.controlador_remover_evento(
        indice_evento
    )

    print(mensagem)

    input("\nPressione Enter para voltar ao menu...")
