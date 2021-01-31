sort(+List, -Sorted).




pairs(List1, List2, Pairs):- findall((X,Y), (member(X, List1), member(Y, List2)), Pairs).


dict(X,Y):- [[_|Y]|_].


teste(X, Pairs):- pairs(X, X, Pairs).





