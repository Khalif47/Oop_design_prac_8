from textEditor import TextEditor

text_editor = TextEditor()


def menu():

    while True:
        try:

            print('---------menu--------\n\n\n')
            print('1. insert num\n')
            print('2. read filename\n')
            print('3. write filename\n')
            print('4. print num1 num2\n')
            print('5. delete num\n')
            print('6. search word\n')
            print('7. quit\n\n')
            print('')

            command = int(input("What option would you like? \n\n"))
            try:
                assert 0 <= command <= 7, "Enter a valid number"
            except AssertionError:
                print("Enter a valid number")
            if command == 1:
                try:
                    line_num = int(input("Line number\n"))
                    item = input("Word")
                    print(text_editor.insert_num(line_num, item))
                except ValueError:
                    print("Enter a correct line number")

            elif command == 2:
                try:
                    filename = input("What is the file name you want to read? \n")
                    print(text_editor.read_filename(filename))
                except FileNotFoundError:
                    print("Enter a valid file")

            elif command == 3:
                filename = input("What is the file name you want to read? \n")
                text_editor.write_filename(filename)
                print("saved file")

            elif command == 4:
                try:
                    position1 = int(input("What is the first position? \n"))
                    position2 = int(input("What is the second position? \n"))
                    print(text_editor.print_num1_num2(position1, position2))
                except ValueError:
                    print("Enter a correct line number")

            elif command == 5:
                try:
                    line_num = int(input("What is the line number you want to delete?\n"))
                    print(text_editor.delete_num(line_num))
                except ValueError:
                    print("Enter a valid line number")

            elif command == 6:
                word = input("Enter a word? \n")
                print(text_editor.search_word(word))

            elif command == 7:
                break
        except ValueError:
            print('Enter a valid number')


menu()
