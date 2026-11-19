from idade import idade_permitida


def test_idade_igual_ao_limite_e_aceita():
    # preparar
    idade = 15
    # agir
    resultado = idade_permitida(idade)
    # verificar
    assert resultado is True


def test_idade_um_abaixo_do_limite_e_rejeitada():
    # preparar
    idade = 14
    # agir
    resultado = idade_permitida(idade)
    # verificar
    assert resultado is False


def test_idade_acima_de_100_e_rejeitada():
    # preparar
    idade = 101
    # agir
    resultado = idade_permitida(idade)
    # verificar
    assert resultado is False

def test_idade_com_virgula_e_rejeitada():
    # preparar
    idade = 15.5
    # agir
    resultado = idade_permitida(idade)
    # verificar
    assert resultado is False
