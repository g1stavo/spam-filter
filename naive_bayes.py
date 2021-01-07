#!/usr/bin/env python3

from utils import println

p_j = 0.5 # P(J)
p_j_f = 0.1 # P(F/J)
p_j_i = 0.1 # P(I/J)

p_j_text = p_j * p_j_f * p_j_i
println(p_j_text)

p_g = 0.5 # P(G)
p_g_f = 0.7 # P(F/G)
p_g_i = 0.2 # P(I/G)

p_g_text = p_g * p_g_f * p_g_i
println(p_g_text)

p_f_i = p_j_text + p_g_text
println('probability of words freedom and immigration being said:', p_f_i)

# P(J|F,I) = (P(J) * P(F|J) * P(I|J)) / P(F,I)
p_j_fi = p_j_text / p_f_i
println('probability of Jill Stein saying the words freedom and immigration:', p_j_fi)

# P(G|F,I) = (P(G) * P(F|G) * P(I|G)) / P(F,I)
p_g_fi = p_g_text / p_g_i
print('probability of Gary Johnson saying the words freedom and immigration:', p_g_fi)