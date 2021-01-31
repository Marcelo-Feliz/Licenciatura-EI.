minimo(X,Y,X) :- X =< Y.
minimo(X,Y,Y) :- Y = X.

membro(X,[X|_]):- !.
membro(X,[_|T]):- membro(X,T).

naomembro(X,[H|T]) :- X \= H, naomembro(X,T).
naomembro(_,[]).

factorial(0,1).
factorial(N,F):- N>0,
                TMP is N-1,
                factorial(TMP,F2),
                F is F2*N.

SUMLIST([],0).
SUMLIST([X|T],S):-
                SUMLIST(T,TMP),
                S is TMP+X.

LENLIST([_|T],C):- LENLIST(T,S)C is S+1.