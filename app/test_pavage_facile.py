
# code recopié depuis https://www.xoolive.org/2016/02/29/pavage-par-tatamis.html
import matplotlib.pyplot as plt
import seaborn as sns
import facile

def tatami(xmax, ymax):

    # On ne travaille pas avec des demi-tatamis
    assert (xmax * ymax) & 1 == 0
    n = xmax * ymax // 2

    # Définitions des variables, x, y et direction
    # d = 1 => horizontal, d = 0 => vertical
    x = [facile.variable(0, xmax-1) for i in range(n)]
    y = [facile.variable(0, ymax-1) for i in range(n)]
    d = [facile.variable(0, 1) for i in range(n)]

    # Les tatamis ne sortent pas du cadre
    for i in range(n):
        facile.constraint(x[i] + 1 + d[i] <= xmax)
        facile.constraint(y[i] + 2 - d[i] <= ymax)

    # Les tatamis ne se chevauchent pas
    for i in range(n-1):
        for j in range(i+1, n):
            left = x[i] + 1 + d[i] <= x[j]
            right = x[i] >= x[j] + 1 + d[j]
            above = y[i] + 2 - d[i] <= y[j]
            below = y[i] >= y[j] + 2 - d[j]
            facile.constraint(left | right | above | below)

    # Impossible d'avoir 4 tatamis qui se rejoignent en un point
    for i in range(n-1):
        for j in range(i+1, n):
            left = x[i] + 1 + d[i] != x[j]
            below = y[i] + 2 - d[i] != y[j]
            facile.constraint(left | below)

    # On casse les symétries
    for i in range(n-1):
        facile.constraint(x[i] <= x[i+1])
        facile.constraint((x[i] != x[i+1]) | (y[i] < y[i+1]))

    return facile.solve_all(x+y+d)

sns.set(style='whitegrid', palette='Set2')
sns.despine()

def fill_square(ax, x, y, xs, ys):
    ax.fill([x, x, x+xs, x+xs], [y, y+ys, y+ys, y])

def plot_sol(ax, x, y, d, xmax, ymax):
    for (xi, yi, di) in zip(x, y, d):
        fill_square(ax, xi, yi, 1+di, 2-di)

    ax.set_xlim((0, xmax))
    ax.set_ylim((0, ymax))
    ax.set_aspect(1)
    ax.set_xticks(range(xmax + 1))
    ax.set_yticks(range(ymax + 1))

def plot_tatami(sol, xmax, ymax):
    n = xmax * ymax // 2
    fig, ax = plt.subplots(ncols=len(sol), nrows=1,
                           figsize=(4*len(sol), 4))

    for i in range(len(sol)):
        x = sol[i][0:n]
        y = sol[i][n:2*n]
        d = sol[i][2*n:]
        plot_sol(ax[i], x, y, d, xmax, ymax)

sol=tatami(6,5)


print(sol)