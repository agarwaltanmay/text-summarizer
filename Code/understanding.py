# ARTIFICIAL INTELLIGENCE PROJECT - Automatic Story Summarization 

# ALGORITHM NAME - Information Extraction

#OWN
import MontyLingua

ml = MontyLingua.MontyLingua()

f1 = open('gift-of-magi.txt')
f2 = open('the-skylight-room.txt')
f3 = open('the-cactus.txt')

# OWN - read the files
text1 = f1.read()
text2 = f2.read()
text3 = f3.read()

# OWN - generates subject-verb-object-object tuples for each sentence
tuples1 = ml.jist_predicates(text1)
tuples2 = ml.jist_predicates(text2)
tuples3 = ml.jist_predicates(text3)

# OWN - flattens the above list of lists
ftuples1 = [item for sublist in tuples1 for item in sublist]
ftuples2 = [item for sublist in tuples2 for item in sublist]
ftuples3 = [item for sublist in tuples3 for item in sublist]

# OWN
# s-v-o-o tuple for a sentence is of form:
# ' "subject" "verb" "object" "object" '
# the following line removes the first and last space, "
# result: 'subject" "verb" "object" "object'
stuples1 = [w[2:-2] for w in ftuples1]
stuples2 = [w[2:-2] for w in ftuples2]
stuples3 = [w[2:-2] for w in ftuples3]

# OWN
# input: 'subject" "verb" "object" "object'
# output: [subject, verb, object, object]
btuples1 = [w.split('" "') for w in stuples1]
btuples2 = [w.split('" "') for w in stuples2]
btuples3 = [w.split('" "') for w in stuples3]

# OWN
# generates summary for the input
summary1 = ml.generate_summary(btuples1)
summary2 = ml.generate_summary(btuples2)
summary3 = ml.generate_summary(btuples3)

# OWN - print the summary generated for each story
print 'gift of magi:\n', summary1

print '\n\nthe skylight room:\n', summary2

print '\n\nthe cactus:\n', summary3