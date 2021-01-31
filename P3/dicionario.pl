/*_________________________Ordenar a lista por ordem de menor para maior__________________________*/
/*_Quando a codificação é do mesmo tamanho a ordem é feita para que os 0's apareçam antes dos 1's_*/
/*______________Estamos a assumir que não podem haver 2 ou mais codificações iguais_______________*/

equalOB(X,Y) :- len(X,T1), len(Y,T2), T1 >= T2.
bigger(X,Y)  :- len(X,T1), len(Y,T2), T1 > T2.

first(X,Y):- bigger(X,Y), !.
first(X,Y):- \+ equalOB(X,Y), !, fail.
first([0|X],[0|Y]):- first(X,Y), equalOB(X,Y), !.
first([1|X],[1|Y]):- first(X,Y), equalOB(X,Y), !.
first([1|_],[Y|_]):- Y=\=1, !.
first([1],Y):- equalOB(X,Y), !.
first([X|_],[1|_]):- X=\=1, fail.
first(X,[1]):- \+ !.

calc((_,X),(_,Y)) :- first(X,Y).

ex(X,(_,X)).

len([], 0).
len([_|H], L ) :- len(H,N) , L is N+1.

isort(I, S) :- isort(I, [], S).
isort([], S, S).
isort([X|Xs], SI, SO) :- insord(X, SI, SX), isort(Xs, SX, SO).
insord(X, [], [X]).
insord(X, [A|As], [X,A|As]) :- \+calc(X,A).
insord(X, [A|As], [A|AAs]) :- calc(X,A), insord(X, As, AAs).
/*________________________________________________________________________________________________*/


/*____________________________Faz todas as combinações dadas 2 listas_____________________________*/

fuse([],L,L).
fuse([X|Xs],L,[X|Y]) :- fuse(Xs,L,Y).

combinations(E,[L2|H],NTH) :- fuse(E,[L2],NTH); combinations(E,H,NTH).

cb([X|L],L2,H):- combinations([X],L2,H); cb(L,L2,H).

equals(P,P).

finalCombin(L1,L2,H,T) :- equals(P,H), cb(L1,L2,P); \+equals(T,3), I is T+1, finalCombin(L1,L2,P,I), combinations(P,L2,H).

ex(X,(_,X)).
convert([],[]).
convert([L1|H],[L2|V]) :- ex(L2,L1), convert(H,V).
/*________________________________________________________________________________________________*/

finalTemp(L,P) :- isort(L,L1), convert(L1,L2), finalCombin(L2,L2,H,0), flatten(H,P). 

example(Y,X) :- findall(Z,finalTemp(Y,Z),Z), isort(Y,Y1) ,convert(Y1,C), fuse(C,Z,X).

duplicate(D, V) :- example(D,L), select(V, L, L1), member(V, L1).


%findall -> detectar duplicados






