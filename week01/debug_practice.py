# Snippet 1: NameError
def snippet_1():
    total = 10
    print(total)


# Snippet 2: TypeError
def snippet_2():
    print("Total:", 5)


# Snippet 3: IndexError
def snippet_3():
    items = [1, 2, 3]
    print(items[2])


# Snippet 4: KeyError
def snippet_4():
    config = {"host": "localhost"}
    print(config["host"])


# Snippet 5: ValueError
def snippet_5():
    number = int("42")
    print(number)


# Snippet 6: ModuleNotFoundError
def snippet_6():
    import matplotlib

    print("Matplotlib imported successfully!")
    print("Matplotlib version:", matplotlib.__version__)


# Snippet 7: Mutable Default Argument
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items


# Run all snippets
snippet_1()
snippet_2()
snippet_3()
snippet_4()
snippet_5()
snippet_6()

print(add_item("a"))
print(add_item("b"))
