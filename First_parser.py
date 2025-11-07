import requests
import html2text

# Делаем GET-запрос
j = requests.get('https://owasp.org/contact/')

print(j.status_code)                            # Код ответа сервера
k = html2text.HTML2Text()                       # Создаем экземпляр парсера
k.ignore_links = True                           # Параметр, влияющий на то, как парсятся ссылки
l = k.handle(j.text)                            # Текст без HTML тегов
g = open('owasp.txt', 'w', encoding='utf-8')    # Откртие файла для записи
g.write(l)                                      # Запись в файл
g.close()                                       # Закрытие файла
