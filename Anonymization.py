import json
import os
from faker import Faker
from collections import defaultdict




def anonymization_data(file, export_file, same_directory):
    here = os.path.dirname(os.path.abspath(__file__))
    if same_directory == True:
        file = os.path.join(here, file) 
        export_file = os.path.join(here, export_file) 
    try:
        f = open(file)
        # returns JSON object as a dictionary
        data = json.load(f)
        
        faker  = Faker('fi_FI')
        # Create mappings of names &amp; emails to faked names &amp; emails.
        names  = defaultdict(faker.name)
        emails = defaultdict(faker.email)
        phonenumber = defaultdict(faker.phone_number)
        address_streetname = defaultdict(faker.street_name)
        address_buildingnumber = defaultdict(faker.building_number)
        address_postalcode  = defaultdict(faker.postcode)
        address_townname = defaultdict(faker.city)


        # Iterating through the json list
        for i in data['persons']:
            i['name'] =  names[i['name']]
            i['email'] =  emails[i['email']]
            i['phonenumber'] =  phonenumber[i['phonenumber']]
            i['address']['streetname'] =  address_streetname[i['address']['streetname']]
            i['address']['buildingnumber'] =  address_buildingnumber[i['address']['buildingnumber']]
            i['address']['postalcode'] =  address_postalcode[i['address']['postalcode']]
            i['address']['townname'] =  address_townname[i['address']['townname']]
        
        try:
            with open(export_file, "w") as outfile: 
                json.dump(data, outfile)
        except:
            print("An exception occurred while wrting the output file")  
        
        # Closing file
        f.close()
    except:
        print("An exception occurred while opening the file")  


if __name__ == "__main__":
   file = 'persons.json'
   export_file = 'persons_anonymized.json'
   same_directory = True
   anonymization_data(file, export_file, same_directory)