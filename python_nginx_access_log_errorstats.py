import datetime
import re
def get_user_date_input():
    user_input = input("Введите дату в формате 'DD/MMM/YYYY' (например, 10/Apr/2024) или нажмите Enter для использования сегодняшней даты: ")
    if user_input:
        try:
            datetime.datetime.strptime(user_input, '%d/%b/%Y')
            return user_input
        except ValueError:
            print("Дата введена некорректно. Будет использована сегодняшняя дата.")
            return datetime.datetime.now().strftime('%d/%b/%Y')
    else:
        return datetime.datetime.now().strftime('%d/%b/%Y')
log_file_path = "/var/log/nginx/access.log"
today = get_user_date_input()
with open(log_file_path, 'r') as file:
    log_contents = file.readlines()
total_requests = sum(1 for line in log_contents if today in line)
error_requests = sum(1 for line in log_contents if today in line and re.search(r' 50[0-9] ', line))
percentage = (error_requests / total_requests * 100) if total_requests > 0 else 0
