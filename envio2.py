# Example Python program to upload a file to an FTP server
# in binary mode
import os
from ftplib import FTP
# Create an FTP object and connect to the server

ftpObject = FTP(host="web20.swisscenter.com");
print(ftpObject.getwelcome());
# Login to the server
#ftpResponseMessage = ftpObject.login();
ftpResponseMessage = ftpObject.login(user="akc001_datos1_espectrales", passwd="wmlTHuBvYF.umc7")
print(ftpResponseMessage);
# Change to the required working directory
ftpResponseMessage = ftpObject.cwd("/upload");
print(ftpResponseMessage);
# Open the file in binary mode
fileObject = open("/home/pi/spectrometer/spectrums/", "rb");
file2BeSavedAs = "28.txt"
ftpCommand = "STOR %s"%file2BeSavedAs;
# Transfer the file in binary mode
ftpResponseMessage = ftpObject.storbinary(ftpCommand, fp=fileObject);
print(ftpResponseMessage);
