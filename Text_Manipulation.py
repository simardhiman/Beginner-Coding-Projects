def reverse_string(text):
    return text[::-1]

def count_words(text):
    words = text.split()
    return len(words)

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join([c for c in text if c not in vowels])

while True:
    # Get user input
    text = input("Enter a sentence or type 'exit' to quit: ")
    if text == "exit":
        break
    # Perform text manipulation
    print("Reversed string:", reverse_string(text))
    print("Number of words:", count_words(text))
    print("String without vowels:", remove_vowels(text))
    print()
