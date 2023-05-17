#!/usr/bin/python3

# A program that prints all the names defined by the compiled module
# hidden_4.pyc (please download it locally)

if __name__ == "__main__":
    import hidden_4

    def_names = dir(hidden_4)
    for name in def_names:
        if name[:2] != "__":
            print(name)
