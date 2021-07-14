with open("./Input/Letters/starting_letter.txt") as letter:
    with open("Input/Names/invited_names.txt") as names:
        l = letter.read()
        n = names.readlines()
        for name in n:
            l1 = l.replace("[name]", name.strip())
            with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", "w") as final:
                final.write(l1)
