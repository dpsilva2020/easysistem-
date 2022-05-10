import cd_pessoa as pessoa
import fcp_duplicata as cp
import prd_produto as produto
import fcr_fatura as cr
import pandas as pd


print('***'*30)
print('EasySistem')
print('***'*30)

modulo=int(input("1-CADASTRO DE PESSOA \n2-CADASTRO DE PRODUTO \n3-CONTAS A PAGAR \n4-CONTAS A RECEBER :"))

if modulo==1:
   cadastro=pessoa.consulta_rfb()

elif modulo==2:
    print(produto.produto_entrada())
    produto_entrada=int(input('informe a opções: '))
    opcoes=produto.opcoes(produto_entrada)
elif modulo==3:
    print('*'*30)
    print('CONTAS A PAGAR')
    print('*'*30)
    opcao=int(input('1-CADASTRAR DUPLICA \n2-ALTERAR DUPLICATA \n3-EXCLUIR DUPLICATA \n4-BAIXAR DUPLICATA'))
    if opcao==1:
        print('*'*30)
        print('CADASTRO DE DUPLICATA')
        print('*'*30)
        cp.cadastro_duplicata()
    elif opcao==2:
        cp.alterar_duplicata()
    elif opcao==3:
        print("ok")
    elif opcao==4:
        cp.baixar_duplicata()
elif modulo==4:
    print('*'*30)
    print('CONTAS A RECEBER')
    print('*'*30)
    opcao=int(input('1-CADASTRAR DUPLICA \n2-ALTERAR DUPLICATA \n3-EXCLUIR DUPLICATA \n4-BAIXAR DUPLICATA'))
    if opcao==1:
        print('*'*30)
        print('CADASTRO DE DUPLICATA')
        print('*'*30)
        cr.cadastro_fatura()


