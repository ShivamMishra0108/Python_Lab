import random
import string


msg = "phone of shivam"

def coder(msg):
    words = msg.split()
    final_words = []

    for word in words:
        if(len(word)<3):
            final_words.append(word[::-1]) 
        
        else:
            start = ''.join(random.choices(string.ascii_letters,k=3))
            end = ''.join(random.choices(string.ascii_letters,k=3))

            modified = word[1:]+word[0]

            final_words.append(start+modified+end)

    return " ".join(final_words)

print(coder(msg))

def decoder(msg):
    words = msg.split()
    final_words = []

    for word in words:
        if(len(word)<3):
            final_words.append(word[::-1])

        else:
            stripped = word[3:-3]

            original = stripped[-1]+stripped[:-1]

            final_words.append(original)
    return " ".join(final_words)

encoded = coder(msg)

print("Encoded:", encoded)
print("Decoded:", decoder(encoded))