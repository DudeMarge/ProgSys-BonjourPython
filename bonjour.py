#!/usr/bin/env python3
# Premier script Python

import time


def main():
    print("Bonjour Python!")
    print("\nJe suis Marjorie Dudemaine")
    print("et je sais compter jusqu'à 10: ", end="", flush=True)
    for i in range(1, 11):
        time.sleep(0.25)
        print(i, " ", end="", flush=True)
    print()


if __name__ == "__main__":
    main()