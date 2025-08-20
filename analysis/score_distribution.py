import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from src import rank_generator, hand_evaluator, score_system

hand_size = 5
sample_size = 1000000
number_values, number_suits, ace_value, alt_value = 13, 4, 14, 1
ranking, odds = rank_generator.generate_ranking(number_values, number_suits, hand_size)
max_rank, total = max(ranking.values()), sum(odds.values())
hand_names = [
    'High card', 'Pair', 'Two Pair', 'Three of a Kind', 'Straight',
    'Flush', 'Full House', 'Four of a Kind', 'Straight Flush', 'Royal Flush'
]

cards_range = list(range(number_values * number_suits))
cards = [(i, j) for i in range(2, 15) for j in range(1, 5)]

samples = [np.random.choice(cards_range, 5, replace=False) for i in range(sample_size)]
hands = [[cards[i] for i in hand] for hand in samples]

hand_scores = []
for hand in hands:
    sorted_cards, frequencies, is_straight, is_flush, is_royal_flush = \
        hand_evaluator.evaluate_hand(hand, ace_value, alt_ace_value=alt_value)
    sorted_values = [card[0] for card in sorted_cards]
    odd = odds[(frequencies, is_straight, is_flush, is_royal_flush)]
    hand_rank = ranking[(frequencies, is_straight, is_flush, is_royal_flush)]
    hand_score = score_system.log_score(sorted_values, hand_rank, ace_value)
    hand_scores.append((hand_rank, hand_score, odd))

quantiles = np.linspace(0, 1, sample_size)
hand_scores.sort(key=lambda tup: tup[1])
ranks, scores, odds = list(zip(*hand_scores))

cmap = plt.get_cmap('tab10')
colors = [cmap(val/9) for val in ranks]

fig, ax = plt.subplots(figsize=(8, 6))
sc = ax.scatter(quantiles, scores, s=10, c=colors)
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label=hand_names[i],
           markerfacecolor=cmap(i), markersize=8)
    for i in range(len(hand_names)-1, -1, -1)
]
ax.legend(handles=legend_elements, title='Hand Rankings')

fig.suptitle('Score distribution by Hand Type', fontsize=14)
ax.set_xlabel('Quantile')
ax.set_ylabel('Log Base 15 Score')

plt.tight_layout()
fig.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
plt.savefig('score_distribution.png', dpi=300)
