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



def tela_listar():
    """
    Exibe a lista de convidados de um evento.
    """

    print("\n===== LISTA DE CONVIDADOS =====")

    indice_evento = escolher_evento()

    convidados = usuario_controller.controlador_listar_convidados(
        indice_evento
    )

    if len(convidados) == 0:
        print("Nenhum convidado cadastrado.")
    else:
        for convidado in convidados:
            status = "Confirmado" if convidado["confirmado"] else "Pendente"
            print(f"- {convidado['nome']} ({status})")

    input("\nPressione Enter para voltar ao menu...")



def tela_confirmar_presenca():
    """
    Confirma a presença de um convidado.
    """

    print("\n===== CONFIRMAR PRESENÇA =====")

    indice_evento = escolher_evento()

    nome = input("Nome do convidado: ")

    sucesso, mensagem = usuario_controller.controlador_confirmar_presenca(
        indice_evento,
        nome
    )

    print(mensagem)

    input("\nPressione Enter para voltar ao menu...")



def tela_contar_participantes():
    """
    Exibe a quantidade de convidados de um evento.
    """

    print("\n===== PARTICIPANTES =====")

    indice_evento = escolher_evento()

    total, confirmados = usuario_controller.controlador_contar_participantes(
        indice_evento
    )

    print(f"Total de convidados: {total}")
    print(f"Presenças confirmadas: {confirmados}")
    print(f"Pendentes: {total - confirmados}")

    input("\nPressione Enter para voltar ao menu...")
