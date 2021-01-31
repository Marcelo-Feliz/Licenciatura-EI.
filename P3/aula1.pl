homem(joao).
homem(rui).
mulher(maria).
mulher(ana).
progenitor(joao,maria).
progenitor(ana,maria).
progenitor(joao,rui).
pai(X,Y):- homem(X), progenitor(X,Y).
mae(X,Y):- mulher(X), progenitor(X,Y).
