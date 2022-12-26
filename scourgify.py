import sys
import csv

if len(sys.argv) == 3:
    students = []
    with open (sys.argv[1]) as file:
        rows = csv.DictReader(file)
        for row in rows:
            last, first = row['name'].split(', ')
            students.append({'first':first, 'last':last, 'house':row['house']})

    with open (sys.argv[2], 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
        writer.writeheader()
        for student in students:
            writer.writerow(student)


elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

else:
    sys.exit('Too few command-line arguments')