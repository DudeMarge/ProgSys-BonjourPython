#!/usr/bin/env python3
# Premier script Python

import time


def main():
    print("Bonjour Python!")
    print("\nJe suis Marjorie Dudemaine")
    n = 10
    print(f"et je sais compter jusqu'à {n}: ", end="", flush=True)
    for i in range(1, n+1):
        time.sleep(0.25)
        print(i, " ", end="", flush=True)
    print()


if __name__ == "__main__":
    main()
