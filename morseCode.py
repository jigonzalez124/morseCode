#   Name:           Jesus Ivan Gonzalez
#   Date:           July 20th 2015
#   Description:    Simple morse code program.  Note:  / indicates whitespace

def morse(code):
    morseCode = {
    '.-': 'a',    '-...': 'b',    '-.-.': 'c',    '-..': 'd',    '.': 'e',
    '..-.': 'f',    '--.': 'g',    '....': 'h',    '..': 'i',    '.---': 'j',
    '-.-': 'k',    '.-..': 'l',    '--': 'm',    '-.': 'n',    '---': 'o',
    '.--.': 'p',    '--.-': 'q',    '.-.': 'r',    '...': 's',    '-': 't',
    '..-': 'u',    '...-': 'v',    '.--': 'w',    '-..-': 'x',    '-.--': 'y',
    '--..': 'z'
    }
    return morseCode[code];

def main():
    fileName = input("Enter the morse code file name to decode: ")
    fhandle = open(fileName)
    for line in fhandle:       #read each line of the file
        code = line.split()     #split line to letters.  '/' character indicates word space

        final_msg = []
        for letter in code:
            if letter == "/":   #if letter is /, then replace with whitespace
                final_msg.append(" ")
            else:
                final_msg.append(morse(letter)) #call morse method
        print("".join(final_msg))

if __name__ == '__main__':
    main()
