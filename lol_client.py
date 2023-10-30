import Pyro4

def main():
    with Pyro4.Proxy("PYRO:lol_server@localhost:9090") as server:
        while True:
            role = input("Digite uma rota (top, jungle, mid, adc, sup) ou 'exit' para sair: ")
            if role == 'exit':
                break
            champions = server.get_champions_by_role(role)
            print(f"Campeões da rota {role}: {', '.join(champions)}")

if __name__ == "__main__":
    main()