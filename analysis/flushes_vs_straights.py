import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import ListedColormap, BoundaryNorm
from src import rank_generator

cmap = ListedColormap(['darkgray', 'black', 'firebrick'])
bounds = [-1.5, -0.1, 0.1, 1.5]
norm = BoundaryNorm(bounds, cmap.N)

x, y = 3, 3
fig, axes = plt.subplots(x, y, figsize=(12, 6))
for k, ax in enumerate(axes.flatten()):
    hand_size = k + 3

    flush = (tuple(hand_size * [1]), False, True, False)
    straight = (tuple(hand_size * [1]), True, False, False)

    number_values = np.arange(hand_size, hand_size + 10, 1)
    number_suits = np.arange(1, 6)

    v, s = np.meshgrid(number_values, number_suits)
    z = np.zeros_like(v, dtype=int)

    for i in range(v.shape[0]):
        for j in range(v.shape[1]):
            ranking, odds = rank_generator.generate_ranking(int(v[i][j]), int(s[i][j]), hand_size)
            flushes = odds.get(flush, 0)
            straights = odds.get(straight, 0)
            z[i, j] = - int(flushes > straights) + int(flushes < straights)

    sc = ax.scatter(v, s, s=10, c=z, cmap=cmap, norm=norm)

    ax.set_title("Hand Size: " + str(hand_size), y=1.1, fontsize=10, va="top")
    ax.tick_params(axis='both', which='major', labelsize=8)
    ax.set_xticks(number_values)
    ax.set_yticks(number_suits)

fig.suptitle('Relative Strength of Flushes and Straights', x=0.5 * (0.8+0.1), y=0.96, ha='center', fontsize=14)

fig.text(0.5 * (0.8+0.1), 0.04, 'Number of Values', ha='center', fontsize=10)
fig.text(0.04, 0.5, 'Number of Suits', va='center', rotation='vertical', fontsize=10)

cbar = fig.colorbar(sc, ax=axes.ravel().tolist(), boundaries=bounds, ticks=[-1, 0, 1],
                    fraction=0.1, pad=0.8, anchor=(0.1, 0.5), shrink=0.7)
cbar.set_ticklabels(['Straight beats Flush', 'Equal Probability', 'Flush beats Straight'])

fig.subplots_adjust(left=0.1, right=0.8, bottom=0.15, top=0.85, wspace=0.2, hspace=0.5)
plt.savefig('flushes_vs_straights.png', dpi=300)

