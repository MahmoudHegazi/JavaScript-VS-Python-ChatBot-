import random
import words
import time


def silly_string(nouns, verbs, templates):
    # Choose a random template.
    template = random.choice(templates)

    # We'll append strings into this list for output.
    output = []

    # Keep track of where in the template string we are.
    index = 0
    mynoun = "{{noun}}"
    myverb = "{{verb}}"
    # Add a while loop here.
    while index < len(template):
        if template[index : index +  len(mynoun)] == "{{noun}}":
             output.append(random.choice(nouns))
             index += 8
        elif template[index : index + len(myverb)] == "{{verb}}":
             output.append(random.choice(verbs))
             index += 8
        else: 
             output.append(template[index])
             index += 1  
    # After the loop has finished, join the output and return it.
        mystring = "".join(output)
    return mystring
for side in range(50):
   print(silly_string(words.nouns, words.verbs,
        words.templates))
   time.sleep(1)