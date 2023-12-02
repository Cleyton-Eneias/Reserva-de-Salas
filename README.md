# Reserva-de-Salas
O projeto consiste em um sistema de reservas de salas, desenvolvido em Python utilizando a programação orientada a objetos. O sistema é projetado para ser utilizado em ambientes onde há a necessidade de gerenciar a reserva de salas em diferentes horários, como em instituições educacionais, empresas ou espaços compartilhados.


# Documentação do Código
1. Classe reserva_visualizar
1.1 Método __init__(self)
O método de inicialização da classe é responsável por iniciar a interação com o usuário, solicitando o login e apresentando um menu de opções. O loop while permite que o usuário selecione diferentes ações até escolher sair.

Atributos:

opcao: Armazena a opção escolhida pelo usuário.
Fluxo do Método:

Solicita o login através do método Login.
Apresenta um menu de opções.
Entra em um loop enquanto o usuário não escolhe a opção de sair (3).
Executa a ação correspondente à escolha do usuário.
Se a opção não for válida, solicita novamente.
1.2 Métodos de Ação (reserva, visualizar, cadastraUsuario, alterarPassword, criarSala)
Cada um desses métodos executa uma ação específica com base na escolha do usuário.

reserva(self):

Solicita informações para a reserva (dia, mês, sala, responsável, horário inicial).
Verifica se a sala é válida.
Verifica se o horário já está reservado.
Adiciona a reserva à lista reservarList.
visualizar(self):

Solicita o mês desejado.
Filtra as reservas pelo mês e exibe o resultado.
cadastraUsuario(self):

Solicita nome de usuário e senha.
Verifica se o nome de usuário já está em uso.
Adiciona o novo usuário à lista usuarios.
alterarPassword(self):

Solicita nome de usuário e senha atual.
Verifica se a senha atual corresponde.
Solicita e atualiza a senha do usuário.
criarSala(self):

Verifica se o usuário tem permissão de administrador.
Solicita o nome da sala.
Verifica se a sala já existe.
Adiciona a nova sala à lista salas.
1.3 Método Login(self)
Solicita o nome de usuário e senha para realizar o login. Verifica a validade das credenciais.

1.4 Atributos Globais
reservarList: Lista que armazena as reservas.
salas: Lista que contém os nomes das salas disponíveis.
usuarios: Lista de usuários cadastrados.
2. Instância da Classe
Uma instância da classe reserva_visualizar é criada no final do código (a = reserva_visualizar()), iniciando assim a execução do programa.

