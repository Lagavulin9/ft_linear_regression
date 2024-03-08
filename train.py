import csv

theta0 = 0
theta1 = 0
learning_rate = 1

try:
    with open('data.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            mileage = int(row['km'])
            price = int(row['price'])
except Exception as e:
    print(e)
    exit(1)

with open('model.csv', 'w') as csvfile:
    fieldnames = ['theta0', 'theta1']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'theta0': theta0, 'theta1': theta1})
