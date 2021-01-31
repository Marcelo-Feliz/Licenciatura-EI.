adj(X,Y,[X,Y|_]).
adj(X,Y,[Y,X|_]).
adj(X,Y,[_|K]):-adj(X,Y,K).


sel(A, [A|B], B).
sel(A, [B, C|D], [B|E]) :- sel(A, [C|D], E).


somatorio([],0).
somatorio([H|T],S):-somatorio(T,G),S is H+G.


ord([]).
ord([_]).
ord([X,Y|Z]):- X =< Y , ord([Y|Z]).


perm([],[]).
perm([X|Y],Z) :- sel(X,Z,W), perm(Y,W) .


sort([],[]).
sort(X,Y):- ord(Y).



