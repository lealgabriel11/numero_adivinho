from random import randint

p1= 999
p2 = 999
p3 = 999
n1 = "vazio"
n2 = "vazio"
n3 = "vazio"

contador = 1


print("""          ███  ███   ███   ███     ████   ███      ███  ████  ███ █   █ ███ █   █ █   █  ███            
           █░░█ ░░█ █ ░░░ █ ░░█    █░░░█ █ ░░█    █ ░░█ █░░░█  █░░█░  █░ █░░██  █░█░  █░█ ░░█           
████       █░░█░ ░█░█░ ██░█░ ░█░   █░░░█░█░ ░█░   █████░█░░░█░ █░░█░░ █░░█░░█░█ █░█████░█░ ░█░   ████   
 ░░░░   █  █░░█░░ █░█░░ █░█░░ █░░  █░░ █░█░░ █░░  █░░░█░█░░ █░░█░░ █░█ ░░█░░█░░██░█░░░█░█░░ █░░   ░░░░  
  ░░░░   ██ ░░ ███ ░░███ ░░███ ░░  ████ ░░███ ░░  █░░░█░████ ░███░  █ ░ ███░█░░ █░█░░░█░░███ ░░    ░░░░ 
          ░░ ░  ░░░ ░ ░░░ ░ ░░░ ░   ░░░░ ░ ░░░ ░   ░░  ░░░░░░ ░░░░   ░ ░ ░░░ ░░  ░░░░  ░░ ░░░ ░         
           ░░    ░░░   ░░░   ░░░     ░░░░   ░░░     ░   ░ ░░░░  ░░░   ░   ░░░ ░   ░ ░   ░  ░░░          """)


while True:
    numero_aleatorio = randint(1,15)

    print("================================")
    menu = print("--- opções 1-iniciar o jogo, 2-placar, 0-sair ---")
    op = input(">>> escolha uma opçao: ")


    if op  == "1":
        print("================================")
        while True:
            
            entrada_usuario = int(input(">>> escolha um numero de 1 a 15: "))

            if entrada_usuario > numero_aleatorio:
                print(f"o numero secreto é menor que {entrada_usuario}")

            elif entrada_usuario < numero_aleatorio:
                print(f"o numero secreto é maior que {entrada_usuario}")


            elif entrada_usuario == numero_aleatorio:
                print("================================")

                print("--- parabens voce conseguiu ---")
                print(f" --- numeros de tentativas: {contador} ---")

                nome = input("registre seu nome: ")

                if contador < p1:
                    p3 = p2
                    p2 = p1
                    p1 = contador

                    n3 = n2
                    n2 = n1
                    n1 = nome
                    
                elif contador < p2:
                    p3 = p2
                    p2 = contador

                    n3 = n2
                    n2 = nome

                elif contador < p3:
                    p3 = contador
                    
                    n3 = nome

                contador = 1
                break

            contador += 1


    elif op == "2":
        print("================================")
        print("placar de lideres: ")
        print(f"1°-{n1}, tentativas: {p1} \n2°-{n2}, tentativas: {p2}\n3°-{n3}, tentativas: {p3}")


    elif op == "0":
        print("programa encerrado")
        break
    

    else:
        print("coloque uma opção valida")
        
