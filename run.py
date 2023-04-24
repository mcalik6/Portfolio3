
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
    print ("This is PC related departement\n")
    name_str = input("Please provide your name \n")
    return name_str

def update_name_worksheet(name):
    """
    Update name sheet
    """
    print("thank you for your name...\n")
    name_worksheet = SHEET.worksheet("name")
    name_worksheet.append_row([name])

def get_surname ():
    """
    function is getting surname of the user
    """
    surname_str = input("Please provide your Surname \n")
    return surname_str
    
def update_surname_worksheet(surname):
    """
    Update Surname sheet
    """
    print("thank you for your surname...\n")
    surname_worksheet = SHEET.worksheet("surname")
    surname_worksheet.append_row([surname])

def get_phone ():
    """
    function is getting phone number of the user
    """
    while True:
        try:
            number = int(input ("Enter Your phone number: \n"))
            return number
        except ValueError:
            print ("Invalid input, Please enter phone number")
    
def update_phone_worksheet(phone):
    """
    Update Phone number sheet
    """
    print("thank you for your Phone number...\n")
    phone_worksheet = SHEET.worksheet("phone_number")
    phone_worksheet.append_row([phone])

def main():

    name = get_name()
    update_name_worksheet(name)
    surname = get_surname()
    update_surname_worksheet(surname)
    phone = get_phone()
    update_phone_worksheet(phone)

main ()