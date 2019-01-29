# REFLECTOR = [("Y","A"),("R","B"),("U","C"),("H","D"),("Q","E"),("S","F"),("L","G"),("P","I"),("X","J"),("N","K"),("O","M"),("Z","T"),("W","V")]

from typing import list, tuple


class Rotor:
    """ This class represents the rotors of the device and they move in close
    connection to the reflectors.
    === Attributes ===
    rotor1: list of tuples for the permutations performed by the first rotor
    rotor2: List of tuples for the permutation performed by the second rotor
    rotor3: List of tuples for the permutations performed by the third rotor
    rotor_id: The id for the rotor to be used
    position1: The position of the Rotor 1
    position2: The position of the Rotor 2
    position3: The position of the Rotor 3
    """
    rotor1: list[tuple]
    rotor2: list[tuple]
    rotor3: list[tuple]
    position1: int
    position2: int
    position3: int

    def __init__(self, rotor_id: int, position: int) -> None:
        """ Initializes the Rotor class.
        """
        self.rotor1 = [('A','E'),('B','K'),('C','M'),('D','F'),('E','L'),
                       ('F','G'),('G','D'),('H','Q'),('I','V'),('J','Z'),
                       ('K','N'),('L','T'),('M','O'),('N','W'),('O','Y'),
                       ('P','H'),('Q','X'),('R','U'),('S','S'),('T','P'),
                       ('U','A'),('V','I'),('W','B'),('X','R'),('Y','C'),
                       ('Z','J')]
        self.rotor2 = [('A','A'),('B','J'),('C','D'),('D','K'),('E','S'),
                       ('F','I'),('G','R'),('H','U'),('I','X'),('J','B'),
                       ('K','L'),('L','H'),('M','W'),('N','T'),('O','M'),
                       ('P','C'),('Q','Q'),('R','G'),('S','Z'),('T','N'),
                       ('U','P'),('V','Y'),('W','F'),('X','V'),('Y','O'),
                       ('Z','E')]
        self.rotor3 = [("A","B"),("B","D"),("C","F"),("D","H"),("E","J"),
                       ("F","L"),("G","C"),("H","P"),("I","R"),("J","T"),
                       ("K","X"),("L","V"),("M","Z"),("N","N"),("O","Y"),
                       ("P","E"),("Q","I"),("R","W"),("S","G"),("T","A"),
                       ("U","K"),("V","M"),("W","U"),("X","S"),("Y","Q"),
                       ("Z","O")]
        self.position1 = 7
        self.position2 = 3
        self.position3 = 23
        # self.rotor_id = rotor_id
        # self.position = position

# the rotors should advance before the letter goes through

    def advance(self) -> None:
        """ Advances the position of the rotors.
        """
        self.position3 += 1
        if self.position3 > 25:
            self.position3 = 0
            self.position2 += 1
        if self.position2 > 25:
            self.position2 = 0
            self.position1 += 1
        if self.position1 > 25:
            self.position1 = 0

    def return_second_letter(self, letter: str, rotor_id: int) -> str:
        """ Returns the second letter from the tuple in the list of tuples.
        """
        if rotor_id == 3:
            for i in range(len(self.rotor3)):
                if self.rotor3[i][0] == letter:
                    return self.rotor3[i][1]
        if rotor_id == 2:
            for i in range(len(self.rotor2)):
                if self.rotor2[i][0] == letter:
                    return self.rotor2[i][1]
        if rotor_id == 1:
            for i in range(len(self.rotor1)):
                if self.rotor1[i][0] == letter:
                    return self.rotor1[i][1]


    def generate_letter(self, letter: str) -> str:
        """ Generates the encrypted letter and returns it.
        """
        self.advance()
        position = ord(letter) - 65
        new_letter_3 = self.return_second_letter(
            (chr(position + self.position3)), 3)
        new_letter_2 = self.return_second_letter()

    def rotation(self):
        pass

    def passing_the_data_of_the_character(self):
        pass


class Reflector:
    """ This class represents the reflector of the device.
    ===ATTRIBUTES===
    REFLECTOR: List of Tuples that represents the reflector, placed at the end of the rotors

    """
    def __init__(self) -> None:
        """Initializes the Reflector class.
        """
        self.reflector = [("Y","A"),("R","B"),("U","C"),("H","D"),("Q","E"),
                          ("S","F"),("L","G"),("P","I"),("X","J"),("N","K"),
                          ("O","M"),("Z","T"),("W","V")]

    def generate_reflected(self, s: str) -> str:
        """ Generates the reflected message.
        """
        pass


class EnigmaRegulator:
    """ This class regulates the whole enigma cypher project.
     === Attributes ===
     sentence: the inputted sentence for the enigma machine.
    """
    sentence: str

    def __init__(self, s: str) -> None:
        """ Initializes the class EnigmaRegulator.
        """
        self.sentence = s

    def generate_encrypted(self, sent: str) -> str:
        """ Generates and returns the message in an encrypted way.
        """
        output_sentence = ""
        for i in range(len(sent)):
            if sent[i] == ' ':
                output += ' '
            # turn all the letters to capitals

    def generate_decrypted(self) -> str:
        """ Generates and returns the message in a non encrypted way.
        """
        pass


if name == '__main__':
    choice = input(" What do you want to do? \n1. Encrypt the message?\n 2.Do "
                   "you want to decrypt the message?")
    if choice == 1:
        pass
    elif choice == 2:
        pass
    else:
        print(" Choice not possible!")

