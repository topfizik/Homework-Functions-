
### Задание 2 ###

# перечень всех документов
documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
# перечень полок, на которых хранятся документы (если документ есть в documents, то он обязательно должен быть и в directories)
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def find_owner(document_number):
    for document in documents:
        if document['number'] == document_number:
            return document['name']
    return None

def find_shelf(document_number):
    for shelf, numbers in directories.items():
        if document_number in numbers:
            return shelf
    return None

def list_documents():
    result = []
    for document in documents:
        shelf = find_shelf(document['number'])
        result.append(f"№: {document['number']}, тип: {document['type']}, владелец: {document['name']}, полка хранения: {shelf}")
    return result

def add_shelf(shelf_number):
    if shelf_number in directories:
        return False
    directories[shelf_number] = []
    return True

def delete_shelf(shelf_number):
    if shelf_number not in directories:
        return 'not_exists'
    if directories[shelf_number]:
        return 'not_empty'
    del directories[shelf_number]
    return 'deleted'


def add_document(doc_number, doc_type, doc_owner, shelf_number):
    if shelf_number not in directories:
        return 'no_shelf'
    documents.append({'type': doc_type, 'number': doc_number, 'name': doc_owner})
    directories[shelf_number].append(doc_number)
    return 'added'

def delete_document(doc_number):
    global documents
    for document in documents:
        if document['number'] == doc_number:
            documents = [doc for doc in documents if doc['number'] != doc_number]
            for numbers in directories.values():
                if doc_number in numbers:
                    numbers.remove(doc_number)
            return 'deleted'
    return 'not_found'

def move_document(doc_number, new_shelf_number):
    if new_shelf_number not in directories:
        return 'no_shelf'

    old_shelf = find_shelf(doc_number)
    if old_shelf:
        directories[old_shelf].remove(doc_number)
        directories[new_shelf_number].append(doc_number)
        return 'moved'
    return 'not_found'

def print_documents():
    print("Текущий список документов:")
    for doc_info in list_documents():
        print(doc_info)

def main():
    while True:
        command = input("Введите команду: ")

        if command == "p":
            document_number = input("Введите номер документа: ")
            owner = find_owner(document_number)
            if owner:
                print(f"Владелец документа: {owner}")
            else:
                print("Документ не найден в базе")

        elif command == "s":
            document_number = input("Введите номер документа: ")
            shelf = find_shelf(document_number)
            if shelf:
                print(f"Документ хранится на полке: {shelf}")
            else:
                print("Документ не найден в базе")

        elif command == "l":
            print_documents()

        elif command == "ads":
            shelf_number = input("Введите номер полки: ")
            if add_shelf(shelf_number):
                print(f"Полка добавлена. Текущий перечень полок: {', '.join(directories.keys())}.")
            else:
                print(f"Такая полка уже существует. Текущий перечень полок: {', '.join(directories.keys())}.")

        elif command == "ds":
            shelf_number = input("Введите номер полки: ")
            result = delete_shelf(shelf_number)
            if result == 'deleted':
                print(f"Полка удалена. Текущий перечень полок: {', '.join(directories.keys())}.")
            elif result == 'not_empty':
                print(f"На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: {', '.join(directories.keys())}.")
            else:
                print(f"Такой полки не существует. Текущий перечень полок: {', '.join(directories.keys())}.")

        elif command == "ad":
            doc_number = input("Введите номер документа: ")
            doc_type = input("Введите тип документа: ")
            doc_owner = input("Введите владельца документа: ")
            shelf_number = input("Введите полку для хранения: ")
            result = add_document(doc_number, doc_type, doc_owner, shelf_number)
            if result == 'no_shelf':
                print(f"Такой полки не существует. Добавьте полку командой ads.")
            else:
                print("Документ добавлен.")
                print_documents()

        elif command == "d":
            doc_number = input("Введите номер документа: ")
            result = delete_document(doc_number)
            if result == 'deleted':
                print("Документ удален.")
            else:
                print("Документ не найден в базе.")
            print_documents()

        elif command == "m":
            doc_number = input("Введите номер документа: ")
            new_shelf_number = input("Введите номер полки: ")
            result = move_document(doc_number, new_shelf_number)
            if result == 'no_shelf':
                print(f"Такой полки не существует. Текущий перечень полок: {', '.join(directories.keys())}.")
            elif result == 'not_found':
                print("Документ не найден в базе.")
            else:
                print("Документ перемещен.")
            print_documents()

        elif command == "q":
            break

        else:
            print("Неправильная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()
