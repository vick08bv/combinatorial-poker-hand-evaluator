# Combinatorial Poker Hand Evaluator

This project implements a **hand evaluator** that determines both the **type of hand** and a **numeric score** for ranking and comparison.  
The design is **general, clean, and combinatorial**: it applies to any number of ranks, suits, or hand sizes.

## Core Ideas

- **Hand Type via Frequency Signatures**  
  Hands are classified by sorting card ranks and computing a **frequency signature**.  
  This signature is matched against a precomputed dictionary of possible hand types.  
  Both the dictionary and the set of possible signatures were derived **combinatorially**.

- **Score Based on Positional Notation**  
  Each hand is also assigned a **positive integer score**, consistent with the standard hand ranking order.  
  - Simple to understand: it is based on positional notation.  
  - Easy to compute: score calculation only requires the card values sorted by their relative strength within the hand. 
  - Fully compatible with ranking comparisons: higher score = stronger hand.

- **Speed and Efficiency**  
  The evaluator is really fast, since classification is reduced to:  
  1. Obtaining the frequency signature.  
  2. Detecting a small set of special hands (e.g., flushes and straights).  
  No complex lookups or heavy computations are required at runtime.

## Analyses Included

The project also includes **exploratory analysis and visualization**:

- **Score distribution across hand rankings**  
  A plot showing how scores spread across categories, illustrating the consistency of the ranking system.

- **Flush vs. Straight rarity comparison**  
  Several plots comparing probabilities of flushes and straights under different configurations,  
  showing in which settings one becomes rarer than the other.

- **Speed test**  
  A quick script measuring how fast the evaluator can score and classify hands.

## Key Features

- **General applicability**: works for any number of ranks, suits, and hand sizes.  
- **Combinatorial foundation**: all probabilities, signatures, and structures come from first principles.  
- **Clear design**: modular, easy to extend, and mathematically grounded.  
- **Fast evaluation**: efficient scoring and classification.
