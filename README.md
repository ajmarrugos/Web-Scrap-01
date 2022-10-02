# WebScrapping Project

### Project designed with the purpose to get information from Job Posting webpages.
### Will allow the user to get Job Offers data, like:
- Company or Enterprise name
- Job Position
- Salary

## Features
- Will have built-in options to make URL request to some kind of webpages.
- Will have an interface to guide the user to use the WebScrapping Engine.
- The Engine will extract data from webpage to create instances that can be reviewed in the Console.
- Once this data is processed and approved, the User can export this to a JSON format or Send it and load it to a MySQL Server.

## Usage

- Interactive (Main program to execute and interact through console)
- Non Interactive (Set of scripts with predefined options to process requests)

## Non Interactive Mode
./WebScrapURL.py
- Options: 1,2,3 / 1,2,3 (Look interactive)

## Interactive Mode Flow

### 1. Start the Interface
./WebScrapBRO.py

### 2. Interface: First Argument

The user will be asked to prompt an option to get the technology he/she is looking to work for. The options will be listed and shown as and Integer argument.
This options will be shown like this:

1. Python
2. SQL
3. Javascript

### 3. Interface: Second Argument

The user will be asked to prompt an option to choose the URL from which he/she wants to get information.

### 4. Backend: Data checking

- App verifies the arguments/options chossed and if they are not good, error message will be returned.
- App will build a URL request with the options given, and will send it to web and wait for response, if URL not available, or URL not responding, or/and anything fails, an error message will be returned.
- App will load the HTML returned and parse it to XML.
- App will verify the XML structure loaded to execute the Scrapping Engine and will throw Success or Error message in case the parsed data doesn't matchs or functions with the Scrapping Engine.

### 5. Backend: Scrapping

- The Engine will search into the Parsed data the information of each offer and load it a cache file.

- The Engine will search into the cached data, the accurate information that the Offer needs to be build or completed and will store each into a Dictionary with a key and value.

- The Model Constructor will take the data gathered form the engine and organize it into a Object Oriented structure, to be: Shown / Exported / Sent.

### 6. Interface: Show Data

- The app will show a message to confirm Data Processing success like this: "Data gathering Success!

- Also will display the count of Offers gathered from data like this:
"Please give number of Offers you want to review."

- Once the user gives the int prompt (TEST CASE) the app will clean the console and return a list of Offers in a friendly view as this example:

/ ----------------- /

Option 1: Offer 1
- Company: ___ (Characters)
- Offer: ___ (Characters)
- Salary: ___ (Int + Currecy)

/ ----------------- /

...

/ ----------------- /

### 7. Interface: Review Data

- The list of Offers will be shown as concatenated objects and in this step user will be able to select which one wants to review to export or send to SQL.

- In this order a prompt will be displayed to confirm which Offer or Offers the user needs to select:

#### This could be requested to the app with the following syntax:
- Just 1 Option: #1
- 2 Options: #1, #2
- Specified Options: #3, #6
- Range of Options: #5 - #8
- All Options: All / # (the symbol)

#### Once prompt is done: Confirmation messsage will be shown and data
- "You selected Offer/Offers #"
- "Shows Offer info"

### 8. Interface: Export or Send

#### Once the Offer info is printed, the user could choose from 3 options:
- Export to CSV/JSON (Interface will ask for a filename and path)
- Send to SQL Server (Interface will ask for Server IP and User credentials)
- Abort (Return to step 6: Show Data)
- Exit (Cleans the chache an closes the program)

### AUTHORS
- Pablo Agudelo
- Víctor Uroza
- Alejandro Urán
- Alberto Marrugo

### COMPANIES INVOLVED
- Holberton School
- Hitch.ai
