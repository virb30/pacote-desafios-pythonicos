"""
14. mimic

Neste desafio você vai fazer um gerador de lero-lero.

É um programa que lê um arquivo, armazena a relação entre as palavras e
então gera um novo texto respeitando essas relações para imitar um
escritor de verdade.

Para isso você precisa:

A. Abrir o arquivo especificado via linha de comando.

B. Ler o conteúdo e separar as palavras obtendo uma lista de palavras.

C. Criar um dicionário de "imitação".

Nesse dicionário a chave será uma palavra e o valor será uma lista
contendo as palavras que aparecem no texto após a palavra usada na chave.

Por exemplo, suponha um arquivo com o conteúdo: A B C B A

O dicionário de imitação deve considerar que:
* a chave A contém uma lista com a palavra B
* a chave B contém uma lista com as palavras C e A
* a chave C contém uma lista com a palavra B

Além disso precisamos considerar que:
* a chave '' contém uma lista com a primeira palavra do arquivo
* a última palavra do arquivo contém uma lista com a palavra ''.

Com o dicionario imitador é bastante simples emitir aleatoriamente texto
que imita o original. Imprima uma palavra, depois veja quais palavras podem
vir a seguir e pegue uma aleatoriamente como a proxima palavra do texto.

Use a string vazia como a primeira palavra do texto para preparar as coisas.

Nota: o módulo padrão do python 'random' conta com o random.choice(list),
método que escolhe um elemento aleatório de uma lista não vazia.
"""

import random
import sys
from collections import defaultdict
import re


def mimic_dict(filename):
    """Retorna o dicionario imitador mapeando cada palavra para a lista de palavras subsequentes."""
    content = read_content(filename)
    word_dict = extract_words(content)
    return word_dict


def read_content(filename):
    with open(filename) as file:
        content = file.read()
    return re.sub(r'[^a-zA-Z_\s]+', '', content)


def extract_words(text):
    words = text.upper().split()
    word_dict = defaultdict(list)
    word_dict[''] = [words[0]]
    word_dict[words[-1]].append('')
    for current, next_ in zip(words[:-1], words[1:]):
        word_dict[current].append(next_)
    return word_dict


def print_mimic(mimic_dict_, word, text=[]):
    """Dado o dicionario imitador e a palavra inicial, imprime texto de 200 palavras."""
    if len(text) == 200:
        print(' '.join(text))
        return
    random_word = random.choice(mimic_dict_.get(word))
    text.append(random_word)
    print_mimic(mimic_dict_, random_word, text)
    return text

    # Solução direta
    # text = []
    # while len(text) < 200:
    #     word = random.choice(mimic_dict_.get(word))
    #     text.append(word)
    # print(' '.join(text))


# Chama mimic_dict() e print_mimic()
def main():
    if len(sys.argv) != 2:
        print('Utilização: ./14_mimic.py file-to-read')
        sys.exit(1)

    word_dict = mimic_dict(sys.argv[1])
    print_mimic(word_dict, '')


if __name__ == '__main__':
    main()
