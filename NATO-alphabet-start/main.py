import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create the dictionary in a single line using dictionary comprehension
phonetic_dict = {row.letter: row.code for row in data.itertuples()}

def get_phonetic_codes(word): # the input "word" derive from.. 🔴
    """Converts a word to a list of phonetic codes"""
    letters = list(word) # input ALVIN, output: ['A', 'L', 'V', 'I', 'N']
    output_list = [phonetic_dict[letter] for letter in letters]
    return  output_list

while True:
    # Get user input and convert to uppercase
    userInput = input("Please insert a word: ").upper()

    #Get the phonetic codes
    phonetic_code = get_phonetic_codes(userInput) # Here! .. 🔴
    print(phonetic_code)

    # Ask if user wants to convert another word/phrase
    answer = input("Do you want to convert another word or phrase? (yes/no): ").lower()

    if answer != 'yes':
        break  # Exit the loop if user doesn't want to continue

