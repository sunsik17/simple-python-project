import csv

result = []
with open('product_list.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for line in reader:
        result.append(line)
        print(line)

with open('product_list.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)
    writer.writerow(['3', '양말', '5000'])