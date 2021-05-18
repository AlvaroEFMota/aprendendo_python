from unittest import TestCase, main

def par(val):
    try: #se o usuário digitar um string por exemplo
        return True if val%2 == 0 else False
    except TypeError:
        return False
    
def soma(x,y):
    return x+y

def sub(x,y):
    return x-y

#um teste usando o unittest
class Testes(TestCase):
    def test_soma(self):
        self.assertEqual(soma(75,87),162)

    def test_sub(self):
        self.assertEqual(sub(75,87),-12)

    def test_par(self):
        self.assertEqual(par(5), False)
        self.assertEqual(par('huehue'), False)

#um teste simples com o assert
#assert soma(2,3) == 5, 'Erro na funçao soma(2,3), deveria ter resposta {}'.format(5)

if __name__ == '__main__':
    main() ## executa a função main do unittest ao iniciar o programa
