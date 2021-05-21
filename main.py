import requests
import json
import urllib3
import csv
import argparse
parser = argparse.ArgumentParser(description="Tow arguments are required: start, end")
parser.add_argument("start", type=int, help="Scraping will start from this 'start' id")
parser.add_argument("end", type=int, help="Scraping will be over when the id reaches the 'end'")
args = parser.parse_args()

input_file = csv.DictReader(open("data.csv"))
existIds = [row['ID'] for row in input_file]

dict_writer = csv.DictWriter(open('data.csv', 'a+', newline=''), ["ID", "Name", "Address", "Phone", "Fax", "Email", "Website"])
if(len(existIds) == 0): dict_writer.writeheader()


http = urllib3.PoolManager()

for id in list(range(args.start, args.end)):
    print(id)
    url = 'https://www.myagedcare.gov.au/api/v1/find-a-provider/details/chsp/%d' % (id)

    # r = http.request('GET', url)
    # response = json.loads(r.data)
    r = requests.get(url)
    response = json.loads(r.content)
    
    if('nid' in response):
        data = {
            "ID": response['nid'],
            "Name": response['name'],
            "Address": response['serviceProvider']['address'] + ", " + response['serviceProvider']['address2'] if('serviceProvider' in response and 'address' in response['serviceProvider']) else '',
            "Phone": response['serviceProvider']['phone'] if('serviceProvider' in response and 'phone' in response['serviceProvider']) else '',
            "Fax": response['serviceProvider']['fax'] if('serviceProvider' in response and 'fax' in response['serviceProvider']) else '',
            "Email": response['serviceProvider']['email'] if('serviceProvider' in response and 'email' in response['serviceProvider']) else '',
            "Website": response['website'] if('website' in response) else '',
        }
        dict_writer.writerow(data)