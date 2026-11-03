#Importação da Biblioteca Colorama para colorir o texto no terminal
from colorama import Fore, Style, init

init()

#Variáveis de níveis de risco

niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

#função para retornar o nível de risco com base no valor do risco

def definir_cor(nivel):

    if nivel == 1:
        return Fore.RED

    elif nivel == 2:
        return Fore.YELLOW

    elif nivel == 3:
        return Fore.GREEN

    elif nivel == 4:
        return Fore.CYAN

    elif nivel == 5:
        return Fore.BLUE


#Monitoramento do nível de risco do reservatório

for nivel in range(1, len(niveis) + 1):

    situacao = niveis[nivel - 1]
    cor = definir_cor(nivel)

    print(f"{cor}Nível {nivel}: {situacao}{Style.RESET_ALL}")