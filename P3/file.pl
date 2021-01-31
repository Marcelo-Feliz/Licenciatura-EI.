delete(L1, E, L2).
append(L1, L2, L3).

indexOf([Element|_], Element, 0). 
indexOf([_|Tail], Element, Index):- indexOf(Tail, Element, Index1), Index is Index1+1.

findelement([H|_],H).
findelement([_|L],X) :- findelement(L,X).

len([], 0).
len([_|H], L ) :- len(H,N) , L is N+1.

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

ex(X,(X,_)).

/*Estamos a assumir que não podem haver 2 ou mais codificações iguais*/
%flatten



len([], 0).
len([_|H], L ) :- len(H,N) , L is N+1.

isort(I, S) :- isort(I, [], S).
isort([], S, S).
isort([X|Xs], SI, SO) :- insord(X, SI, SX), isort(Xs, SX, SO).
insord(X, [], [X]).
insord(X, [A|As], [X,A|As]) :- \+calc(X,A).
insord(X, [A|As], [A|AAs]) :- calc(X,A), insord(X, As, AAs).

/*Cria uma lista com o elemento removido*/

%execute(L1, L2, E) :- isort(L1,L), indexOf(L,R,E), delete(L,R,L2).

%combinations(E,[],E).
%combinations(E,[L2|H],NTH) :- append(E,[L2],NTH); combinations(E,H,NTH).

%test(L1, NTH) :- isort(L1,L), combinations(E,).

ist_pairs(List1, List2, Pairs) :- findall((X,Y), (member(X, List1), member(Y, List2)), Pairs).

/*como fazer para parar esta recursividade até 6*/
recursividade(L1, L2, L1, 2).
recursividade(L1, L2, Pairs, K) :- H is K +1, ist_pairs(L1, L2, P), recursividade(P, L2, Pairs, H).

convert([],[]).
convert([L1|H],[L2|V]) :- ex(L2,L1), convert(H,V).

test(L, El) :- isort(L,L1), convert(L1,L2), recursividade(L2,L2,El,0).

%fuse(L1,L2) :- 

%compare(elemento, elemento) :-

%decode/dicionario :-

%array que guarda todas as iterações da recursividade




%combinations([], L2, Pairs).

%combinations([L1|H], [L2|K], Pairs) :- fuse(L1,L2,Pairs),  combinations( H , [L2|K], Pairs).


%combinations(E,[],E).

%combinations(E,[L2|H],NTH) :- fuse(E,[L2],NTH); combinations(E,H,NTH).

%combinations([L1|E],[L2|H],NTH) :- fuse([L1],[L2],NTH); combinations([L1|E],H,NTH).

%combinations([L1|E],L2,NTH) :- fuse([L1],L2,NTH); combinations(E,L2,NTH).




combinations(E,[L2|H],NTH) :- fuse(E,[L2],NTH); combinations(E,H,NTH).


cb([X|L],L2,H):- combinations([X],L2,H); cb(L,L2,H).




fuse([],L,L).
fuse([X|Xs],L,[X|Y]) :- fuse(Xs,L,Y).

