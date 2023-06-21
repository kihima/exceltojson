import pdf_to_json as p2j
import json

# web document : UDHR
url = "https://www.iebc.or.ke/docs/rov_per_polling_station.pdf"

# Convert the document into a python dictionary
lConverter = p2j.pdf_to_json.pdf_to_json_converter()
lDict = lConverter.convert(url)

print(json.dumps(lDict, indent=4))