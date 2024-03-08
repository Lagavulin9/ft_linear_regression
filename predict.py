import csv

theta0 = 0
theta1 = 0

try:
    with open('model.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            theta0 = float(row['theta0'])
            theta1 = float(row['theta1'])
except:
    print("invalid parameters for theta")
    exit(1)

try:
    mileage = int(input("Enter mileage: "))
    assert(mileage >= 0)
    print(f"Estimated Price: {theta0 + (theta1 * mileage)}")
except:
    print("Mileage must be positive integer")