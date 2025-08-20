import numpy as np
import time
from src import rank_generator, hand_evaluator, score_system

hand_size = 5
sample_size = 1000000
number_values, number_suits, ace_value, alt_value = 13, 4, 14, 1
ranking, odds = rank_generator.generate_ranking(number_values, number_suits, hand_size)
max_rank, total = max(ranking.values()), sum(odds.values())

cards_range = list(range(number_values * number_suits))
cards = [(i, j) for i in range(2, 15) for j in range(1, 5)]

samples = [np.random.choice(cards_range, 5, replace=False) for i in range(sample_size)]
hands = [[cards[i] for i in hand] for hand in samples]

start_time = time.time()
for hand in hands:
    sorted_cards, frequencies, is_straight, is_flush, is_royal_flush = \
        hand_evaluator.evaluate_hand(hand, ace_value, alt_ace_value=alt_value)
    sorted_values = [card[0] for card in sorted_cards]
    hand_rank = ranking[(frequencies, is_straight, is_flush, is_royal_flush)]
    hand_score = score_system.log_score(sorted_values, hand_rank, ace_value)

end_time = time.time()
elapsed = end_time - start_time
print(f'Total execution time for evaluating {sample_size} hands: {elapsed:.3f} seconds')
