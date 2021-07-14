import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

df = pandas.read_csv("nato_phonetic_alphabet.csv")

# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
names = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    s = input().upper()
    try:
        final = [names[letter] for letter in s]
    except KeyError:
        print("Only alphabets please.")
        generate_phonetic()
    else:
        print(final)


generate_phonetic()
