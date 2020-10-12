#!/usr/bin/env python3
"""
Premier script Python

par:Marjorie Dudemaine
"""

import time


def main():
    """
    Fonction principale du script
    """
    print("Bonjour Python!")
    print("\nJe suis Marjorie Dudemaine")
    compter_jusqua(10)


def compter_jusqua(limite_sup):
    """
    Affiche progressivement une séquence de nombre à partir de 1 en montant

    :param limite_sup: jusqu'à ou compteur
    """
    print(f"et je sais compter jusqu'à {limite_sup}: ", end="", flush=True)
    for i in range(1, limite_sup + 1):
        time.sleep(0.25)
        print(i, " ", end="", flush=True)
    print()


if __name__ == "__main__":
    main()
