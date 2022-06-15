from pathlib import Path

import character

char_list = []
filename = Path.cwd() / "data.txt"


def load_list():
    try:

        in_file = open(filename, "r")
    except FileNotFoundError:
        print("File noe found " + str(filename))
        raise
    except IOError:
        print("Could not open the file " + str(filename))
        raise
    else:
        for line in in_file.readlines():
            element = line.split(',')
            if "Ranger" in element[0]:
                char_list.append(character.Ranger(element[1].replace('"', ''), element[2].replace('"', ''),
                                                  element[3].replace('"', '').replace("\r", "").replace("\n", "")))
            elif "Wizard" in element[0]:
                char_list.append(character.Wizard(element[1].replace('"', ''), element[2].replace('"', ''),
                                                  element[3].replace('"', '').replace("\r", "").replace("\n", "")))
            elif "Bard" in element[0]:
                char_list.append(character.Bard(element[1].replace('"', ''), element[2].replace('"', ''),
                                                element[3].replace('"', '').replace("\r", "").replace("\n", "")))
            elif "Paladin" in element[0]:
                char_list.append(character.Paladin(element[1].replace('"', ''), element[2].replace('"', ''),
                                                   element[3].replace('"', '').replace("\r", "").replace("\n", "")))
            elif "Barbarian" in element[0]:
                char_list.append(character.Barbarian(element[1].replace('"', ''), element[2].replace('"', ''),
                                                     element[3].replace('"', '').replace("\r", "").replace("\n", "")))
            else:
                char_list.append(character.Character(element[1].replace('"', ''), element[2].replace('"', '')))
        in_file.close()


def print_list():
    for chr in char_list:
        if isinstance(chr, character.Ranger):
            print("Ranger " + chr.name + " of family " + chr.family)
        elif isinstance(chr, character.Wizard):
            print("Wizard " + chr.name + " of family " + chr.family)
        elif isinstance(chr, character.Bard):
            print("Bard " + chr.name + " of family " + chr.family)
        elif isinstance(chr, character.Paladin):
            print("Paladin " + chr.name + " of family " + chr.family)
        elif isinstance(chr, character.Barbarian):
            print("Barbarian " + chr.name + " of family " + chr.family)
        else:
            print(chr.name)


if __name__ == '__main__':
    load_list()
    print_list()
