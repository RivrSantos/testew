from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
from datetime import date

Base = declarative_base()

class Usuario(Base):
   __tablename__ = 'usuarios'
   id = Column(Integer, primary_key=True)
   nome = Column(String)
   cpf = Column(Integer)
   contato = Column(Integer)
   endereco = Column(String)

class Veiculo(Base):
   __tablename__ = 'motos'
   id = Column(Integer, primary_key=True)
   moto = Column(String)
   ano = Column(Integer)
   placa = Column(String)
   km = Column(Integer)
   servico =Column(String)
   data = Column(String)

engine = create_engine('sqlite:///my_clients.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

datas= date.today()

print('>>> Welcome to flow register, your tool work\n')
time.sleep(1)
print('--> Connection Ok! Ready....')
time.sleep(2)
while True:
   try:
        nomes= input(' Nome: ')
        cpfs= int(input(' CPF: '))
        contatos = int(input(' Contato: '))
        enderecos = input(' Endereço: ')

        novo_usuario = Usuario(nome= nomes, cpf= cpfs, contato= contatos, endereco= enderecos)
        session.add(novo_usuario)
        session.commit()

        motos = input(' Moto/Modelo: ')
        anos = int(input(' Ano: '))
        placas = input(' Placa: ')
        kms = int(input(' KM: '))
        servicos = input(' Servico: ')

        nova_moto = Veiculo(moto= motos, ano= anos, placa= placas, km= kms, servico= servicos, data= datas)
        session.add(nova_moto)
        session.commit()

        print('\n -> Next register...\n')

        sair= int(input('DIGITE: \n--> 1: continuar\n--> 2: encerrar conexao com o Banco\n\n'))
        if sair == 1:
           pass
        elif sair == 2:
           print('--> The connection finish...')
           time.sleep(2)
           break
   except ValueError:
     print('--> valor incorreto')
while True:
    try:
        # Para ler registros, podemos usar o método query() da sessão. Podemos filtrar, ordenar e executar várias outras operações:
        cons= int(input('Deseja fazer conslta no Banco de Dados:\n\n --> 1: sim\n --> 2: nao\n\n > '))
        if cons == 1:
            cons1= input('Informe Colmn/filtro:')
            usuarios = session.query(Usuario).filter_by(cons1).all()
            for usuario in usuarios:
                print(usuario.nome)

        elif cons == 2:
            pass

        #Para atualizar, basta modificar os atributos do objeto e então chamar session.commit():
        atualizar= int(input('Deseja fazer atualizaçao no Banco de Dados:\n\n --> 1: sim\n --> 2: nao\n\n > '))
        if atualizar == 1:
            cons2= input('Informe Colmn/atualizaçao:')
            usuario = session.query(Usuario).first()
            usuario.nome = atualizar
            session.commit()

        elif atualizar == 2:
            pass

        # Para deletar, use o método delete() e então session.commit():
        deletar= int(input('Deseja deletar usuario no Banco de Dados:\n\n --> 1: sim\n --> 2: nao\n\n > '))
        if deletar == 1:
            cons3= input('Informe ID:')
            usuario = session.query(Usuario).get(cons3)
            session.delete(usuario)
            session.commit()

        elif deletar == 2:
            pass
        saindo= int(input('DIGITE: \n--> 1: continuar\n--> 2: sair\n\n'))
        if sair == 1:
            pass
        elif saindo == 2:
            print('--> The looping entry program finish...')
            time.sleep(2)
            break
    except ValueError:
        print('valor incorreto')
# Além do simples filter_by, podemos usar o método filter para construir critérios de filtragem mais complexos, utilizando operadores como ==, !=, <, >, entre outros:

# usuarios = session.query(Usuario).filter(Usuario.idade > 25).all()

# SQLAlchemy nos permite também usar funções SQL nativas, como COUNT, MAX, MIN, diretamente em nossas consultas:
# from sqlalchemy import func

# numero_de_usuarios = session.query(func.count(Usuario.id)).scalar()
# setup.py 
# colocar as dependencias do projeto
# from distutils.core import setup
# setup(console=['workflow.py'])
