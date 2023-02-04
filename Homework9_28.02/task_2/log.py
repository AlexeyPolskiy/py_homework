from datetime import datetime


def log_temp(num_1, action, num_2, result):
    time = datetime.now().strftime('%d:%b:%Y:%H:%M:%S')
    print(f"Лог выполнен")
    with open('log.csv', 'a') as file:
        file.write(f'{time}; {num_1}; {action}; {num_2}; {str(result)}\n')
