


membro(X,[X|_]).
membro(X,[_|T]):- membro(X,T).

prefixo([],H).
prefixo([X|T],[X|H]):- prefixo(T,H).

sufixo(X,X).
sufixo(X,[T|H]):- sufixo(X,H).


sublista(X,X).
sublista(X,[T|H]):- sublista(X,H).
sublista([X|T],[X|H]):- sublista(T,H).


