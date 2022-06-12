# Import Libraries
import os
import time
import json

from IPy import IP
from art import tprint
from termcolor import colored
from urllib.request import urlopen

# 'InternFunctions' 
class InternFunctions:
    def ClearTerminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
IF = InternFunctions()


# 'SetUp'
class SetUp:
    def WelcomeMsg(self):
        IF.ClearTerminal()
        tprint('Antio', font='bulbhead')

    def AutoUpdate(self):
        AutoUpdate = open('autoupdate.json', 'r+')
        AutoUpdateData = json.load(AutoUpdate)   
        # Check Update
        if AutoUpdateData['updated'] == False:
            time.sleep(1)
            print()
            RequiredLibs = AutoUpdateData['libs'].split(' ')
            CurrentLibCount = -1
            # Update Libraries
            for i in range(len(RequiredLibs)):
                CurrentLibCount = CurrentLibCount + 1
                os.system('pip install ' + RequiredLibs[CurrentLibCount])
            # Update 'Updated' To 'True'
            UpdateData = {"updated": True, "libs": AutoUpdateData['libs']}
            AutoUpdate.seek(0)
            AutoUpdate.truncate()
            json.dump(UpdateData, AutoUpdate, indent=2)
            print(colored('Dependencies Installed!', 'green', attrs=['bold']))

    def EnterInfo(self):
        time.sleep(1)
        IF.ClearTerminal()
        global InternetProtocol
        InternetProtocol = input(colored('Internet Protocol (IP): ', 'green', attrs=['bold']))
        # Validate 'InternetProtocol'
        try:
            IP(InternetProtocol)
        except ValueError:
            print()
            time.sleep(0.5)
            print(colored('Validating ...', 'green', attrs=['bold']))
            print()
            time.sleep(1)
            print(colored('Error : Invalid Input', 'red', attrs=['bold']))
SU = SetUp()


# 'Lookup'
class Lookup:
    def Lookup(self):
        LookupUrl = 'https://ipinfo.io' + InternetProtocol + '/json'
        LookupResponse = urlopen(LookupUrl)
        LookupData = json.load(LookupResponse)
        # Define Country, City, ...
        LookupCountry = LookupData['country']
        LookupCity = LookupData['city']
        LookupTimezone = LookupData['timezone']
        LookupProvider = LookupData['org']
        LookupLocation = LookupData['loc']
        # Split / Replace Country, City, ...
        ContinentTimezone = str(LookupTimezone).split('/')[0]
        CityTimezone = str(LookupTimezone).split('/')[1]
        CityTimezone = str(CityTimezone).replace('_', ' ')
        LookupTimezone = ContinentTimezone + ' / ' + CityTimezone
        LookupProvider = str(LookupProvider).split(' ')[1]
        LookupLocation = str(LookupLocation).replace(',', ' ')
        # Final Country, City, ...
        global Location
        Location = LookupCountry + ' / ' + LookupCity
        global Provider
        Provider = LookupProvider
        global LocationLang
        LocationLang = LookupLocation
        global Timezone
        Timezone = LookupTimezone
LU = Lookup()


class Result:
    def PrintResult(self):
        print()
        print(colored(Location, 'green', attrs=['bold']))
        print(colored(LocationLang, 'green', attrs=['bold']))
        print(colored('-----------------------', 'green', attrs=['bold']))
        print(colored(Timezone, 'green', attrs=['bold']))
RT = Result()

# Run Antio
SU.WelcomeMsg()
SU.AutoUpdate()
SU.EnterInfo()
LU.Lookup()
RT.PrintResult()