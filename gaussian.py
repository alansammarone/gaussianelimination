# -*- coding: utf-8 -*-


def pp(M):

    def eprint(*args):
        for i in args:
            print i,
        print

    for rows in M:
        A = ['{:<4}'.format(each) for each in rows]
        eprint(*A)

A = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
]

def gaussian_elimination(A):

    m = len(A)
    n = len(A[0])

    for k in range(min(m, n)):

        if A[k][k] != 0:

            for i in range(k):
                M = float(A[k][i]) / A[i][i]
                if M.is_integer():
                    if M < 0:
                        u = "(%s)" % int(M)
                    else:
                        u = "%s" % int(M)
                else:
                    u = "(%s / %s)" % (A[k][i], A[i][i])

                print "R%s → R%s - %s⋅R%s" % (k+1, k+1, u, i+1)

                A[k] = [n - A[i][p]*M for p,n in enumerate(A[k])]


    return A

pp(A)
A = gaussian_elimination(A)
print "----"
pp(A)

