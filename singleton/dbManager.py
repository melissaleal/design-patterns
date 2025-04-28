## Definindo uma abstract factory para conexão
class Connection: 
    def createConnection(self):
        pass

    def createConnectionString(self):
        pass

## Criando uma superclasse para a string de conexão
class ConnectionString:
    def __init__(self, host, port, database, user, password):
        self._host = host
        self._port = port
        self._database = database
        self._user = user
        self._password = password

    def returnString(self):
        pass

## Especificando as strings de conexão para cada banco
class MySQLString(ConnectionString):
    def returnString(self):
        return f"jdbc:mysql://{self._host}:{self._port}/{self._database}?user={self._user}&password={self._password}"
    
class PostgreSQLString(ConnectionString):
    def returnString(self):
        return f"jdbc:postgresql://{self._host}:{self._port}/{self._database}?user={self._user}&password={self._password}"
    
class SQLServerString(ConnectionString):
    def returnString(self):
        return f"jdbc:sqlserver://{self._host}:{self._port}/{self._database}?user={self._user}&password={self._password}"

## Definindo fábricas concretas para cada banco
class MySQLFactory(Connection): 
    def createConnection(self):
        return MySQLConnection()
    
    def createConnectionString(self):
        return MySQLString("localhost", 3306, "database", "root", "seungmin")
    
    def message(self):
        return f"Establishing connection with MySQL"

class PostgreSQLFactory(Connection): 
    def createConnection(self):
        return PostgreSQLConnection()
    
    def createConnectionString(self):
        return PostgreSQLString("localhost", 5432, "database", "root", "banhgchan")

    def message(self):
        return f"Establishing connection with PostgreSQL"
    
class SQLServerFactory(Connection): 
    def createConnection(self):
        return SQLServerConnection()
    
    def createConnectionString(self):
        return SQLServerString("localhost", 1433, "database", "root", "sTrayKidS")

    def message(self):
        return f"Establishing connection with SQL Server"

## Criando Singletons para cada banco
class MySQLConnection:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            MySQLConnection.__instance = super().__new__(cls)
        return MySQLConnection.__instance

class PostgreSQLConnection:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            PostgreSQLConnection.__instance = super().__new__(cls)
        return PostgreSQLConnection.__instance    

class SQLServerConnection:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            SQLServerConnection.__instance = super().__new__(cls)
        return SQLServerConnection.__instance

def menu():
    while True:
        print(f"\n DATABASES ")
        print(f"1 - MySQL")
        print(f"2 - PostgreSQL")
        print(f"3 - SQL Server")
        print(f"4 - Cancel")
        
        opt = input("Choose: ")
        try:
            opt = int(opt)
        except:
            print("Choose")
            
        if opt == 1:
            factory = MySQLFactory()

        elif opt == 2:
            factory = PostgreSQLFactory()
        elif opt == 3:
            factory = SQLServerFactory()
        elif opt == 4:
            print(f"Goodbye...")
            break
        else:
            print(f"Invalid...")

        connection1 = factory.createConnection()
        connection2 = factory.createConnection()
        connectionstring = factory.createConnectionString()

        print(f"{factory.message()}")
        print(f"Connection string: {connectionstring.returnString()}")
        print(f"Is it Singleton? {connection1 is connection2}")

if __name__ == "__main__":
    menu()