import re

my_string = "Place of delivery of goods: 82172, Ukraine, Lviv Region, Stryi, str. Doroshenko, 1. Deadline for delivery of goods: 31.12.2024"


if __name__ == '__main__':
    data = {
        'country': re.search(r',\s+([A-Za-z]+),\s+([A-Z\s+a-z]+),\s+([A-Za-z]+),', my_string).group(1),
        'region': re.search(r',\s+([A-Za-z]+),\s+([A-Z\s+a-z]+),\s+([A-Za-z]+),', my_string).group(2),
        'city': re.search(r',\s+([A-Za-z]+),\s+([A-Z\s+a-z]+),\s+([A-Za-z]+),', my_string).group(3),
        'postal': re.search(r'\d+', my_string).group(),
        'address': re.search(r'str\.\s*[A-Za-z]+,\s*\d+', my_string).group(),
        'deadline': re.search(r'\d{2}\.\d{2}\.\d{4}', my_string).group(),
    }
    print(data)
