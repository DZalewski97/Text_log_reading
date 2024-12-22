import re
from collections import Counter
from datetime import datetime

user_action = Counter()
ip_list = set()
data_search = []


data_from = datetime.strptime(input('Od jakiej daty szukać. Format: rrrr-mm-dd'),'%Y-%m-%d')
data_to = datetime.strptime(input('Do jakiej daty szukać. Format: rrrr-mm-dd: '),'%Y-%m-%d')


with open('server_logs.txt', 'r') as file:
    for line in file:
        #print(line)
        if 'User:' in line:
            user_info = line.split('User: ')[1].split(',')[0]
            user = user_info.strip()
            user_action[user] += 1
        if 'IP: 'in line:
            ip_info = line.split('IP: ')[1].split(' ')[0]
            ip_list.add(ip_info)
        match = re.search(r'\d{4}-\d{2}-\d{2}', line)
        if match:
            log_date = datetime.strptime(match.group(0), '%Y-%m-%d')
            if data_from <= log_date <= data_to:
                data_search.append(line)



print(data_search)
top_users = user_action.most_common(3)

with open('log_analysis.txt', 'w') as file:
    for name,times in top_users:
        file.write(f'User: {name}, show times: {times} \n')

with open('IP_adres', 'w') as file:
    for ip in ip_list:
        file.write(f'IP: {ip}')

with open('Date', 'w') as file:
    for date in data_search:
        file.write(date)





