import os

def save_file_sizes(directory):
    files_sizes = {}

    # Просканировать папку и получить список файлов
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Получить полный путь к файлу
            file_path = os.path.join(root, file)
            # Получить размер файла в байтах
            file_size = os.path.getsize(file_path)
            # Сохранить полный путь и размер файла в словаре
            files_sizes[file_path] = file_size

    # Записать полные пути и размеры файлов в файл
    with open('files_size.txt', 'w') as f:
        for file_path, file_size in files_sizes.items():
            f.write(f"{file_path}: {file_size} bytes\n")

    # Найти название и размер самого большого файла
    largest_file_path = max(files_sizes, key=files_sizes.get)
    largest_file_name = os.path.basename(largest_file_path)
    largest_file_size = files_sizes[largest_file_path]

    return largest_file_name, largest_file_size

if __name__ == "__main__":
    directory = os.getcwd()  # Текущая директория
    largest_file_name, largest_file_size = save_file_sizes(directory)

    print("Название самого большого файла:", largest_file_name)
    print("Размер самого большого файла:", largest_file_size, "байт")
