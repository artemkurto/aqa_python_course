class Reader:

    def __init__(self, file_path):
        self.__file_path = file_path
        self.data = None

    def read_file(self):
        with open(self.__file_path, 'r') as f:  # 'r' -  мод читання
            self.data = f.read()


class Writer:  # write realisation
    def __init__(self, file_path):
        self.__file_path = file_path
        self.data = None

    def write_file(self, row):
        with open(self.__file_path, 'a') as f:
            self.data = f.write('\n' + row)


class ProxyReaderWriter:

    def __init__(self, file_path):
        self.file_path = file_path
        self.reader = Reader(file_path)
        self.writer = Writer(file_path)
        self.data = None
        self.previous_row = None

    def read(self):
        """
        1) Не читати файл, а просто повертати значення ЯКЩО файл не було змінено
        :return: None
        """

        if self.data:
            print('Don not read the file \n', self.data)
            return
        self.reader.read_file()
        self.data = self.reader.data
        print('Read the file\n', self.data)

    def write(self, row):  # write realisation
        """
        2) Він повинен записувати інформацію в кінець файлу(не переписуе, а доповлюе, дивись mode = 'a')
        3) Якщо інформація на запис надсилаеться повторно, то не записувати другий раз поспіль одне і те саме
        Важливо. Для перевірки чи МИНУЛИЙ раз ми записували цю ж строку що і зараз в файл читати не треба
        :return: None
        """

        if row == self.previous_row:
            print("Did not write")
            return
        self.writer.write_file(row)
        self.previous_row = row
        self.data = None
        print(f'Wrote: {row}')


proxy_rw = ProxyReaderWriter(file_path='tst_file.txt')

# proxy_rw.read()
# proxy_rw.read()
# proxy_rw.read()
#
# proxy_rw.write('asd')  # буде запис
# proxy_rw.write('asd')  # не буде запису
# proxy_rw.write('asd2')  # буде запис
# proxy_rw.write('asd')  # буде запис
# proxy_rw.write('asd') # не буде запису

proxy_rw.read()  # файл читаеться, текст повертаеться
print('----------------')
proxy_rw.read()  # файл НЕ читаеться, текст повертаеться
print('----------------')
proxy_rw.write('aa')  # запис в файл відбуваеться
print('----------------')
proxy_rw.read()  # файл читаеться, текст повертаеться
print('----------------')
proxy_rw.write('aa')  # запис в файл НЕ відбуваеться
print('----------------')
proxy_rw.read()  # файл НЕ читаеться, текст повертаеться
print('----------------')
proxy_rw.write('ab')  # запис в файл відбуваеться
print('----------------')
proxy_rw.read()  # файл читаеться, текст повертаеться
print('----------------')
proxy_rw.write('aa')  # запис в файл відбуваеться
print('----------------')
proxy_rw.read()  # файл читаеться, текст повертаеться
print('----------------')
proxy_rw.read()  # файл не читаеться, текст повертаеться
print('----------------')
proxy_rw.read()  # файл не читаеться, текст повертаеться
print('----------------')
