"""
Question 081 - Level 03
Please write a program to generate all sentences where subject is in ["I", "You"] and the object is in ["Hockey",
"Football"].
Hints: Use list[index] notation to get a element from a list.
--- Nguyen Van Duc ---
"""
subjects = ["I", "You"]
verbs = ["Hockey", "Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(subjects)):
            sentence = "%s %s %s." % (subjects[i], verbs[j], subjects[k])
            print(sentence)
