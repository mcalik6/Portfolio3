
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

def get_pending():
    """
    Now we try to fix that before making call
    """
    answer1 = None
    answer2 = None
    answer3 = None 

    while answer1 not in ['Y','N']:
        answer1 = input("Did you turned  off your computer ? (Y/N) \n").upper()

    while answer2 not in ['Y','N']:
        answer2 = input("Did you turned your computer on? (Y/N) \n").upper()
    
    while answer3 not in ['Y','N']:
        answer3 = input("Is it working now?? (Y/N) \n").upper()

    status= None
    if answer1 == 'Y' and answer2 == 'Y' and answer3 == 'Y':
        status = 0
        """print("There is no need to call you your computer is working\n")"""
    else:
        status = 1
        """"print("Wait for our support teem to contact you \n")"""

    return status

def update_pending_worksheet(pending):
    """
    Update pending calls  sheet plus give customers of how long does he have to wait
    """
    print("Thank You for your time. please let us check our pending calls\n")
    
    pending_worksheet = SHEET.worksheet("pending")
    """pending_worksheet.append_row([pending])"""
    pending_list = pending_worksheet.col_values(1)
    queue_number = pending_list.count("1")
    if pending == 0:
        print ("there is no need to contact you, your computer is workinng now\n")
    else:
        pending_worksheet.append_row([pending])
        if queue_number == 0:
            print("your call has been registered. We will contact you shortly\n")
        else:
            print ("Your call has been registered. You are number {} in the que\n".format(queue_number+1))


    

def main():

    name = get_name()
    update_name_worksheet(name)
    surname = get_surname()
    update_surname_worksheet(surname)
    phone = get_phone()
    update_phone_worksheet(phone)
    pending = get_pending()
    update_pending_worksheet(pending)

main ()