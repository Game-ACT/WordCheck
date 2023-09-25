# WordCheck
# By Noigamegun
# Version Nightly
# words.txt is required

start_confirm = str(input("Loading the words maybe freeze your PC temporary. Continue? [y,n] : ")).strip().lower()
if start_confirm == "y":
    print("\n")
    print("Loading words list...")
    file_path = "words.txt"
    word_list = []

    with open(file_path, "r") as file:
        for line in file:
            word_list.append(line.strip())

    print("\n")
    print("Loading Done.")

    while True:
        print("\n")
        word_to_check = input("Enter a word (Enter \"stop the program\" to stop): ").strip().lower()
        if word_to_check == "stop the program":
            print("\n")
            print("Stopped")
            break
        else:
            print("\n")
            if word_to_check in word_list:
                print(f"The word \"{word_to_check}\" is a word.")
            else:
                print(f"The word \"{word_to_check}\" is not a word.")

else:
    print("Aborted")
