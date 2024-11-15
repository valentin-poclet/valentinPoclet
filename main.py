"""
import essentiel
"""
#### Fonction secondaire
import string
from unidecode import unidecode


def ispalindrome(p):
    """
    Fonction permettant de verifier si le mot p est un palindrome
    """
    p = unidecode(p).translate(str.maketrans('','',string.punctuation)).upper().replace(" ","")
    if len(p) == 1:
        return True
    if p == "":
        return True
    if p[0] == p[-1]:
        return ispalindrome(p[1:-1])
    return False

#### Fonction principale


def main():
    """
    fonction main
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
