import os

DIRECTORY = r'C:\DIR'  # Укажите папку, в которой необходимо проверить файлы
FIND_STRING = 'Строка для поиска' # Укажите строку для поиска
COUNT_ADDING_SYMBOLS = 10 # Укажите количество символов до и после совпадения, которые будут показаны в выводе


def find(find_directory: str, find_string: str) -> None:
    """
    Рекурсивно проходит по всем файлам в указанной директории и вызывает поиск строки в каждом файле.

    :param find_directory: Путь к каталогу, в котором производится поиск.
    :param find_string: Строка, которую нужно найти в файлах.
    """
    for root, dirs, files in os.walk(find_directory):
        for name in files:
            full_path = os.path.join(root, name)
            find_string_in_file(full_path, find_string)


def find_string_in_file(file: str, find_string: str) -> None:
    """
    Читает файл и ищет в нём указанную строку.

    :param file: Путь к файлу.
    :param find_string: Строка для поиска.
    """
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    index = content.find(find_string)
    if index != -1:
        print_find_info(file, content, find_string)


def print_find_info(file: str, content: str, find_string: str) -> None:
    """
    Находит контекст вокруг найденной строки и печатает его.

    :param file: Путь к файлу, где найдено совпадение.
    :param content: Содержимое файла.
    :param find_string: Найденная строка.
    """
    index = content.find(find_string)

    start_index = index - COUNT_ADDING_SYMBOLS if index >= COUNT_ADDING_SYMBOLS else 0
    end_index = index + len(find_string) + COUNT_ADDING_SYMBOLS

    content = content[start_index:end_index]

    content = content.replace(find_string, f"\x1b[32;1m{find_string}\x1b[0m")

    print(f"{file}:\n{content}\n")


if __name__ == "__main__":
    find(DIRECTORY, FIND_STRING)
