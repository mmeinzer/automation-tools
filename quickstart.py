from __future__ import print_function
import httplib2
import os
import urllib
import requests
import json

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1FbW7phhfvLR1oseNJg-zd-LkrzFR9hYCGTlLnrDmRSg'
    rangeName = 'Businesses!A2:A'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])
    start_details = "https://maps.googleapis.com/maps/api/place/details/json?"
    start_text = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    key_url = "&key=AIzaSyAamv8TVOVdduhy0FCPYwIXOEtmZkMw-DY"

    for row in values:
        mapping = {'query': row[0]}
        query = urllib.urlencode(mapping)
        req_url_text = start_text + query + key_url
        res = requests.get(req_url_text).json()

        try:
            #if no results the index [0] is out of range
            mapping = {'place_id': res['results'][0]['place_id']}
        except IndexError:
            #if no search results proceed to the next search item
            print("No Search Results")
            print()
            continue
        
        place_id = urllib.urlencode(mapping)
        req_url_details = start_details + place_id + key_url
        res = requests.get(req_url_details).json()
        
        try:
            website_url = res['result']['website']
        except KeyError:
            website_url = "None Found"

        try:
            phone_number = res['result']['formatted_phone_number']
        except KeyError:
            phone_number = "None Found"

        try:
            address = res['result']['formatted_address']
        except KeyError:
            address = "None Found"

        print("URL:     " + website_url)
        print("Phone:   " + phone_number)
        print("Address: " + address)
        print()
            
if __name__ == '__main__':
    main()

