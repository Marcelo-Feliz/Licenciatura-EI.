ReadMe:
Introdução:
No âmbito da unidade curricular de Metodologias de Desenvolvimento de Software pretende-se, com base na matéria e nos diagramas dados ao longo das aulas, nomeadamente diagramas de classe, diagramas de objetos, diagramas de use cases, máquinas de estados, diagramas de actividade, etc, representar um sistema informático que gere informações acerca de marcação de férias para varios colaboradores geridos por gestores usando UML para criar os diagramas necessários á representação deste problema.
Uses cases


Marcação de férias

 

Actor: Colaborador

Main Success Scenario :

    O colaborador preenche o seu nome de utilizador.

    De seguida é pedida a respectiva password.

    Sistema mostra as várias acções permitidas ao utilizador.

    O colaborador escolhe a opção de “Marcar férias”.

    O colaborador preenche a data de início.

    O colaborador preenche a data de fim.

    O sistema deve indicar o número de dias úteis do período marcado e respectiva pontuação.

    O sistema deve indicar o número dias de férias disponível para marcação.

    O sistema deve indicar que o período de férias se encontra a aguardar por validação do gestor.

    São mostradas a várias acções permitidas para o utilizador.

 

Extensions:

2.a)

    Colaborador introduziu um nome de utilizador ou password errada.

    Sistema indica “Nome de utilizador ou password errados”.

    Volta ao MSS no ponto 1.

5.a)

    Colaborador preenche uma data inválida.

    Sistema deve informar o colaborador do problema encontrado no ponto anterior.

    Volta ao MSS no ponto 3.

6.a)

    Colaborador preenche uma data inválida

    Sistema deve informar o colabora do problema encontrado no ponto anterior.

    Volta ao MSS no ponto 3.

6.b)

    Data de fim é posterior à data de início

    Sistema deve informar o colabora do problema encontrado no ponto anterior.

    Volta ao MSS no ponto 3.

6.c)

    O colaborador já não têm dias suficientes disponíveis para poder marcar o período indicado.

    Sistema deve informar o colaborador do problema encontrado no ponto anterior.

    Volta ao MSS no ponto 3.

Consulta de férias

 

Actor: Colaborador

Main Success Scenario :

    O colaborador preenche o seu nome de utilizador.

    De seguida é requerida a respectiva password.

    O sistema mostra as várias acções permitidas para o utilizador

    O Colaborador deve escolher a opção de “Consultar férias”

    O sistema deve mostrar todos os períodos de férias separados por estado.

    O sistema indica o nº dias de férias que o colaborador ainda tem disponíveis.

    São mostradas a várias acções permitidas para o utilizador

Extensions:

2.a)

    Sistema indica “Nome de utilizador ou password errados”.

    Volta ao MSS no ponto 1.

5.a)

    O colaborador não tem períodos de férias marcados.

    O Sistema informa que o utilizador não tem nenhum período de férias aprovado.

    Voltar ao MSS no ponto 6.


Validação de marcação de férias

 

Actor: Gestor

Main Success Scenario :

    O manager preenche o seu nome de utilizador.

    De seguida é requerida a respectiva password.

    O sistema mostra as várias acções permitidas para o utilizador

    O gestor deve escolher a opção de “Aprovar férias”

    O sistema deve mostrar todos os períodos de férias no estado “Por aprovar”.

    O gestor deve escolher o ID do período de férias a aprovar

    O Sistema deve mostrar a opção de “(A)provar ou (R)ejeitar”

    O gestor escolhe a opção Aprovar.

    Sistema indica que o período foi aprovado com sucesso.

    São mostradas as várias acções permitidas ao utilizador

Extensions:

2.a)

    Sistema indica “Nome de utilizador ou password errados”.

    Volta ao MSS no ponto 1.

5.a)

    O colaborador não tem períodos de férias marcados.

    O Sistema informa o manager que não tem nenhum período de férias por aprovar.

    Voltar ao MSS no ponto 9.

6.a)

    O manager indica um ID que não existe

    Sistema deve informar o manager do problema encontrado no ponto anterior.

    Voltar ao MSS no ponto 5.

7.a)

    O mager escolhe a opção de Rejeitar

    Sistema informa que o período de férias indicado foi rejeitado.

    Voltar ao MSS no ponto 10.


Decisões tomadas ao longo do trabalho:

Foram implementados alguns testes iniciais, e restantes ao longo do decorrer do trabalho.

O primeiro elemento a ser implementada foi o Login para Gestores e Colaboradores.

A partir do ponto anterior criámos 2 menus diferentes para os dois tipos de utilizadores.

Usámos uma LinkedList com todas as informações dos Colaboradores e outra para os Gestores.

Usando o metodo Calendar do java implemenou-se a marcação dos dias e envio para o Gestor aprovar.

Foi implementado a validação do Gestor e cancelamento de fárias que resultou em alguns erros de dias devolvidos e datas eliminadas.

Foram implementados mais metodos necesários para a resolução do problema alterior.

Todas as funcionalidades foram terminadas ainda que com alguns erros.

Foram feitos varios testes.

Todos os erros foram resolvidos e démos por completo o nosso trabalho.




