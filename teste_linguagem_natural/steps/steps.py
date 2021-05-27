#este aquivo deve se chamar steps.py e deve estar dentro de um diretório chamado steps

from behave import step
from funcao_soma import soma
from decimal import *
getcontext().prec = 3


#@step('somar "{val_0:d}" com "{val_1:d}"') # transforma val_0 e val_1 em decimais (se for usar deve-se tirar os cast Decimal)
@step('somar "{val_0}" com "{val_1}"')
def test_soma(context, val_0, val_1):
    context.soma_result = Decimal(soma(Decimal(val_0), Decimal(val_1)))

#@step('o resultado deve ser "{resultado:d}"')
@step('o resultado deve ser "{resultado}"')
def test_soma_resultado(context, resultado):
    print(context.soma_result, "==", resultado)
    assert context.soma_result == Decimal(resultado)