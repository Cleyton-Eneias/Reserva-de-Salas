class reserva_visualizar:

    def __init__(self):
        reserva_visualizar.Login(self)
        self.opcao = input("Digite sua ação: 1- Visualizar| 2- Reservar| 3- Sair | 4- Cadastro de usuario | 5- Alterar Senha | 6- Criar Sala ")
        while(self.opcao != '3'):

            if ('1') in self.opcao:
                reserva_visualizar.visualizar(self)
                self.opcao = input("Digite sua ação: 1- Visualizar| 2- Reservar| 3- Sair | 4- Cadastro de usuario | 5- Alterar Senha | 6- Criar Sala ")
            if ('2') in self.opcao:
                reserva_visualizar.reserva(self)
                self.opcao = input("Digite sua ação: 1- Visualizar| 2- Reservar| 3- Sair | 4- Cadastro de usuario | 5- Alterar Senha | 6- Criar Sala ")
            if ('3') in self.opcao:
                print("Saindo do Sistema!")
                return
            if ('4') in self.opcao:
                reserva_visualizar.cadastraUsuario(self)
                self.opcao = input("Digite sua ação: 1- Visualizar| 2- Reservar| 3- Sair | 4- Cadastro de usuario | 5- Alterar Senha | 6- Criar Sala ")
            if ('5') in self.opcao:
                reserva_visualizar.alterarPassword(self)
                self.opcao = input("Digite sua ação: 1- Visualizar| 2- Reservar| 3- Sair | 4- Cadastro de usuario | 5- Alterar Senha | 6- Criar Sala ")
            if ('6') in self.opcao:
                reserva_visualizar.criarSala(self)
                self.opcao = input("Digite sua ação: 1- Visualizar| 2- Reservar| 3- Sair | 4- Cadastro de usuario | 5- Alterar Senha | 6- Criar Sala ")
            else:
                print('Digite um valor válido.')
                self.opcao = input("Digite sua ação: 1- Visualizar| 2- Reservar| 3- Sair | 4- Cadastro de usuario | 5- Alterar Senha | 6- Criar Sala ")




    def reserva(self):
        horariosReservadosDay = []
        self.dia = (input('Digite o dia que você deseja Reservar '))
        self.mes = (input('Digite o mes que você deseja Reservar '))
        self.sala = (input('Digite a sala que você deseja Reservar '))
        if(self.sala not in salas):
            print("Sala inválida")
            return reserva_visualizar.reserva(self)
        self.resp = (input('Digite a Responsavel da Reserva '))
        self.horarioIni =  input("Digite o Horario Inicial que deseja marcar: ")
        filtro = lambda x: x["dia"] == self.dia and x["mes"] == self.mes and x["sala"] == self.sala
        filtrados = list(filter(filtro,reservarList))
        validaHorario = self.horarioIni + ' ás ' + str(int(self.horarioIni) + 1)
        if(filtrados):
            if(validaHorario in filtrados[0]['horarioReserva']):
                print("Horario Já Cadastrado")
                print(filtrados)
            else:
                for i in range(len(reservarList)):
                    if reservarList[i]['dia'] == self.dia and reservarList[i]['mes'] == self.mes and self.sala == reservarList[i]['sala'] :
                        reservarList[i]['horarioReserva'].append(self.horarioIni + ' ás ' + str(int(self.horarioIni) + 1))
                print("Horario Cadastrado com sucesso!")
        else:
            horariosReservadosDay.append(self.horarioIni + ' ás ' + str(int(self.horarioIni) + 1))
            reservarList.append(
                {
                    'dia': self.dia,
                    'mes': self.mes,
                    'horarioReserva': horariosReservadosDay,
                    'sala': self.sala,
                    'responsavel': self.resp
                }
            )
            print("Horario Cadastrado com sucesso!")

    def visualizar(self):
        self.mes = (input('Digite o mes que você deseja Visualizar as Reservas: '))
        filtro = lambda x: x["mes"] == self.mes
        filtrados = list(filter(filtro, reservarList))
        if(filtrados):
            print(filtrados)
        else:
            print("Não Existe Reserva para esse mês: ")

    def cadastraUsuario(self):
        self.username = (input('Digite seu nome: '))
        filtro = lambda x: x['username'] == self.username
        filtrados = list(filter(filtro, usuarios))
        if (filtrados):
            print("Já existe usuario com esse nome")
            return
        self.password = (input('Digite sua senha: '))
        usuarios.append({
            'username':self.username,
            'password':self.password,
            'adm':True
        })

    def alterarPassword(self):
        self.username = (input('Digite seu nome: '))
        filtro = lambda x: x['username'] == self.username
        filtrados = list(filter(filtro, usuarios))
        if (filtrados):
            self.password = (input('Digite sua senha atual: '))
            if(filtrados[0]['password'] == self.password):
                self.password = (input('Digite sua nova senha: '))
                for i in range(len(usuarios)):
                    if usuarios[i]['username'] == self.username:
                        usuarios[i]['password'] = self.password
                print("Senha alterada com sucesso!")
                print(usuarios)
            else:
                print('Senha não condiz com o usuario')
        else:
            print('Usuario não cadastrado no sistema')

    def Login(self):
        self.username = (input('Digite seu nome: '))
        filtro = lambda x: x['username'] == self.username
        filtrados = list(filter(filtro, usuarios))
        if (filtrados):
            self.password = (input('Digite sua senha: '))
            if (filtrados[0]['password'] == self.password):
                self.adm = filtrados[0]['adm']
                print('Login Efetuado com Sucesso!')
            else:
                print("Senha Inválida")
                return reserva_visualizar.Login(self)
        else:
            print('Usuario não existe para fazer Login')
            return reserva_visualizar.Login(self)

    def criarSala(self):
        if(self.adm):
            self.sala = (input('Digite o nome da sala: '))
            filtro = lambda x: x == self.sala
            filtrados = list(filter(filtro, salas))
            if(filtrados):
                print('Sala com esse nome já cadastrada')
                return reserva_visualizar.criarSala(self)
            else:
                salas.append(self.sala)
                print('Sala cadastrada com sucesso!')
        else:
            print("Você não tem permissão para criar salas")


reservarList = []
horarioReserva = []
salas = ['Laboratorio 1']
usuarios = [
    {
        'username': 'Cleyton',
        'password':'123',
        'adm': False
    },
    {
        'username': 'admin',
        'password': 'admin',
        'adm': True
    }
]
a = reserva_visualizar()

