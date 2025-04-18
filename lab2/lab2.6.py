import re
with open('text.txt',encoding='utf-8') as file:
    content=file.read()
dates=re.findall(r'\b(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})\b',content)
formatted_dates=[f'{year}-{month}-{day}' for day,month,year in dates]
formatted_dates.sort(key=lambda x:(int(x.split('-')[0]),int(x.split('-')[1]),int(x.split('-')[2])))

with open('dates.txt','w',encoding='utf-8') as file:
    for date in formatted_dates:
        file.write(date+'\n')