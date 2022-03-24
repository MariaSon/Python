documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

comands = ['p', 's', 'l', 'a', 'd', 'm', 'as']

comand = input('Введите код пользовательской команды "p" (people),\n"s" (shelf), "l" (list), "a" (add), '
               '"d" (delete),\n"m" (move), "as" (add shelf): ')

while comand not in comands:
    print('Введите команду еще раз!')
    comand = input('Введите код пользовательской команды "p" (people),\n"s" (shelf), "l" (list), "a" (add), '
                   '"d" (delete),\n"m" (move), "as" (add shelf): ')


def find_person(document):
    for dicts in documents:
        for k, v in dicts.items():
            if document == dicts["number"]:
                return dicts["name"]
    return 'Документ в базе не найден!'


def find_shelf(document):
    for shelf, doc_num in directories.items():
        if document in doc_num:
            return f'Номер полки для документа: {document} - "{shelf}"'
    return 'Документ в базе не найден!'


def show_documents():
    for dicts in documents:
        document_list = list(dicts.values())
        print(f'{document_list[0]} "{document_list[1]}" "{document_list[2]}"')  # либо (*document_list, sep = ' ')


def add_document():
    documents.append({'type': new_type, 'number': new_number, 'name': new_name})
    b = directories[new_shelf]
    c = b.append(new_number)


def delete_document(document):
    for dicts in documents:
        if document == dicts["number"]:
            dicts.clear()

    for shelf_num, document_num in directories.items():
        if document in document_num:
            b = directories[shelf_num]
            c = []
            for element in b:
                if element == document:
                    pass
                else:
                    c.append(element)
            directories[shelf_num] = c


def move_document(document_m):
    for shelf_num, document_num in directories.items():
        if document_m in document_num:
            b = directories[shelf_num]
            c = []
            for element in b:
                if element == document_m:
                    pass
                else:
                    c.append(element)

            directories[shelf_num] = c

    d = directories[shelf_m]
    e = d.append(document_m)


def add_shelf(new_shelf):
    directories[new_shelf] = []


if comand == 'p':
    document = input('Введите номер документа: ')
    result = find_person(document)
    print(result)

elif comand == 's':
    document = input('Введите номер документа: ')
    result = find_shelf(document)
    print(result)

elif comand == 'l':
    show_documents()

elif comand == 'a':
    new_type = input('Введите тип документа: ')
    new_number = input('Введите номер документа: ')
    new_name = input('Введите имя владельца документа: ')
    new_shelf = input('Введите полку для хранения документа: ')

    while new_shelf not in directories.keys():
        print(f'Полки "{new_shelf}" не существует!')
        new_shelf = input('Введите полку для хранения документа: ')

    add_document()
    print(documents)
    print(directories)

elif comand == 'd':
    document = input('Введите номер документа: ')
    c = []
    for dicts in documents:
        c.append(dicts["number"])

    while document not in c:
        print(f'Документ "{document}" не существует!')
        document = input('Введите номер документа повторно: ')

    delete_document(document)

    print(documents)
    print(directories)


elif comand == 'm':
    document_m = input(str('Введите номер документа: '))
    c = []
    for dicts in documents:
        c.append(dicts["number"])

    while document_m not in c:
        print(f'Документ "{document_m}" не существует!')
        document_m = input('Введите номер документа повторнmо: ')

    shelf_m = input('Введите полку для хранения документа: ')

    while shelf_m not in directories.keys():
        print(f'Полки "{shelf_m}" не существует!')
        shelf_m = input('Введите полку для хранения документа: ')

    move_document(document_m)

    print(directories)

else:
    new_shelf = input('Введите номер новой полки: ')

    while new_shelf in directories.keys():
        print(f'Полка "{new_shelf}" существует!')
        new_shelf = input('Введите номер новой полки: ')

    add_shelf(new_shelf)

    print(directories)