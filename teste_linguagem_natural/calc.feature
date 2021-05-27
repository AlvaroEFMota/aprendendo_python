#language: pt

#Behave
#pip install beahve
#para executar o behave usa-se o comando 'behave calc.feature'
#podemos criar um relatorio com junit com o comando 'behave calc.feature --junit'
# e será criado um novo diretorio chamado, no meu exemplo, TESTS-calc.xml

Funcionalidade: Calc    
    Cenario: adicao basica
        Quando somar "2" com "2"
        Então o resultado deve ser "4"

        Quando somar "30" com "2"
        Então o resultado deve ser "32"

        Quando somar "2" com "-2"
        Então o resultado deve ser "0"

    Cenario: soma com ponto flutuante
        Quando somar "4.2" com "2.1"
        Então o resultado deve ser "6.3"