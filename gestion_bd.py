import sqlite3

def create_db():
    
    try:
        
        conn = None
        conn = sqlite3.connect('db.sqlite')
        
        if conn:
            conn.close()
            
    except sqlite3.Error as e:
        print(f'Error al crear la base de datos: {e}')
        
if __name__ == '__main__':
    create_db()

def create_table():
    
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

if __name__ == '__main__':
   create_table()
   
def connection(statement, data):
    
    try:
        with sqlite3.connect('db.sqlite') as conn:
            cursor = conn.cursor()
            cursor.execute(statement, data)
            conn.commit()
    except sqlite3.Error as e:
        print(f'Error al conectarse a la base de datos: {e}')
   
def insert_data_employees(employee):
    
    insert_statement = '''
    
    INSERT INTO employees (name, apellido, id_departamento)
    VALUES (?, ?, ?)
    '''
    
    connection(insert_statement, employee)

def insert_data_departaments(departament):
    
    insert_statement = '''
    
    INSERT INTO departaments (name)
    VALUES (?)
    '''
    
    connection(insert_statement, departament)


def update_employees(employee):
    
    update_statement = f'''
        UPDATE employees
        SET name = ?,
            apellido = ?,
            id_departamento = ?
        WHERE id = ?
    '''
    
    connection(update_statement, employee)

def update_departaments(departament):
    
    update_statement = '''
        UPDATE departaments
        SET name = ?
        WHERE id = ?
    '''
    
    connection(update_statement, departament)

def delete_employees(employee):
    
    delete_statement = '''
        DELETE FROM employees
        WHERE id = ?
    '''
    
    connection(delete_statement, employee)

def delete_departaments(departament):
    
    delete_departament = '''
        DELETE FROM departaments
        WHERE id = ?
    '''
    
    connection(delete_departament, departament)


def menu():
    
    while True:
    
        print('\n****************')
        print('MENÚ DE OPCIONES')
        print('****************')
        
        print('\n1. Insertar datos')
        print('2. Actualizar datos')
        print('3. Eliminar datos')
        print('4. Salir\n')
        
        option = input('Ingrese una opción: ')
        print()
        
        match option:
            
            case '1':
                
                table = input('¿En qué tabla desea insertar datos?(employees or departaments): ')
                
                if table.lower() in ('e', 'employees'):
                        
                        while True:
                        
                            name = input('Nombre: ')
                            last_name = input('Apellido: ')
                            
                            while True:
                                try:
                                    id_departament = int(input('Id del departamento: '))
                                    break
                                except ValueError as e:
                                    print('El id del departamento debe ser un número entero.')
                                
                            
                            if name != '' and last_name != '' and id_departament != '':
                                
                                employee = (name, last_name, id_departament)
                                insert_data_employees(employee)
                                print(f'Empleado {name} agregado con éxito')
                                break
                            else:
                                print('No pueden haber campos sin rellenar.')
                
                
                if table.lower() in ('d', 'departaments'):
                    
                    while True:
                        
                        name = input('Nombre: ')
                        
                        if name != '':
                            if not name.isnumeric():
                                departament = (name,)
                                insert_data_departaments(departament)
                                print(f'Departamento {name} agregado con éxito')
                                break
                            else:
                                print('El nombre debe contener solo letras')
                        else:
                            print('No pueden haber campos sin rellenar.')

            case '2':
                
                table = input('¿Qué tabla desea actualizar?(employees or departaments): ')
                
                    
                if table.lower() in ('e', 'employees'):
                    
                    while True:
                        
                        id_employee = int(input('Ingrese el id del empleado a actualizar: '))
                        
                        name = input('Nuevo nombre: ')
                        last_name = input('Nuevo apellido: ')
                        
                        while True:
                            try:
                                id_departament = int(input('Nuevo id del departamento: '))
                                break
                            except ValueError as e:
                                print('El id del departamento debe ser un número entero.')
                            
                        
                        if name != '' and last_name != '' and id_departament != '':
                            
                            employee = (name, last_name, id_departament, id_employee)
                            update_employees(employee)
                            print(f'Empleado {name} actualizado con éxito')
                            break
                        else:
                            print('No pueden haber campos sin rellenar.')
    
                
                    
                if table.lower() in ('d', 'departaments'):
                    
                    while True:
                        
                        id_departament = int(input('Ingrese el id del departamento a actualizar: '))
                        
                        name = input('Nombre: ')
                        
                        if name != '':
                            if not name.isnumeric():
                                departament = (name, id_departament)
                                update_departaments(departament)
                                print(f'Departamento {name} actualizado con éxito')
                                break
                            else:
                                print('El nombre debe contener solo letras')
                        else:
                            print('No pueden haber campos sin rellenar.')
            
            case '3':
                
                    table = input('¿Qué tabla desea eliminar?(employees or departaments): ')
                    
                
                    if table.lower() in ('e', 'employees'):
                        
                        while True:
                            
                            try:
                                id_employee = int(input('Ingrese el id del empleado a eliminar: '))
                                if id_employee != '':
                                    employee = (id_employee,)
                                    delete_employees(employee)
                                    break
                            except ValueError:
                                    print('El id del empleado debe ser un número entero.')
                    
            
                    
                    if table.lower() in ('d', 'departaments'):
                        
                        while True:
                            
                            try:
                                id_departament = int(input('Ingrese el id del empleado a eliminar: '))
                                if id_departament != '':
                                    departament = (id_departament,)
                                    delete_departaments(departament)
                                    break
                            except ValueError:
                                    print('El id del empleado debe ser un número entero.')
            case '4':
                break


if __name__ == '__main__':
    create_db()
    create_table()
    menu()