from model.banco_dados import usuarios
import model.banco_dados as banco_dados


# LOGIN DO ADMINISTRADOR
def validar_login(login, senha):
    return login in usuarios and usuarios[login] == senha


# =========================
# EVENTOS
# =========================

def cadastrar_evento(nome, data, local):
    banco_dados.eventos.append({
        "nome": nome,
        "data": data,
        "local": local,
        "convidados": []
    })


def existe_evento():
    return len(banco_dados.eventos) > 0


def listar_eventos():
    return banco_dados.eventos


def dados_evento(indice_evento):

    if 0 <= indice_evento < len(banco_dados.eventos):
        return banco_dados.eventos[indice_evento]

    return None


def remover_evento(indice_evento):

    if 0 <= indice_evento < len(banco_dados.eventos):
        banco_dados.eventos.pop(indice_evento)
        return True

    return False


# =========================
# CONVIDADOS
# =========================

def cadastrar_convidado(indice_evento, nome):

    evento = dados_evento(indice_evento)

    if evento:

        if pesquisar_convidado(indice_evento, nome) is None:

            evento["convidados"].append({
                "nome": nome,
                "confirmado": False
            })


def pesquisar_convidado(indice_evento, nome):

    evento = dados_evento(indice_evento)

    if evento:

        for convidado in evento["convidados"]:

            if convidado["nome"].lower() == nome.lower():
                return convidado

    return None



def remover_convidado(indice_evento, nome):

    evento = dados_evento(indice_evento)

    convidado = pesquisar_convidado(indice_evento, nome)

    if evento and convidado:

        evento["convidados"].remove(convidado)
        return True

    return False



def confirmar_presenca(indice_evento, nome):

    convidado = pesquisar_convidado(indice_evento, nome)

    if convidado:

        convidado["confirmado"] = True
        return True

    return False



def listar_convidados(indice_evento):

    evento = dados_evento(indice_evento)

    if evento:
        return evento["convidados"]

    return []



def contar_participantes(indice_evento):

    convidados = listar_convidados(indice_evento)

    total = len(convidados)
    confirmados = 0

    for convidado in convidados:

        if convidado["confirmado"]:
            confirmados += 1

    return total, confirmadosu
