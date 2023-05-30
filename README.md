# Product-Price-Comparison-Bard-API

This is a test Python application using the open source Google Bard API Library that allows a user to upload a csv file of products and the lowest price of each product is prompted using the Bard API, finally the filtered results are returned which include the price and site link.

![price comparison](https://github.com/zainmz/Product-Price-Comparison-Bard-API/assets/7949768/3824d1a8-9aa9-47e3-a990-89fc3204b01b)


The open source Bard-API created by  Antonio Cheong, Daniel Park can be found here:

https://github.com/dsdanielpark/Bard-API/tree/main

## Instructions on Usage ##
1) Clone or Download repository

2) You will have to replace (Line 8) the "XXXXX" with your __Secure-1PSID cookie

![image](https://github.com/zainmz/Product-Price-Comparison-Bard-API/assets/7949768/ae9ac895-692f-431d-915b-a70789059092)

3) *Cookie Instruction*

  - Visit https://bard.google.com/
  - F12 for console
  - Session: Application → Cookies → Copy the value of __Secure-1PSID cookie.
  - Paste the value in the location mentioned at step 2

4) *Edit Prompt for Localisation*

This script was created for the Sri lankan market by mentioning specifically the country in the prompt, you can change the prompt on Line 29

![image](https://github.com/zainmz/Product-Price-Comparison-Bard-API/assets/7949768/6fca9fca-c27f-4cfd-af1d-bca8c5108dfc)

5) CSV File Format
I've used a format for the CSV file as below

![image](https://github.com/zainmz/Product-Price-Comparison-Bard-API/assets/7949768/84615e8e-e695-4c2b-aa82-3724aea03c3e)


