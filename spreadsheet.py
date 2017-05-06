import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Copy of Minnesota Accountants").sheet1

list_of_hashes = sheet.get_all_records()
print(list_of_hashes)

