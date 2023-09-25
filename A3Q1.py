#Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Use dictionaries.

def most_frequent(input_string):
    letter_freq={}
    
    input_string=input_string.replace(" ","").lower()
    for i in input_string:
        if i.isalpha():
            if i in letter_freq:
                letter_freq[i] += 1
            else:
                letter_freq[i] = 1
                
    sorted_freq=sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)
    
    for a,b in sorted_freq:
        print(f"{a} : {b}")

most_frequent("MISSISSIPPI")
