# Import Libraries
import sys
import time
import json

from IPy import IP
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel
from urllib.request import urlopen


# Main Window
class AppWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # GUI Style
        self.setFixedSize(700, 400)
        self.setWindowTitle('Intan - IP Analyzer')
        self.setStyleSheet('background-color: #FFFFFF;')

        # IP Input
        self.IpInput = QLineEdit(self)
        self.IpInput.move(35, 35)
        self.IpInput.resize(375, 60)
        self.IpInput.setPlaceholderText('Internet Protocol')
        self.IpInput.setStyleSheet('border: none; border-radius: 20px; background-color: #EEEEEE; color: #606060; padding-left: 10px; font-weight: 500; font-size: 15px;')

        #####################################################

        def Scan():
            # Validate IP
            try:
                InternetProtocol = self.IpInput.text()
                IP(InternetProtocol)
            except ValueError:
                print('Error : Invalid IP')
                time.sleep(2)
                sys.exit('Exit')
            
            # Get Informations
            LookupUrl = 'https://ipinfo.io/' + InternetProtocol
            LookupResponse = (LookupUrl)
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
            Location = LookupCountry + ' / ' + LookupCity
            Provider = LookupProvider
            LocationLang = LookupLocation
            Timezone = LookupTimezone
            # Set Text
            self.LocationValue.setText(Location)
            self.ProviderValue.setText(Provider)
            self.LongLatValue.setText(LocationLang)
            self.TimezoneValue.setText(Timezone)

        #####################################################

        # Scan Button
        self.ScanBtn = QPushButton('Scan', self)
        self.ScanBtn.move(430, 35)
        self.ScanBtn.resize(235, 60)
        self.ScanBtn.setStyleSheet('border: none; border-radius: 20px; background-color: #006EE6; color: #FFFFFF; font-weight: 500; font-size: 15px;')
        self.ScanBtn.clicked.connect(Scan)
        
        #####################################################

        # Location Background
        self.LocationBg = QLabel(self)
        self.LocationBg.move(35, 130)
        self.LocationBg.resize(305, 100)
        self.LocationBg.setStyleSheet('border: none; border-radius: 20px; background-color: #EEEEEE;')

        # Location Title
        self.LocationTitle = QLabel(self)
        self.LocationTitle.setText('Location')
        self.LocationTitle.move(50, 135)
        self.LocationTitle.resize(200, 40)
        self.LocationTitle.setStyleSheet('background-color: #EEEEEE; border-radius: 20px; color: #606060; font-size: 20px; font-weight: 500;')

        # Location Value
        self.LocationValue = QLabel(self)
        self.LocationValue.setText('DE / Stuttgart')
        self.LocationValue.move(50, 175)
        self.LocationValue.resize(250, 40)
        self.LocationValue.setStyleSheet('background-color: #EEEEEE; border-radius: 20px; color: #222222; font-size: 23px; font-weight: 500;')

        #####################################################

        # Provider Background
        self.ProviderBg = QLabel(self)
        self.ProviderBg.move(360, 130)
        self.ProviderBg.resize(305, 100)
        self.ProviderBg.setStyleSheet('background-color: #EEEEEE; border-radius: 20px; color: #606060; font-size: 20px; font-weight: 500;')

        # Provider Title
        self.ProviderTitle = QLabel(self)
        self.ProviderTitle.setText('Provider')
        self.ProviderTitle.move(375, 135)
        self.ProviderTitle.resize(200, 40)
        self.ProviderTitle.setStyleSheet('background-color: #EEEEEE; border-radius: 20px; color: #606060; font-size: 20px; font-weight: 500;')

        # Provider Value
        self.ProviderValue = QLabel(self)
        self.ProviderValue.setText('Starlink')
        self.ProviderValue.move(375, 175)
        self.ProviderValue.resize(200, 40)
        self.ProviderValue.setStyleSheet('background-color: #EEEEEE; border-radius: 20px; color: #222222; font-size: 23px; font-weight: 500;')

        #####################################################

        # Timezone Background
        self.TimezoneBg = QLabel(self)
        self.TimezoneBg.move(35, 250)
        self.TimezoneBg.resize(305, 100)
        self.TimezoneBg.setStyleSheet('background-color: #EEEEEE; border-radius: 20px; color: #606060; font-size: 20px; font-weight: 500;')

        # Timezone Title
        self.TimezoneTitle = QLabel(self)
        self.TimezoneTitle.setText('Timezone')
        self.TimezoneTitle.move(50, 255)
        self.TimezoneTitle.resize(200, 40)
        self.TimezoneTitle.setStyleSheet('background-color: #EEEEEE; border-radius: 20px; color: #606060; font-size: 20px; font-weight: 500;')

        # Timezone Value
        self.TimezoneValue = QLabel(self)
        self.TimezoneValue.setText('Berlin / Germany')
        self.TimezoneValue.move(50, 295)
        self.TimezoneValue.resize(200, 40)
        self.TimezoneValue.setStyleSheet('background-color: #EEEEEE; border-radius: 20px; color: #222222; font-size: 23px; font-weight: 500;')

        #####################################################

        # Long- & Latitude Background
        self.LongLatBg = QLabel(self)
        self.LongLatBg.move(360, 250)
        self.LongLatBg.resize(305, 100)
        self.LongLatBg.setStyleSheet('background-color: #EEEEEE; border-radius: 20px; color: #606060; font-size: 20px; font-weight: 500;')

        # Long- & Latitude Title
        self.LongLatTitle = QLabel(self)
        self.LongLatTitle.setText('Long- & Latitude')
        self.LongLatTitle.move(375, 255)
        self.LongLatTitle.resize(200, 40)
        self.LongLatTitle.setStyleSheet('background-color: #EEEEEE; border-radius: 20px; color: #606060; font-size: 20px; font-weight: 500;')

        # Long- & Latitude Value
        self.LongLatValue = QLabel(self)
        self.LongLatValue.setText('69.4200 -420.6969')
        self.LongLatValue.move(375, 295)
        self.LongLatValue.resize(250, 40)
        self.LongLatValue.setStyleSheet('background-color: #EEEEEE; border-radius: 20px; color: #222222; font-size: 23px; font-weight: 500;')

# Define & Run
if __name__ == '__main__':
    App = QtWidgets.QApplication(sys.argv)
    AppWindow = AppWindow()
    AppWindow.show()
    sys.exit(App.exec())