import Pyro4

champions = {
    'top': ['Aatrox', 'Camille', 'Garen', 'Irelia'],
    'jungle': ['Amumu', 'Evelynn', 'Graves', 'Lee Sin'],
    'mid': ['Ahri', 'Annie', 'Orianna', 'Syndra'],
    'adc': ['Ashe', 'Ezreal', 'Jhin', 'Miss Fortune'],
    'sup': ['Braum', 'Leona', 'Morgana', 'Thresh'],
}

@Pyro4.expose
class LOLServer(object):
    def get_champions_by_role(self, role):
        if role in champions:
            return champions[role]
        else:
            return "Rota não encontrada"

def main():
    Pyro4.config.NS_HOST = 'localhost'
    Pyro4.config.NS_PORT = 9090
    Pyro4.Daemon.serveSimple(
        {
            LOLServer: "lol_server"
        },
        host="localhost",
        port=9090,
        ns=False
    )

if __name__ == "__main__":
    main()