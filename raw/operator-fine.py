# This snippet prints Fine parameter values for each semitone in Ableton Operator synth

for i in range(12):
	print(int(0.5 + 1000*2**(i/12.) - 1000))

# Output
# 0
# 59
# 122
# 189
# 260
# 335
# 414
# 498
# 587
# 682
# 782
# 888