import os

DIRECTORY = r"C:\DIR"  # Укажите папку, в которой необходимо переименовать файлы


def rename_files(find_directory: str) -> None:
    """
    Рекурсивно проходит по всем файлам в указанной директории и переименовывает их согласно правилам.

    :param find_directory: Путь к каталогу, в котором производится переименование.
    """
    for root, dirs, files in os.walk(find_directory):
        for name in files:
            rename_file(root, name)


def rename_file(root: str, name: str) -> None:
    """
    Переименовывает один файл в указанной директории.

    :param root: Путь к директории, содержащей файл.
    :param name: Текущее имя файла (включая расширение).
    """
    valid_name = get_valid_name(name)
    old_file = os.path.join(root, name)
    new_file = os.path.join(root, valid_name)
    os.rename(old_file, new_file)


def get_valid_name(name: str) -> str:
    """
    Преобразует имя файла по заданным правилам замены.

    :param name: Исходное имя файла.
    :return: Новое валидное имя файла.
    """
    # Замены по шаблонам
    name = name.replace(" ", "шаблон")
    # name = name.replace("замена", "шаблон")

    return name


if __name__ == "__main__":
    rename_files(DIRECTORY)