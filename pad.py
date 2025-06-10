import itertools

string = "aaabbccdfd"

for char, group in itertools.groupby(string):
    print(char)
    print(sum(1 for _ in group))
