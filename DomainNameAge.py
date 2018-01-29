import whois
import datetime
import csv
import re

with open("top-1m.csv", 'r+') as fr:
    with open('DomainAge.csv', 'w+') as fw:
        writer = csv.writer(fw, delimiter = ',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Domain Name', 'Creation date', 'Active time (minutes)','Active time (days)','Expiration date' ])
        readCSV = csv.reader(fr, delimiter=',')
        for line in readCSV:
#             temp = re.findall(r',([\w\.]+)', domain)
            domain = line[1]
            print(domain)
            result = whois.whois(domain)
            if (result != None and result.creation_date != None and result.expiration_date != None):
                if (isinstance(result.creation_date, datetime.datetime)):
                    a = datetime.datetime.now() - result.creation_date
                    crt = result.creation_date
                else:
                    a = datetime.datetime.now() - result.creation_date[0]
                    crt = result.creation_date[0]
                if (isinstance(result.expiration_date, datetime.datetime)):
                    exp = datetime.datetime.now() - result.expiration_date
                else:
                    exp = datetime.datetime.now() - result.expiration_date[0]
                writer.writerow([domain, crt, (a)/datetime.timedelta(minutes = 1), (a)/datetime.timedelta(days = 1),exp])
            domain = fr.readline()
