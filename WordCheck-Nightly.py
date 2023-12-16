# WordCheck
# By Noigamegun
# Version Nightly
# words.txt is required

start_confirm = str(input("Loading the words maybe freeze your PC temporary. Continue? [y,n] : ")).strip().lower()
if start_confirm == "y":
    while True:
        try:
            while True:
                print()
                # Just add the names here
                print("[1] words.txt")
                print("[0] Enter Manually")
                user_input = int(input("Select From List Above : "))
                print()
                # Just add the files here
                if user_input == 1:
                    file_path = "words.txt"
                    break
                elif user_input == 0:
                    file_path = str(input("Enter The Word List Name : "))
                    break
                else:
                    print("Invalid. Try Again.")

            print("\n")
            print("Loading words list...")
            word_list = []

            with open(file_path, "r") as file:
                for line in file:
                    word_list.append(line.strip().lower())

            print("\n")
            print("Loading Done.")
            break
        except:
            print()
            print("File not found. Try again.")
            print()

    while True:
        print("\n")
        word_to_check = input("Enter a word (Enter \"WORDKILL\" to stop): ").strip().lower()
        if word_to_check == "wordkill":
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
