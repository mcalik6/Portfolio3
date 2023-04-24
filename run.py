
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Portfolio3')

def get_name ():
    """
    function is getting name of the user
    """
    print ("Thank you for contacting our service team\n")
    name_str = input("Enter Your name here \n")
    return name_str


def update_name_worksheet(name):
    """
    Update name sheet
    """
    print("thank you for your name...\n")
    name_worksheet = SHEET.worksheet("name")
    name_worksheet.append_row([name])
  
name = get_name()
update_name_worksheet(name)