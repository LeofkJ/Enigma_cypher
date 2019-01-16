# REFLECTOR = [("Y","A"),("R","B"),("U","C"),("H","D"),("Q","E"),("S","F"),("L","G"),("P","I"),("X","J"),("N","K"),("O","M"),("Z","T"),("W","V")]

from typing import list, tuple

class Rotor:
    """ This class represents the rotors of the device and they move in close
    connection to the reflectors.
    === Attributes ===
    rotor1: list of tuples for the permutations performed by the first rotor
    rotor2: List of tuples for the permutation performed by the second rotor
    rotor3: List of tuples for the permutations performed by the third rotor
    """
    rotor1: list[tuple]
    rotor2: list[tuple]
    rotor3: list[tuple]

    def __init__(self) -> None:
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
