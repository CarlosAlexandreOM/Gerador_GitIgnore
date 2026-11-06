
from group import GROUPS, DICT_NAMES


def create_file(text) -> None:
    """
    Cria o arquivo .gitignore com o conteúdo fornecido.

    Parameters
    ----------
    text : str
        Conteúdo que será escrito no arquivo .gitignore.
    """

    with open(".gitignore", "w", encoding="utf_8") as file:
        file.write(text)


def get_option() -> int:
    """
    Solicita e valida a opção selecionada pelo usuário.

    Returns
    -------
    int
        Número correspondente à opção selecionada pelo usuário.
    """

    while True:
        try:
            option = int(input("\nDigite a opção que deseja incluir: "))

            if option in DICT_NAMES:
                return option

            print("Erro: Opção não disponível.")

        except ValueError:
            print("Erro: Digite um valor válido!")


def create_text(selected: list[str]) -> str:
    """
    Monta o conteúdo do arquivo .gitignore com base nos grupos selecionados.

    Parameters
    ----------
    selected : list[str]
        Lista contendo os nomes dos grupos selecionados pelo usuário.

    Returns
    -------
    str
        Texto formatado com as regras dos grupos selecionados.
    """

    linhas = []

    for item in selected:
        if item in GROUPS:
            linhas.append(f"# {item}")
            linhas.append("")
            linhas.extend(GROUPS[item])
            linhas.append("")

    text = "\n".join(linhas)

    return text


def painel():
    """
    Exibe o menu de opções do programa no terminal.
    """

    print("\n" + "=" * 50)
    print("GERADOR DE GIT IGNORE".center(50, " "))
    print("=" * 50 + "\n")

    for key, value in DICT_NAMES.items():
        print(f"{key} - {value}")
