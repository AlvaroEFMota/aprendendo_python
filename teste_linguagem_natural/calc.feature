#language: pt

#Behave
#pip install beahve
#para executar o behave usa-se o comando 'behave calc.feature'

Funcionalidade: Calc    
    Cenario: adicao basica
        Quando somar "2" com "2"
        Então o resultado deve ser "4"
