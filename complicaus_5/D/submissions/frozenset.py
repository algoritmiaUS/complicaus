def solve():
    # Diccionario global para asignar IDs únicos a cada conjunto único
    id_map = {}

    def get_id(s):
        """Asigna o recupera un ID entero para un frozenset dado."""
        if s not in id_map:
            id_map[s] = len(id_map)
        return id_map[s]

    try:
        # Leer número de casos de prueba
        line = input().strip()
        if not line: return
        t_cases = int(line)
        
        for _ in range(t_cases):
            # Para cada caso, reiniciamos la pila y el mapa de IDs
            stack = []
            id_map.clear()
            
            n_cmds = int(input().strip())
            
            for _ in range(n_cmds):
                cmd = input().strip()
                
                if cmd == "PUSH":
                    # Un conjunto vacío representado como frozenset
                    stack.append(frozenset())
                
                elif cmd == "DUP":
                    # Duplicar el elemento en el tope
                    stack.append(stack[-1])
                
                else:
                    # Operaciones binarias: sacamos los dos conjuntos de arriba
                    # A es el que estaba más arriba, B el que estaba debajo
                    set_a = stack.pop()
                    set_b = stack.pop()
                    
                    if cmd == "UNION":
                        res = set_a | set_b
                    
                    elif cmd == "INTERSECT":
                        res = set_a & set_b
                    
                    elif cmd == "ADD":
                        # ADD mete el ID de A dentro del conjunto B
                        # Usamos unión con un set de un solo elemento {id}
                        res = set_b | {get_id(set_a)}
                    
                    stack.append(res)
                
                # Imprimir el tamaño del conjunto resultante en el tope
                print(len(stack[-1]))
            
            print("***")
            
    except EOFError:
        pass

if __name__ == "__main__":
    solve()