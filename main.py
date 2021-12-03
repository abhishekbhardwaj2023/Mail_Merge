# Global Variable
PLACEHOLDER = "[name]"

# Open file and read content
with open("D:/VS_Code Programs/Python/Mail_Merge_Project/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Merging names with the invitation letter
with open("D:/VS_Code Programs/Python/Mail_Merge_Project/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"D:/VS_Code Programs/Python/Mail_Merge_Project/Output/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

