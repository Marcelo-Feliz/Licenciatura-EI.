homem(joao).
homem(rui).
homem(manuel).
homem(ricardo).
mulher(maria).
mulher(ana).
mulher(rita).
mulher(silvia).

progenitor(joao, maria).
progenitor(joao, rui).
progenitor(manuel, joao).
progenitor(ricardo, manuel).
progenitor(ana, rui).
progenitor(rita, joao).
progenitor(rita, silvia).

pai(X, Y) :- homem(X), progenitor(X, Y).
mae(X, Y) :- mulher(X), progenitor(X, Y).

avos(X, Y) :- progenitor(A, Y), progenitor(X, A).

antepassados(X, Y) :- progenitor(X,Y) ; progenitor(X,A) , antepassados(A,Y).

irmaos(X, Y) :- pai(A,Y), pai(A,X), X\=Y ; mae(A,Y), mae(A,X), X\=Y.

tios(X, Y) :- progenitor(A,Y), irmaos(X,A).

parentes(X, Y) :- antepassados(X,Y) ; antepassados(Y,X) ; (antepassados(C,Y) ; antepassados(Y,C)) ,(antepassados(C,X) ; antepassados(X,C)).