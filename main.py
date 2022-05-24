from asyncore import read
from click import command
import mysql.connector
import conectionDb 

# fazendo conexao ao banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password=f'{conectionDb.password}',
    database='bdmycrud',
)
# o cursor escreve no sql
cursor = conexao.cursor()

# crud
def create():
    #create (criar)
    # variaveis
    nome_produto = str(input("Qual produto deseja criar?"))
    valor = float(input('Digite o valor do produto:'))
    # comando(codigo que será setado no sql)
    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
    cursor.execute(comando)
    # commit edita o banco, executa o comando
    conexao.commit()


def read():
    # comando(codigo que será setado no sql)
    comando = f'SELECT * FROM bdmycrud.vendas;'
    cursor.execute(comando)
    # fechtall lê o banco de dados
    resultado = cursor.fetchall()
    print(resultado)


def readID():
    idVendas = str(input('Informe o ID do produto que deseja ver:'))
    # comando(codigo que será setado no sql)
    comando = f'SELECT * FROM bdmycrud.vendas where idVendas={idVendas};'
    cursor.execute(comando)
    # fechtall lê o banco de dados
    resultado = cursor.fetchall()
    print(resultado)


def update():
    nome_produto = "todynho"
    valor = 11
    comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    conexao.commit()


def delete():
    idVendas = int(input("ID a ser excluido: "))
    comando = f'DELETE FROM vendas WHERE idVendas = "{idVendas}"'
    cursor.execute(comando)
    conexao.commit()


print(
    'Digite a opção que deseja fazer no banco de dados: \n[1]Criar Produto, \n[2]Ler todos produtos \n[3]Ler produto específico \n[4]Editar produto \n[5]Deletar Produto \n[0]Sair')

opcao = int(input("Informe: "))

if opcao == 1:
    create()
elif opcao == 2:
    read()
elif opcao == 3:
    readID()
elif opcao == 4:
    update()
elif opcao == 5:
    delete()
else:
    print('Tchau')

cursor.close()
conexao.close()
print("BD fechado com sucesso")
