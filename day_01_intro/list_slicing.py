scores = [65,78,92,88,75,95,82,70,85,90]

top_3 = scores[-3:] # last 3
middle = scores[3:7] # score 4 to 7
everyother = scores[::2] # every 2nd score
rev_scores = scores[::-1]

print(top_3)
print(middle)
print(everyother)
print(rev_scores)

# Task 1: get first 5 scores
first_5_scores = scores[:5]
print(first_5_scores)

# Task 2: get every 3rd scores
every_3_scores = scores[3::]
print(every_3_scores)

# Task 3: get scores in reverse order
rev_scores = scores[::-1]
print(rev_scores)