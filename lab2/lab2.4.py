import re
with open('text.txt', encoding='utf-8') as file:
    text=file.read()
#в регулярном выражении учитываю, что имя пользователя и доменный адрес могут начинаться и заканчиваться только буквой
emails=re.findall(r'\b[A-Za-z0-9]+[A-Za-z0-9._-]*[A-Za-z0-9]+@[A-Za-z0-9]+[A-Za-z0-9._-]*[A-Za-z0-9]+\.[A-Za-z]{2,}\b',text)
with open('emails.txt', 'w') as file:
    for email in emails:
        file.write(f'{email}\n')
phones=re.findall(r'\+7-\d{3}-\d{3}-\d{2}-\d{2}',text)
with open('phones.txt', 'w') as file:
    for phone in phones:
        file.write(f'{phone}\n')
capital_words=re.findall(r'\b[A-ZА-ЯЁ][a-zа-яё]*\b',text)
with open('capital_words', 'w', encoding='utf-8') as file:
    for capital_word in capital_words:
        file.write(f'{capital_word}\n')