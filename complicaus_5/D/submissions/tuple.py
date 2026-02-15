def solve():
    id_map = {}

    def get_id(s_tuple):
        """s_tuple ya debe venir como una tupla ordenada."""
        if s_tuple not in id_map:
            id_map[s_tuple] = len(id_map)
        return id_map[s_tuple]

    try:
        line = input().strip()
        if not line: return
        t_cases = int(line)
        
        for _ in range(t_cases):
            stack = [] # Guardaremos tuplas ordenadas aquí
            id_map.clear()
            
            n_cmds = int(input().strip())
            
            for _ in range(n_cmds):
                cmd = input().strip()
                
                if cmd == "PUSH":
                    # Un conjunto vacío es una tupla vacía
                    stack.append(())
                
                elif cmd == "DUP":
                    stack.append(stack[-1])
                
                else:
                    # Sacamos las tuplas
                    tuple_a = stack.pop()
                    tuple_b = stack.pop()
                    
                    # Convertimos a set temporalmente para operar
                    set_a = set(tuple_a)
                    set_b = set(tuple_b)
                    
                    if cmd == "UNION":
                        res_set = set_a | set_b
                    elif cmd == "INTERSECT":
                        res_set = set_a & set_b
                    elif cmd == "ADD":
                        # Añadimos el ID de A al set B
                        set_b.add(get_id(tuple_a))
                        res_set = set_b
                    
                    # Convertimos el resultado de vuelta a tupla ordenada
                    # Esto es lo que permite que id_map lo reconozca
                    stack.append(tuple(sorted(res_set)))
                
                # El tamaño es la cantidad de elementos en la tupla
                print(len(stack[-1]))
            
            print("***")
            
    except EOFError:
        pass

if __name__ == "__main__":
    solve()