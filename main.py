import cnpj

cnpjs = ['04.252.011/0001-10', '11.111.111/1111-11', '123', 'aaaaa', '40.688.134/0001-61']

for cnpj1 in cnpjs:
    if cnpj.valida(cnpj1):
        print(f'{cnpj1} - Valido')
    else:
        print(f'{cnpj1} - INVALIDO')