#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

total = len(enron_data)
salary_count = len([person['salary'] for person in enron_data.values() if person['salary'] != 'NaN'])
email_count = len([person['salary'] for person in enron_data.values() if person['email_address'] != 'NaN'])
payments_nan_count = len([person['salary'] for person in enron_data.values() if person['total_payments'] == 'NaN'])
poi_payments_nan_count = len([person['salary'] for person in enron_data.values() if (person['total_payments'] == 'NaN' and person['poi'])])

poi_count = sum(person['poi'] for person in enron_data.values())

print("Total persons:", total)
print("Total features:", len(enron_data["METTS MARK"]))
print("Persons of interest", poi_count)
print("Prentice James total stock", enron_data["PRENTICE JAMES"]["total_stock_value"])
print("Wesley Colwell to poi emails", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print("Jeffrey K Skilling stock options", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
print("Kenneth Lay total payments", enron_data["LAY KENNETH L"]["total_payments"])
print("Jeff skilling total payments", enron_data["SKILLING JEFFREY K"]["total_payments"])
print("Andrew fastow total payments", enron_data["FASTOW ANDREW S"]["total_payments"])
print("Salary count", salary_count)
print("Email count", email_count)
print("NaN in total payments", payments_nan_count/float(total))
print("NaN in total payments for poi", poi_payments_nan_count/float(total))
