

len([], 0).
len([_|H], L ) :- len(H,N) , L is N+1.

equalOB(X,Y) :- len(X,T1), len(Y,T2), T1 >= T2.
bigger(X,Y)  :- len(X,T1), len(Y,T2), T1 > T2.
smaller(X,Y) :- len(X,T1), len(Y,T2), T1 < T2.


first(X,Y):- bigger(X,Y), !.
first(X,Y):- \+ equalOB(X,Y), !, fail.

first([0|X],[0|Y]):- first(X,Y), equalOB(X,Y), !.
first([1|X],[1|Y]):- first(X,Y), equalOB(X,Y), !.

first([1|_],[Y|_]):- Y=\=1, !.
first([1],Y):- equalOB(X,Y), !.

first([X|_],[1|_]):- X=\=1, fail.
first(X,[1]):- \+ !.




combinacao([X],Y):- K is X+Y+1 ,  combinacao([_|X],Y).
combinacao([X],Y):- X+1 = Y ,  combinacao([_|X],Y).
combinacao([X],Y):- K is X+Y+1 ,  combinacao([_|X],Y).









