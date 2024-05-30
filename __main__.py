from gestion_bd import SetUp, OperationsDataBase

def menu():
    
    set_up = SetUp()
    operations_db = OperationsDataBase()
    
    set_up.create_db()
    set_up.create_table()
    
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
                                operations_db.insert_data_employees(employee)
                                print(f'Empleado {name} agregado con éxito')
                                break
                            else:
                                print('No pueden haber campos sin rellenar.')
                
                
                elif table.lower() in ('d', 'departaments'):
                    
                    while True:
                        
                        name = input('Nombre: ')
                        
                        if name != '':
                            if not name.isnumeric():
                                departament = (name,)
                                operations_db.insert_data_departaments(departament)
                                print(f'Departamento {name} agregado con éxito')
                                break
                            else:
                                print('El nombre debe contener solo letras')
                        else:
                            print('No pueden haber campos sin rellenar.')
                
                else:
                    print(f'La tabla {table} no existe, intente nuevamente')


            case '2':
                
                table = input('¿Qué tabla desea actualizar?(employees or departaments): ')
                
                    
                if table.lower() in ('e', 'employees'):
                    
                    while True:
                        
                        while True:
                            try:
                                id_employee = int(input('Ingrese el id del empleado a actualizar: '))
                                break
                            except  ValueError:
                                print('El id debe ser un número entero.')
                        
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
                            operations_db.update_employees(employee)
                            print(f'Empleado {name} actualizado con éxito')
                            break
                        else:
                            print('No pueden haber campos sin rellenar.')
    
                
                    
                elif table.lower() in ('d', 'departaments'):
                    
                    while True:
                        
                        id_departament = int(input('Ingrese el id del departamento a actualizar: '))
                        
                        name = input('Nombre: ')
                        
                        if name != '':
                            if not name.isnumeric():
                                departament = (name, id_departament)
                                operations_db.update_departaments(departament)
                                print(f'Departamento {name} actualizado con éxito')
                                break
                            else:
                                print('El nombre debe contener solo letras')
                        else:
                            print('No pueden haber campos sin rellenar.')
                            
                else:
                    print(f'La tabla {table} no existe, intente nuevamente')
            
            case '3':
                
                    table = input('¿Qué tabla desea eliminar?(employees or departaments): ')
                    
                
                    if table.lower() in ('e', 'employees'):
                        
                        while True:
                            
                            try:
                                id_employee = int(input('Ingrese el id del empleado a eliminar: '))
                                if id_employee != '':
                                    employee = (id_employee,)
                                    operations_db.delete_employees(employee)
                                    break
                            except ValueError:
                                    print('El id del empleado debe ser un número entero.')
                    
            
                    
                    elif table.lower() in ('d', 'departaments'):
                        
                        while True:
                            
                            try:
                                id_departament = int(input('Ingrese el id del empleado a eliminar: '))
                                if id_departament != '':
                                    departament = (id_departament,)
                                    operations_db.delete_departaments(departament)
                                    break
                            except ValueError:
                                    print('El id del empleado debe ser un número entero.')
                                    
                    else:
                        print(f'La tabla {table} no existe, intente nuevamente')
            case '4':
                break


if __name__ == '__main__':
    menu()

