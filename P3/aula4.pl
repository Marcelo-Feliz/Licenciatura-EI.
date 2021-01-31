num(0).

num(X):- Y is X - 1, num(Y).

le(X,Y):- X < Y ; X = Y.

lt(X,Y):- X < Y.

soma(X,Y,R):- num(X) , num(Y) , R is X + Y.

mult(X,Y,R):- num(X) , num(Y) , R is X * Y.


