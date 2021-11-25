"""
    Aula 01 do curso de NLP
    JR Steiner

    Pasta do Curso:
    https://bit.ly/2o9yAOo


"""

from spacy.lang.pt import Portuguese

def main():
    """
        main function
    """

    """
    No centro de spaCy está o objeto que contém o pipeline de processamento.
    Geralmente chamamos essa variável "nlp".

    Por exemplo, para criar um objeto nlp em português, você pode importar a classe 
    de idioma português do spacy.lang.pt e instancia-la.
    
    Você pode usar o objeto NLP como uma função para analisar o texto.

    Ele contém todos os diferentes componentes no pipeline.

    Ele também inclui regras específicas do idioma usadas para tokenizar o 
    texto em palavras e pontuação.
    
    O spaCy suporta uma variedade de idiomas disponíveis no spacy.lang.
    """
    nlp = Portuguese()

    """
    Quando você processa um texto com o objeto NLP, o spaCy cria um objeto Doc -
    abreviação de "documento".
    O Doc permite acessar informações sobre o texto de maneira estruturada e
    nenhuma informação é perdida.

    O Doc se comporta como uma sequência Python normal, a propósito, e permite
    iterar sobre seus tokens, ou obter um token por seu índice.
    """
    # print('\n -------------------------- \n')
    # doc = nlp(u'Este é um exemplo bem simples.')
    # for token in doc:
    #     print(token.text)

    """
    Um objeto Span é uma fatia do documento que consiste em um ou mais tokens.
    É apenas uma visão do Doc e não contém dados em si.

    Para criar um Span, você pode usar a notação de fatia do Python.
    """
    # print('\n -------------------------- \n')
    # span = doc[1:7]
    # print(f'\nRetiramos o primeiro token:\n {span.text}')

    """
    Aqui você pode ver alguns dos atributos de token disponíveis:
        "i" é o índice do token no documento pai.
        "text" retorna o texto do token.
        "is alpha", "é punct" e "like num" retornam valores booleanos
        indicando se o token consiste em caracteres alfabéticos, se é pontuação,
        ou se parece com um número.
        
    Por exemplo, um token "10" - um, zero - ou a palavra "dez" - D, E, Z
    
    Esses atributos também são chamados de atributos lexicais: eles se referem à
    entrada no vocabulário e não dependem do contexto do token.
    """
    # print('\n -------------------------- \n')
    # doc = nlp("Este custa $5.")
    # print('Index:   ', [token.i for token in doc])
    # print('Text:    ', [token.text for token in doc])

    # print('is_alpha:', [token.is_alpha for token in doc])
    # print('is_punct:', [token.is_punct for token in doc])
    # print('like_num:', [token.like_num for token in doc])

if __name__ == "__main__":
    main()