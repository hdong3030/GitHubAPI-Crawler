import csv

with open('classifier.csv', newline='') as csvfile:
    with open('production_nb.csv', mode='a') as prodcsv:
        with open('sharing_nb.csv', mode='a') as sharingcsv:
            with open('personal_nb.csv', mode='a') as personalcsv:
                reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                fieldnames = ['repo']
                prodWriter = csv.DictWriter(prodcsv, fieldnames=fieldnames)
                sharWriter = csv.DictWriter(sharingcsv, fieldnames=fieldnames)
                personalWriter = csv.DictWriter(personalcsv, fieldnames=fieldnames)
                print(reader)

                for row in reader:
                    arr = row[0].split(",")

                    #production notebook:
                    if arr[1] == "True":
                       prodWriter.writerow({
                           'repo': arr[0],
                       })

                    #sharing
                    if arr[2] == "True":
                        sharWriter.writerow({
                           'repo': arr[0],
                        })

                    #other/personal
                    if arr[3] == "True":
                        personalWriter.writerow({
                           'repo': arr[0],
                        })