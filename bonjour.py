#!/usr/bin/env python3
# Premier script Python

import time


def main():
    print("Bonjour Python!")
    print("\nJe suis Marjorie Dudemaine")
    compter_jusqua(10)


def compter_jusqua(limite_sup):
    print(f"et je sais compter jusqu'à {limite_sup}: ", end="", flush=True)
    for i in range(1, limite_sup + 1):
        time.sleep(0.25)
        print(i, " ", end="", flush=True)
    print()


if __name__ == "__main__":
    main()
