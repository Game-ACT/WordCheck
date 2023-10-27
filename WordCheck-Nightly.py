# WordCheck
# By Noigamegun
# Version Nightly
# words.txt is required

start_confirm = str(input("Loading the words maybe freeze your PC temporary. Continue? [y,n] : ")).strip().lower()
if start_confirm == "y":
    while True:
        try:
            file_path = str(input("Enter file name (Must be a txt file.  Not Case-sensitive. The program will remove and starting and ending spaces.)"))
            print("\n")
            print("Loading words list...")
            word_list = []

            with open(file_path, "r") as file:
                for line in file:
                    word_list.append(line.strip())

            print("\n")
            print("Loading Done.")
        except:
            print()
            print("File not found. Try again.")
            print()

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
