#code to book vaccination slot
import requests

my_headers = {'user-agent' : 'Mozilla/5.0'}
#response = requests.get('http://httpbin.org/headers', headers=my_headers)

vaccine_type = "COVISHIELD"
min_age = 18
dose=1
if(dose == 1):
    available_dose_capacity = "available_capacity_dose1"   
else:
    available_dose_capacity = "available_capacity_dose2"
possible_slots=[]

response = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=294&date=28-05-2021", headers=my_headers)

print(response)
print('----------------------------------')
#print(response.content())
print('----------------------------------')
#text = response.text()
#print(text)
print("---------------------------------")
centres = response.json() 



#let's try to parse it and print
#print(f"Number of centres for the given district : {centres['centers'].length}")
required_keys = []
# find the all the centres for vaccine=<input vaccine type>, min_age_limit=<age>, dose=1/2
for key in centres.keys():
    print(f"Key : {key}   length of value : {len(centres[key])}")
    centre_list = centres[key]
    
    print(centre_list[0].keys())
    for centre in centre_list:
        print(centre['name'],centre['address'],sep=',')
        for session in centre['sessions']:
            print(session['date'],session['available_capacity'],session['min_age_limit'], 
                  session['vaccine'],session['available_capacity_dose1'],session['slots'])
            if((session['vaccine'] == vaccine_type) && (session['min_age_limit'] == min_age) 
               && (session[available_dose_capacity] > 0))
            #add the details in the list
            possible_slots.append(session)
            

#lets print the possible slots
print("***********************************************************************************")
print(possible_slots)
print("***********************************************************************************")
        
        
        
        