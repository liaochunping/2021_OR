
import pivot as pi

A = [[-1, -10, -6, -15, 0, 0, 0, 0], [0, 1, 1, 3, 1, 0, 0, 2], [0, -1, -2, -4, 0, 1, 0, 3], [0, 1, 3, 5, 0, 0, 1, 4]]
BV = [4, 5, 6]
pi.pprint(A)
print("")

A, BV = pi.pivot(A, BV, 1, 3)
pi.pprint(A)
print("")

A, BV = pi.pivot(A, BV, 1, 1)
pi.pprint(A)