# Lecture 1 - Pig Latin

def pig_latin(word):
    """
        Given a word, moves first letter to end if consonant and repeats until first vowel found. Then, adds 'ay' to end of word and returns word.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Base case: word starts with vowel:
    if word[0].lower() in vowels:
        return word + 'ay'
    else:
        # If word contains no vowels:
        if all(char not in vowels for char in word):
            return word
        else:
            # Recursive case: word starts with consonant:
            word = word[1:] + word[0]
            return pig_latin(word)
    

# Lecture 2 - Buzz

def buzz(number):
    """
        Counts until given positive number, printing the number or, if the number is divisible by 7 or contains a 7 digit, prints 'buzz' instead.
    """

    for num in range(1, number + 1):
        if num % 7 == 0 or '7' in str(num):
            print('buzz')
        else: 
            print(num)

buzz(17)