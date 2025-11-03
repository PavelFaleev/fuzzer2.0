import requests


def main():
    file_name = input('Файл с ссылками(адрес относительный):\t')
    url = input('URL для поиска:\t')
    extension = input('Адреса оканчиваются на("/" или ""):\t')

    links = []
    with open(file_name, 'rt') as f:
        links = f.readlines()
    f.close()

    if len(links) == 0:
        print('Нет ссылок для проверки')
        return

    for link in links:
        link = link.replace('\n', '')
        full_link = ''.join((url, link, extension))
        response = requests.get(full_link)
        
        if response.status_code != 404:
            print(f'{full_link} - существует')
            with open('file.txt', 'a') as result:
                result.write(full_link + '\n')
    result.close()

if __name__ == "__main__":
    main()