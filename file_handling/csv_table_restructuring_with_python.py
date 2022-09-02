# import csv

with open('t.csv', 'r') as f:
    # csv_reader = csv.reader(f)

    with open('out.csv', 'w') as w:
        w.write("Names,Month,Sales\n")
        headers = f.readline()
        months = headers.split(',')[1:]
        content = f.readlines()

        for i in range(len(months)-1):
            for j in range(len(content)):
                jthline = content[j].split(',')
                w.write(f'{jthline[0]},{months[i]},{jthline[i+1]}\n')
