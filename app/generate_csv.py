import random
import string

def create_large_csv(file_name: str, rows: int, cols: int):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        headers = [''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for _ in range(cols)]
        writer.writerow(headers)
        for _ in range(rows):
            writer.writerow([''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) for _ in range(cols)])

create_large_csv('dummy.csv', 100000, 100)
