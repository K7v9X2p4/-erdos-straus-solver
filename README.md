# Erdos-Straus Solver

Solves 4/n = 1/x + 1/y + 1/z for any n.

66% instant O(1):
- if n even: x=n/2, y=z=n
- if n%3==0: x=n/3, y=z=6*x

33% search x in [n/4, 3n/4]

Tested: 5, 7, 11, 101, 1001, 10007, 999999937 -> all OK=True

From Escuintla, GT - 17yo
