import csv
import json

def csvToJson(csvFilePath, jsonFilePath):
	# create a dictionary
	data = {}

	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		for rows in csvReader:

			# Assuming a column named 'No' to
			# be the primary key
			key = rows['No']
			data[key] = rows

	# Open a json writer, and use the json.dumps() 
	# function to dump data
	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=4))

# Decide the two file paths according to your 
# computer system
csvFilePath = r'Names.csv'
jsonFilePath = r'Names.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)
