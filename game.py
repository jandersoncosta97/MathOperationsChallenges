from models.calcular import Calcular


def main() -> None:
    """Responsável por executar jogar(), e inicializar os pontos como nulo.
    """
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    """Responsável pela interação do usuário com a interface do jogo, incluindo gerenciamento de dificuldade,
    utilização dos métodos de Calcular. Finalmente, é responsável pelas impressão de resultados.
    """
    dificuldade: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
    print(f'Você possui {pontos} ponto' if pontos <= 1 else f'Você possui {pontos} pontos')

    continuar: int = int(input('Deseja continuar no jogo? [1 - sim, 0 - não]: '))
    while continuar not in [0, 1]:
        continuar: int = int(input('Valor inserido incorreto. Deseja continuar no jogo? [1 - sim, 0 - não]: '))
    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto' if pontos <= 1 else f'Você finalizou com {pontos} pontos')
        print('Até a próxima!')

if __name__ == '__main__':
    main()
