import hashlib
import platform
import sys
from os import system

# Required libraries
import requests
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier, geocoder, parse

kOperativeSystem = platform.system()

def Verify_Premium_Key():
    """Online Premium Key Validation System"""
    print("\n\033[33m=======================================")
    print("\033[35m       MJ PHONE INFO TOOL - PREMIUM     ")
    print("\033[33m=======================================\033[0m")
    
    user_key = input("\033[36m[?] Enter your Premium Activation Key: \033[0m").strip()
    
    if not user_key:
        print("\033[31m[-] Key cannot be empty!\033[0m")
        sys.exit()

    print("\033[32m[*] Verifying key with server...\033[0m")
    
    # Master premium key jo hamesha chalegi
    MASTER_KEY = "MANISH-VIP-77"
    
    try:
        url = "https://raw.githubusercontent.com/manishjanarda678-art/phone-infoga/main/valid_keys.txt"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            valid_keys = response.text.splitlines()
            
            if user_key in valid_keys or user_key == MASTER_KEY:
                print("\033[32m[+] Access Granted! Premium License Activated.\033[0m\n")
                return True
            else:
                print("\033[31m[-] Invalid Key! Access Denied.\033[0m")
                print("\033[33m[!] To buy a premium key, contact developer (MANISH) on Telegram/WhatsApp.\033[0m\n")
                sys.exit()
        else:
            if user_key == MASTER_KEY:
                print("\033[32m[+] Access Granted via Master Key!\033[0m\n")
                return True
            print("\033[31m[-] Server Error! Try again later.\033[0m")
            sys.exit()
            
    except Exception:
        if user_key == MASTER_KEY:
            print("\033[32m[+] Offline Access Granted via Master Key!\033[0m\n")
            return True
        print("\033[31m[-] Network Error! Internet connection is required to verify key.\033[0m")
        sys.exit()

def Main():
    Verify_Premium_Key()

    # Fixed Banner: MJ .COM perfectly formatted
    print('''
\033[32m███╗   ███╗██████╗     ██████╗ ██████╗ ███╗   ███╗
\033[33m████╗ ████║╚══███║    ██╔════╝██╔═══██╗████╗ ████║
\033[34m██╔████╔██║   ███║    ██║     ██║   ██║██╔████╔██║
\033[35m██║╚██╔╝██║   ███║    ██║     ██║   ██║██║╚██╔╝██║
\033[36m██║ ╚═╝ ██║██████║    ╚██████╗╚██████╔╝██║ ╚═╝ ██║ \033[32mV2.0 PREMIUM
\033[31m╚═╝     ╚═╝╚═════╝     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝
\033[33m88 88b 88 888888  dP"Yb   dP""b8    db        
\033[31m88 88Yb88 88__   dP   Yb dP   `"   dPYb       
\033[38m88 88 Y88 88""   Yb   dP Yb  "88  dP__Yb      
\033[34m88 88  Y8 88      YbodP   YboodP dP""""Yb
\033[35m*****\033[38m*******\033[32mPHONE NUMBERS INFORMATION \033[38m*******\033[35m********
\033[33m*\033[31mDeveloper:\033[35mMANISH (MJ.COM)
\033[35m***********\033[31m************\033[33m***************\033[32m****************''')
    
    print('[!] Phone number example: +56 9 1122 3344')
    Number = input('[!] Premium Panel < MJ.COM > Enter Phone Number :: ')

    if not Number.strip():
        print("[!] Invalid Input!")
        return

    KEY = '7fea841369ae4b5ea7e394219f5bba11'

    try:
        ParsedNumber = parse(Number.replace(' ', ''), None)
        Country = geocoder.description_for_number(ParsedNumber, 'en')
        Service = carrier.name_for_number(ParsedNumber, 'en') or "Unknown Carrier"

        if not Country:
            print("[!] Could not find country information for this number.")
            return

        geocoder_api = OpenCageGeocode(KEY)
        PhoneInformation = geocoder_api.geocode(Country)

        if PhoneInformation and len(PhoneInformation) > 0:
            Geometry = PhoneInformation[0]
            Latitude = Geometry['geometry']['lat']
            Longitude = Geometry['geometry']['lng']
            State = Geometry['components'].get('state', 'N/A')
            Timezone = Geometry['annotations'].get('timezone', {}).get('name', 'N/A')
            CountryCode = Geometry['components'].get('country_code', 'N/A')
            Continent = Geometry['components'].get('continent', 'N/A')
            
            MapLink = f"https://www.google.com/maps/search/?api=1&query={Latitude},{Longitude}"
        else:
            Latitude = Longitude = State = Timezone = CountryCode = Continent = "Not Found"
            MapLink = "N/A"

        Output = f'''
=============== PREMIUM RESULTS ===============
 * Country: {Country} [{CountryCode.upper()}] [{Continent}]
 * State: {State} [Approximate]
 * Carrier: {Service}
 * Timezone: {Timezone}
 * Latitude: {Latitude} [Approximate]
 * Longitude: {Longitude} [Approximate]
 * Google Map Link: \033[36m{MapLink}\033[0m
 ===============================================
'''
        print(Output)
        
        SaveDataResponse = input('[!] Do you want to save the information in a file?[y/N]: ')

        if SaveDataResponse.upper() == 'Y':
            with open('Log.txt', 'a', encoding='utf-8') as LogFile:
                LogFile.write(f'Information related to the number: {Number}\n{Output}\n')
            print('\nInformation saved in [Log.txt]')
        else:
            print('\n:: Goodbye, stay safe!')

    except Exception as e:
        print(f'\n:: Error occurred: {e}')

def ClearScreen() -> None:
    system('cls' if kOperativeSystem == 'Windows' else 'clear')

if __name__ == '__main__':
    try:
        ClearScreen()
        Main()
    except KeyboardInterrupt:
        print('\n:: Exiting tool...')
