clients = 'pablo,ricardo,rene,'

def create_client(client_name):
    global clients
    
    if client_name not in clients:
        clients += client_name + ','  # Agregar la coma directamente aquí
        list_clients()
    else:
        print('El cliente ya está en la lista de clientes')

def list_clients():
    global clients
    print('Lista de clientes:', clients)

def update_client(client_name, update_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name, update_client_name)
        list_clients()  # Muestra la lista actualizada después de la actualización
    else:
        print("El cliente no se encuentra")

def print_welcome():
    print('Bienvenidos a CRUD de ventas')
    print('*' * 50)
    print('¿Qué quieres hacer hoy?')
    print('[C]rear cliente')
    print('[A]ctualizar cliente')
    print('[E]liminar cliente')

def get_client():
    return input('¿Cuál es el nombre del cliente? ')

if __name__ == '__main__':
    print_welcome()
    
    commands = input().upper() 
    
    if commands == 'C':
        clients_name = get_client()
        create_client(clients_name)
        
    elif commands == 'D':
        pass  
    elif commands == 'A':
        clients_name = get_client()
        update_client_name = input('¿Cuál es el nombre del cliente actualizado? ')
        update_client(clients_name, update_client_name)
    else:
        print('Comando invalido')

