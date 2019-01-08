# Automation-using-selenium
[![Build Status](https://travis-ci.org/nileshpatra/Automation-using-selenium.svg?branch=master)](https://travis-ci.org/nileshpatra/Automation-using-selenium)

This reposirtory contains three python notebooks for web automation using selenium.
1. Whatsapp automation generator
  - selenium is imported , adn so is webdriver and keys
  - firefox browser is opened using webdriver instance
  - the driver object gets the website of whatsapp
  - the xpath of search bar is then passed
  - the required name is sent using ```send_keys()``` function
  - then entered key is presses for the required name by using ```u'\ue007``` in ```send_keys()```
  - the message instance is then created using the message box of the chat
  - finally message is entered and looped over for a fixed number of times to send the message
  
2. Google search using selenium
  - imported webdriver and https://www.google.com site is passed to it
  - the site then opens up in firefox
  - the xpath of search bar is passed , the message is sent using ```send_keys()``` function and enter key is pressed 
    with ```u'\ue007```
  
3. google for filling using selenium :
  - created a dummy form
  - form is available at : https://docs.google.com/forms/d/e/1FAIpQLSfwPaHQZv9Ft6s2uvbmEWGuqkA9h7dFns0Xgg0uKHGOF1Sc-  g/viewform?vc=0&c=0&w=1
  - passed xpath for the radio buttons and made an array
  - filling the form 5 times , and each time, random number is selected from the list of entries
  - the radio buttons are ticked accordingly and then ticked
  - finally the google form is submitted.
  
  Finally the responses are recoreded from the bot :
  <img src = https://github.com/nileshpatra/Automation-using-selenium/blob/master/Screenshot_2019-01-04%20Event%20RSVP.png>
  
  4. facebook autologin:
  
    - type the facebok username and password in the variables username and password
    - the webdriver gets ther xpath of username and password text boxes , it send the text tot those
    - the webdriver then clicks on login by getting the xpath
    
  5. Stackoverflow search :
    - type in the message to the ```message``` variable in  stack_overflow_search.py and run the python file to get       desired search results of message from stackoverflow.
