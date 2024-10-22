import os
def print_docks(directoty):
    all_files = os.walk(directoty)
    for catalog in all_files:
        print(f'Папка{catalog[0]} содержит:')
        print(f'Файлы: {",".join([file for file in catalog])}')
        print('-' * 40)
print_docks('C:Пользователи/Анна/Desktop/Software/1')