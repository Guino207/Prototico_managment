import sqlite3
import os
import time

def apresentation():
    print('1 - Sign Up')
    print('2 - Sign In')

    choose = int(input())

    if choose == 1:
        def SignUp():
            nome = input('Digite o seu nome: ')
            email = input('Digite o seu E-mail: ')
            numero = input('Digite o seu numero: ')

            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email NOT NULL,
            numero INTEGER NOT NULL               
                           )
""")
            conn.commit()

            cursor.execute("INSERT INTO usuarios(nome,email,numero) VALUES(?,?,?)",(nome,email,numero))
            conn.commit()

            print('Usuario criado com sucesso!')

            def Produto():
                
                conn = sqlite3.connect('produto.db')
                cursor = conn.cursor()

                cursor.execute("""
CREATE TABLE IF NOT EXISTS Produtos(
                               ID INTEGER PRIMARY KEY AUTOINCREMENT,
                               nome TEXT NOT NULL,
                               preco INTEGER NOT NULL,
                               quantidade INTEGER NOT NULL
                               )
""")
                conn.commit()

                print('1 - Pretende visualizar produtos: ')
                print('2 - Pretende adicionar produtos: ')
 

                escolha = input()

                if escolha == "1":
                    cursor.execute("INSERT INTO Produtos(nome,preco,quantidade) VALUES('Telefone','12000','2')")
                    conn.commit()
                    cursor.execute("SELECT * FROM Produtos")

                    for row in cursor.fetchall():
                        print(row)


                elif escolha == "2":
                    nome = input('Digite o nome do produto: ')
                    preco = input('Digite o preco do produto: ')
                    quantidade = input('Digite a quantidade dos produtos: ')

                    cursor.execute("INSERT INTO Produtos(nome,preco,quantidade) VALUES(?,?,?)",(nome,preco,quantidade))
                    conn.commit()

                    cursor.execute("SELECT * FROM Produtos")
                    conn.commit()

                    for row in cursor.fetchall():
                        print(row)

            Produto()


    SignUp()

apresentation()