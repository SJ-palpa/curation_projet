import os
import csv
import requests

write_path = '***path***'  # ASSUMING THAT FOLDER EXISTS!

with open('list_pdf_cc.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile)
    for link in spamreader:
        #Prend la fin de l'url pour le nommage du pdf
        pdf_file = link[0].split('/')[-1]
        with open(os.path.join(write_path, pdf_file), 'wb') as pdf:
            try:
                # Essaye de telechrger l'url avec le PDF
                print('TRYING {}...'.format(link[0]))
                a = requests.get(link[0], stream=True)
                for block in a.iter_content(512):
                    if not block:
                        break

                    pdf.write(block)
                print('OK.')
            except requests.exceptions.RequestException as e:  # This will catch ONLY Requests exceptions
                print('REQUESTS ERROR:')
                print(e)  # This should tell you more details about the error
