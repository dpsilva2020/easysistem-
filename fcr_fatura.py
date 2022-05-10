#CONTAS A RECEBER

def cadastro_fatura():
    print('-'*30)
    print('CONTAS A RECEBER')
    print('-'*30)


    nfatura=input('Fatura: ')
    ncliente=int(input('Cliente: '))
    dt_emissao=input('Data emissão: ')
    dt_vencimento_original=input('Data vencimento: ')
    dt_vencimento=dt_vencimento_original
    t_fatura='MN'
    f_valor=float(input('Valor:'))
    f_juros=float(input('Juros: '))
    f_desconto=float(input('Desconto: '))
    f_vl_liquido=f_valor+f_juros-f_desconto

    print(f'{nfatura}')