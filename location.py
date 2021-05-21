import requests
import json
import urllib3
http = urllib3.PoolManager()
fo = open("location_list.txt", "w")
for a in [chr(x) for x in range(ord('a'), ord('z')+1)]:
    # for b in [chr(x) for x in range(ord('a'), ord('z')+1)]:
    #     for c in [chr(x) for x in range(ord('a'), ord('z')+1)]:
    print(a)
    url = 'https://www.myagedcare.gov.au/locality-autocomplete?q='+a

    r = http.request('GET', url)
    response = json.loads(r.data)
    print(len(response))
    for item in response:
        fo.write(item['value'])
        fo.write('\n')
fo.close()