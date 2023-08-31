lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A',
        'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v',
        'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
        'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l',
        'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
        'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a',
        '1': '0', '2': '9', '3': '8', '4': '7', '5': '6', '6': '5', '7': '4',
        '8': '3', '9': '2', '0': '1', '.': '.', ',': ',', '!': '!', '?': '?',
        '"': '"'}

def atbashPrompt():
    codeChoice = input(str(" \nВведите \"а\" для шифрования файла.\nВведите \"б\" для рисшифровки текста.\n"))
    if codeChoice == "а":
        with open("kniga.txt") as f:
            text = f.read()

        new_text = atbash(text)

        with open("Шифр.txt", 'w') as f:
            f.write(new_text)
    elif codeChoice == "б":
        with open("Шифр.txt") as f:
            text = f.read()

        new_text = atbash(text)

        with open("Расшифр.txt", 'w') as f:
            f.write(new_text)

def atbash(message):
  cipher = ''
  for letter in message:
    if (letter in lookup_table):
      cipher += lookup_table[letter]
    else:
      cipher += ' '

  return cipher

atbashPrompt()