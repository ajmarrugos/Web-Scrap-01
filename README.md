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

- At first, user will be engaged with the interface to follow some instructions.
- The program will print a Welcome Message and show a list of options to work with. 
- User will be asked to select one of this options equivalent to a technology he/she is looking to work with.
- The program will wait until user enter the correct int option to continue flow.
- The options are show numerical commands and it could be selected with an int.

1. Python
2. SQL
3. Javascript

### 3. Interface: Second Argument

- The user will be asked to prompt an option to choose the URL from which he/she wants to get information.

### 4. Backend: Data Checkers

- App will verify the option selected and evaluate: if it's good, to continue app flow. If not, error message will be returned.
- Once option selection is completed, it will build a URL request with the options given as arguments.
- The request will be sent to web and app will wait for response.
- If URL not available/not responding, or anything fails, a new error message will be returned.
- If URL response, the app will load the HTML returned and parse it to XML.
- Next, app will evaluate the parsed XML, to detect the structure and to select a Scrapping Engine.
- If XML structure doesn't match with Engine Config, it will throw an Error message through Console.
- If the XML is good, it will return "Success!" And will start the Scrapping Engine.

### 5. Backend: Scrapping Engine

- It's a Dedicated set of scripts and rules to help process information from a certain source.
- Will search into the Parsed data the information of each offer and load it a cache file.
- Will search into the cached data, the exact words that the Offer Constructor needs to build the BaseModel instance.
- Will store each instance in dictionary format, with a key and value.
- Offer Constructor will take the instances created and arrange it into a Object Oriented structure to be: Shown / Exported / Sent.

### 6. Interface: Show Data

- I this step the app will show a message to confirm Data Processing success like this: "Data Processing Success!
- Will display the count of created Offers (instances) from data, like this: "## Instances created"
- It could have the option to retrieve from user the number of offers to be shown, like this:
"Please give number of Offers you want to review."
- If the user gives the correct int prompt, data will be displayed like this:

/ ----------------- /

Option 1: Offer 1
- Company: ___ (Characters)
- Offer: ___ (Characters)
- Salary: ___ (Int + Currecy)

/ ----------------- /

...

/ ----------------- /

- If not, error message will be shown. And will take you back to interface.

### 7. Interface: Review Data

- In this step user will be able to select which Offers wants to review before exporting or sending to SQL.
- A list of Offers will be shown as data concatenated inside cards.
- Next a new prompt will be displayed at last to confirm which Offer or Offers the user needs to review.

#### This prompt will accept requests with the following syntax:
- Just 1 Option: #1
- 2 Options: #1, #2
- Specified Options: #3, #6
- Range of Options: #5 - #8
- All Options: All / # (the symbol)

#### Once prompt is done, this confirmation messsage will be shown with number of offers on review.
- "You selected Offer/Offers

### 8. Interface: Export or Send

#### Once the Offer info is printed, the user could choose between 4 options:
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
