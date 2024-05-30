import sqlite3

class SetUp:
    
    def create_db(self):
        
        try:
            
            conn = None
            conn = sqlite3.connect('db.sqlite')
            
            if conn:
                conn.close()
                
        except sqlite3.Error as e:
            print(f'Error al crear la base de datos: {e}')

    def create_table(self):
        
        tables = [
            '''
                CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    id_departamento INTEGER NOT NULL,
                    
                    FOREIGN KEY (id_departamento)
                    REFERENCES departaments (id)
                    ON UPDATE NO ACTION
                    ON DELETE NO ACTION
                )
            ''',
            '''
                CREATE TABLE IF NOT EXISTS departaments (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL
                )
            '''
        ]
        
        try:
            with sqlite3.connect('db.sqlite') as conn:
                cursor = conn.cursor()
                
                for table in tables:
                    cursor.execute(table)
                    
        except sqlite3.Error as e:
            print(f'Error al crear las tablas: {e}')


class OperationsDataBase:
    
    def connection(self,statement, data):
        
        try:
            with sqlite3.connect('db.sqlite') as conn:
                cursor = conn.cursor()
                cursor.execute(statement, data)
                conn.commit()
        except sqlite3.Error as e:
            print(f'Error al conectarse a la base de datos: {e}')
    
    def insert_data_employees(self,employee):
        
        insert_statement = '''
        
        INSERT INTO employees (name, apellido, id_departamento)
        VALUES (?, ?, ?)
        '''
        
        self.connection(insert_statement, employee)

    def insert_data_departaments(self,departament):
        
        insert_statement = '''
        
        INSERT INTO departaments (name)
        VALUES (?)
        '''
        
        self.connection(insert_statement, departament)

    def update_employees(self, employee):
        
        update_statement = f'''
            UPDATE employees
            SET name = ?,
                apellido = ?,
                id_departamento = ?
            WHERE id = ?
        '''
        
        self.connection(update_statement, employee)

    def update_departaments(self,departament):
        
        update_statement = '''
            UPDATE departaments
            SET name = ?
            WHERE id = ?
        '''
        
        self.connection(update_statement, departament)

    def delete_employees(self,employee):
        
        delete_statement = '''
            DELETE FROM employees
            WHERE id = ?
        '''
        
        self.connection(delete_statement, employee)

    def delete_departaments(self,departament):
        
        delete_departament = '''
            DELETE FROM departaments
            WHERE id = ?
        '''
        
        self.connection(delete_departament, departament)

