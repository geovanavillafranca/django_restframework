import re
from validate_docbr import CPF


def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)
        
def nome_valido(nome):
    return nome.isalpha()        

def rg_valido(numero_do_rg):
    return len(numero_do_rg) == 9 

def celular_valido (numero_do_celular):
    """
        Verifica se o celular é valido (11 91111-1111)
    """
    modelo = re.compile('([0-9]){2} ([0-9]){5}-([0-9]{4})')
    resposta = modelo.search(numero_do_celular)
    return resposta
