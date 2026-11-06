from generator import get_option, create_file, create_text, painel
from group import DICT_NAMES


def main():

    selected = []

    while True:

        painel()

        option = get_option()

        if option == 11:
            print("Obriado por utilizar o nosso programa")
            break
        
        elif option == 12:
            
            if selected:
                text = create_text(selected)
                create_file(text)
                break

            else:
                print("\nPor favor, selecione alguma opção")

        else:
            selected.append(DICT_NAMES.pop(option))


if __name__ == "__main__":
    main()