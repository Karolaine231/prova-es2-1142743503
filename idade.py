MINIMA = 15  # TROQUE pelo seu LIMITE


def idade_permitida(idade):
    if type(idade) is not int:
        return False
    if idade > 100:
        return False
    return idade >= MINIMA
