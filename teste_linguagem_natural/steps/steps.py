#este aquivo deve se chamar steps.py e deve estar dentro de um diretório chamado steps

from behave import step
from funcao_soma import soma

temp = None

@step('somar "{val_0:d}" com "{val_1:d}"')
def test_soma(context, val_0, val_1):
    global temp
    temp = soma(val_0, val_1)

@step('o resultado deve ser "{resultado:d}"')
def test_soma_resultado(context, resultado):
    assert temp == resultado