import re
def analyze_log(log_text):
    result={'ipv4':[],
            'timestamp':[],
            'uppercase':[],
            'email_protected':log_text}
    result['ipv4']=re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', log_text)
    result['timestamp']=re.findall(r'\b\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\b', log_text)
    result['uppercase']=re.findall(r'\b[A-ZА-ЯЁ]+\b', log_text)
    result['email_protected']=re.sub(r'\b[A-Za-z0-9]+[A-Za-z0-9._-]*[A-Za-z0-9]+@[A-Za-z0-9]+[A-Za-z0-9._-]*[A-Za-z0-9]+\.[A-Za-z]{2,}\b', '[EMAIL PROTECTED]', log_text)
    return result

example="""2023-10-15 12:30:45 INFO User john.doe@example.com logged in from 192.168.1.100
2023-10-15 12:31:22 ERROR Connection failed from 8.8.8.8
2023-10-15 12:32:10 WARNING Multiple FAILED attempts from admin@server.com
2023-10-15 12:33:05 DEBUG Processing request from 10.0.0.1
2023-10-15 12:34:18 CRITICAL SYSTEM shutdown initiated by ROOT@DOMAIN.LOCAL
2023-10-15 12:35:00 INFO Backup completed successfully
Contact support at help@company.com for assistance
SERVER RESTARTED at 2023-10-15 12:36:00"""

x=analyze_log(example)
print('ipv4:')
for ip in x['ipv4']:
    print(f'{ip}')
print('Время:')
for time in x['timestamp']:
    print(f'{time}')
print('КАПС:')
for word in x['uppercase']:
    print(f'{word}')
print(f'Текст со скрытыми почтами:{x['email_protected']}')
