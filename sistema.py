class Sistema:
    
    def capturaOpcao(iteravel):
        while True:
            x = input("Escolha uma opção: ")
            if x in iteravel:
                return x
            print("Opcao Inválida")
            
    def capturaNome():
        while True:
            x = input("Digite o nome: ")  
            return x
        
    def capturaFloat():
        while True:
            x = input("Digite : ")  # sempre vem como string
            try:
                return float(x)  # tenta converter para float
            except ValueError:
                print("Valor inválido! Digite um número.")
    def capturaInt():
        while True:
            x = input("Digite o valor: ")  
            try:
                return int(x)  
            except ValueError:
                print("Valor inválido! Digite um número.")
                
    def capturaSenha():
        while True:
            x = input("Digite: ") 
            return x
    
    def capturaEmail():
        while True:
            x = input("Digite: ")
            if '@' in x:
                return x
            print("Email inválido")
