from RBTree_imp import *


def load_from_file(path):
    file = open(path, "r")
    tree = RBTree()
    for word in file.readlines():
        tree.insert(word.strip())
    file.close()
    print("size = " + str(tree.get_size()) + " height = " + str(tree.get_height(tree.root)))
    return tree


def word_lookup(dictionary):
    word = input("Please enter a word to lookup in the dictionary: ")
    print(dictionary.search(word))


def user_insert(dictionary):
    word = input("Please enter a word to insert in the dictionary: ")
    status = dictionary.insert(word)
    if status == -1:
        print(word + " Already exists in the dictionary")
    else:
        print(word + " inserted successfully")
        print("size = " + str(dictionary.get_size()) + " height = " + str(dictionary.get_height(dictionary.root)))


file_path = "C:\\Users\\zedan.net\\Downloads\\EN-US-Dictionary.txt"
dictionary = load_from_file(file_path)
print("Welcome to the  us english dictionary system please choose an option:")
print("options:\n1-Lookup a word\n2-Insert a word\n3-Print current size\n4-END")
choice = input()
while choice != "4":
    if choice == "1":
        word_lookup(dictionary)
    elif choice == "2":
        user_insert(dictionary)
    elif choice == "3" :
        print("Size is :" + str(dictionary.get_size()))

    print("What else would you like to do ? : ")
    print("options:\n1-Lookup a word\n2-Insert a word\n3-Print current size\n4-END")
    choice = input()
