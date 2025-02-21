class ConnectionDB:
    def conectar(self):
        print("Conectando ao banco")

class SQLRepository(ConnectionDB):
    def select(self):
        print("Buscando dados no banco SQL")

class NoSQLRepository(ConnectionDB):
    def select(self):
        print("Buscando dados no banco NoSQL")

#Quebra o principio de Liskov se a classe NoSQLRepository for herdada
#Porque a classe DBHandler não pode substitui-la

class DBHandler(SQLRepository):
    def alter_table(self):
        print("Alterando tabela em SQL")

con = ConnectionDB()
con.conectar()

print()

sql_repo = SQLRepository()
sql_repo.conectar()
sql_repo.select()

print()

no_sql_repo = NoSQLRepository()
no_sql_repo.conectar()
no_sql_repo.select()

print()

db_handler = DBHandler()
db_handler.conectar()
db_handler.select()
db_handler.alter_table()