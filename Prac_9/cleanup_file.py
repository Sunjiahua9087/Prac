"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ""
    name = filename.replace(" ", "_").replace(".TXT", ".txt")
    for i, character in enumerate(name):
        if name[i-1] == "_":
            character = name[i].upper()
        if name[i-1].islower() and name[i].isupper():
            if i != 0:
                character = "_" + name[i]
        new_name += character
    return new_name


main()