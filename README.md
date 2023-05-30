# Product-Price-Comparison-Bard-API

This is a test Python application using the open source Google Bard API Library that allows a user to upload a csv file of products and the lowest price of each product is prompted using the Bard API, finally the filtered results are returned which include the price and site link.

![image](https://github.com/zainmz/Product-Price-Comparison-Bard-API/assets/7949768/41329189-add6-48fb-8dab-1ffe2207dc8c)


The open source Bard-API created by  Antonio Cheong, Daniel Park can be found here:

https://github.com/dsdanielpark/Bard-API/tree/main

## Instructions on Usage ##
1) Clone or Download repository

2) You will have to replace (Line 8) the "XXXXX" with your __Secure-1PSID cookie
![image](https://github.com/zainmz/Product-Price-Comparison-Bard-API/assets/7949768/109a7eeb-8997-4a80-b05d-8ab9bc2aaa3e)

3) *Cookie Instruction*

  - Visit https://bard.google.com/
  - F12 for console
  - Session: Application → Cookies → Copy the value of __Secure-1PSID cookie.
  - Paste the value in the location mentioned at step 2

4) *Edit Prompt for Localisation*

This script was created for the Sri lankan market by mentioning specifically the country in the prompt, you can change the prompt on Line 29
![image](https://github.com/zainmz/Product-Price-Comparison-Bard-API/assets/7949768/e8b98feb-40ca-4a6b-bcbd-917882add717)

5) CSV File Format
I've used a format for the CSV file as below

![image](https://github.com/zainmz/Product-Price-Comparison-Bard-API/assets/7949768/93ccc527-b124-4bc5-badc-c08b756f52e1)


