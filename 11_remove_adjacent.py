"""
11. remove_adjacent

Dada uma lista de números, retorne uma lista onde todos elementos
adjacentes iguais são reduzidos a um único elemento.

Exemplo: [1, 2, 2, 3]
Irá retornar: [1, 2, 3]
"""


def remove_adjacent(nums):
    if not nums:
        return []

    result = [nums[0]]

    pairs = zip(nums[:-1], nums[1:])
    for c, n in pairs:
        if c != n:
            result.append(n)
    return result


def one_line_solution(nums):
    if not nums:
        return []
    return [nums[0]] + [n for c, n in zip(nums[:-1], nums[1:]) if c != n]


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(remove_adjacent, [1, 2, 2, 3], [1, 2, 3])
    test(remove_adjacent, [2, 2, 3, 3, 3], [2, 3])
    test(remove_adjacent, [], [])
    test(remove_adjacent, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])
    print('One Line solution')
    test(one_line_solution, [1, 2, 2, 3], [1, 2, 3])
    test(one_line_solution, [2, 2, 3, 3, 3], [2, 3])
    test(one_line_solution, [], [])
    test(one_line_solution, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])
