# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
len(it_companies)

# Add 'Twitter' to it_companies
it_companies.add('Twitter')

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Snap', 'ByteDance'])

# Remove one of the companies from the set it_companies
it_companies.remove('Twitter')

# What is the difference between remove and discard
'''the remove method will raise an error if an item is not found in the set
the discard method will not raise an error if the item is not found in the set'''

# Join A and B
C = A.union(B)
# A.update(B)

# Find A intersection B
A.intersection(B)

# Is A subset of B
B.issubset(A)  # False

# Are A and B disjoint sets
A.isdisjoint(B)  # False

# Join A with B and B with A

# What is the symmetric difference between A and B
B.symmetric_difference(A)

# Delete the sets completely
del A, B

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?

# convert list to set
age_set = set(age)
# find lengths
set_length = len(age_set)
list_length = len(age)
# list is bigger because it contains duplicate items.
# a set does not contain duplicates


# "I am a teacher and I love to inspire and teach people." How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

sentence = "I am a teacher and I love to inspire and teach people."
sentence_as_list = sentence.split()

sentence_as_set = set(sentence_as_list)
unique_words_count = len(sentence_as_set)
print(f'There are {unique_words_count} unique words in the sentence')
