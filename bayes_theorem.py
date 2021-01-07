#!/usr/bin/env python3

from utils import println

p_diabetes = 0.01 # P(D)
p_no_diabetes = 0.99 # P(~D)
p_pos_diabetes = 0.9 # Sensitivity or P(Pos|D)
p_neg_no_diabetes = 0.9 # Specificity or P(Neg/~D)

# P(Pos) = (P(D) * Sensitivity) + (P(~D) * (1-Specificity))
p_pos = ((p_diabetes * p_pos_diabetes) 
    + (p_no_diabetes * (1 - p_neg_no_diabetes)))
println('probability of getting a positive test result:', p_pos)

# P(D/Pos) = (P(D) * Sensitivity)) / P(Pos)
p_diabetes_pos = (p_diabetes * p_pos_diabetes) / p_pos
println('probability of an individual having diabetes, \
given that individual got a positive test result:', p_diabetes_pos)

p_pos_no_diabetes = 0.1

# P(~D|Pos) = P(~D) * P(Pos|~D) / P(Pos)
p_no_diabetes_pos = (p_no_diabetes * p_pos_no_diabetes) / p_pos
print('probability of an individual not having diabetes, \
given that individual got a positive test result:', p_no_diabetes_pos)