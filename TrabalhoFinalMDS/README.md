ReadMe:
Introdu��o:
No �mbito da unidade curricular de Metodologias de Desenvolvimento de Software pretende-se, com base na mat�ria e nos diagramas dados ao longo das aulas, nomeadamente diagramas de classe, diagramas de objetos, diagramas de use cases, m�quinas de estados, diagramas de actividade, etc, representar um sistema inform�tico que gere informa��es acerca de marca��o de f�rias para varios colaboradores geridos por gestores usando UML para criar os diagramas necess�rios � representa��o deste problema.
Uses cases


Marca��o de f�rias

 

Actor: Colaborador

Main Success Scenario :

    O colaborador preenche o seu nome de utilizador.

    De seguida � pedida a respectiva password.

    Sistema mostra as v�rias ac��es permitidas ao utilizador.

    O colaborador escolhe a op��o de �Marcar f�rias�.

    O colaborador preenche a data de in�cio.

    O colaborador preenche a data de fim.

    O sistema deve indicar o n�mero de dias �teis do per�odo marcado e respectiva pontua��o.

    O sistema deve indicar o n�mero dias de f�rias dispon�vel para marca��o.

    O sistema deve indicar que o per�odo de f�rias se encontra a aguardar por valida��o do gestor.

    S�o mostradas a v�rias ac��es permitidas para o utilizador.

 

Extensions:

2.a)

    Colaborador introduziu um nome de utilizador ou password errada.

    Sistema indica �Nome de utilizador ou password errados�.

    Volta ao MSS no ponto 1.

5.a)

    Colaborador preenche uma data inv�lida.

    Sistema deve informar o colaborador do problema encontrado no ponto anterior.

    Volta ao MSS no ponto 3.

6.a)

    Colaborador preenche uma data inv�lida

    Sistema deve informar o colabora do problema encontrado no ponto anterior.

    Volta ao MSS no ponto 3.

6.b)

    Data de fim � posterior � data de in�cio

    Sistema deve informar o colabora do problema encontrado no ponto anterior.

    Volta ao MSS no ponto 3.

6.c)

    O colaborador j� n�o t�m dias suficientes dispon�veis para poder marcar o per�odo indicado.

    Sistema deve informar o colaborador do problema encontrado no ponto anterior.

    Volta ao MSS no ponto 3.

Consulta de f�rias

 

Actor: Colaborador

Main Success Scenario :

    O colaborador preenche o seu nome de utilizador.

    De seguida � requerida a respectiva password.

    O sistema mostra as v�rias ac��es permitidas para o utilizador

    O Colaborador deve escolher a op��o de �Consultar f�rias�

    O sistema deve mostrar todos os per�odos de f�rias separados por estado.

    O sistema indica o n� dias de f�rias que o colaborador ainda tem dispon�veis.

    S�o mostradas a v�rias ac��es permitidas para o utilizador

Extensions:

2.a)

    Sistema indica �Nome de utilizador ou password errados�.

    Volta ao MSS no ponto 1.

5.a)

    O colaborador n�o tem per�odos de f�rias marcados.

    O Sistema informa que o utilizador n�o tem nenhum per�odo de f�rias aprovado.

    Voltar ao MSS no ponto 6.


Valida��o de marca��o de f�rias

 

Actor: Gestor

Main Success Scenario :

    O manager preenche o seu nome de utilizador.

    De seguida � requerida a respectiva password.

    O sistema mostra as v�rias ac��es permitidas para o utilizador

    O gestor deve escolher a op��o de �Aprovar f�rias�

    O sistema deve mostrar todos os per�odos de f�rias no estado �Por aprovar�.

    O gestor deve escolher o ID do per�odo de f�rias a aprovar

    O Sistema deve mostrar a op��o de �(A)provar ou (R)ejeitar�

    O gestor escolhe a op��o Aprovar.

    Sistema indica que o per�odo foi aprovado com sucesso.

    S�o mostradas as v�rias ac��es permitidas ao utilizador

Extensions:

2.a)

    Sistema indica �Nome de utilizador ou password errados�.

    Volta ao MSS no ponto 1.

5.a)

    O colaborador n�o tem per�odos de f�rias marcados.

    O Sistema informa o manager que n�o tem nenhum per�odo de f�rias por aprovar.

    Voltar ao MSS no ponto 9.

6.a)

    O manager indica um ID que n�o existe

    Sistema deve informar o manager do problema encontrado no ponto anterior.

    Voltar ao MSS no ponto 5.

7.a)

    O mager escolhe a op��o de Rejeitar

    Sistema informa que o per�odo de f�rias indicado foi rejeitado.

    Voltar ao MSS no ponto 10.


Decis�es tomadas ao longo do trabalho:

Foram implementados alguns testes iniciais, e restantes ao longo do decorrer do trabalho.

O primeiro elemento a ser implementada foi o Login para Gestores e Colaboradores.

A partir do ponto anterior cri�mos 2 menus diferentes para os dois tipos de utilizadores.

Us�mos uma LinkedList com todas as informa��es dos Colaboradores e outra para os Gestores.

Usando o metodo Calendar do java implemenou-se a marca��o dos dias e envio para o Gestor aprovar.

Foi implementado a valida��o do Gestor e cancelamento de f�rias que resultou em alguns erros de dias devolvidos e datas eliminadas.

Foram implementados mais metodos neces�rios para a resolu��o do problema alterior.

Todas as funcionalidades foram terminadas ainda que com alguns erros.

Foram feitos varios testes.

Todos os erros foram resolvidos e d�mos por completo o nosso trabalho.




