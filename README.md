# RendezVu

A web app that will find the most convenient meetup location between members of a friend group.

# Built With: 
Languages: Python, HTML, JavaScript
APIs: Google Maps 
Framework: Python Flask

# Inspiration
Each one of us has experienced the struggle of deciding on a meetup point when we hang out with our friends. Often times the indecisiveness of choosing the location becomes a roadblock that prevents the meetup from even occurring. This is a common scenario that many people face and it can be extremely frustrating. Our annoyance and dissatisfaction when making plans served as the inspiration for RendezVu. We wanted to create a platform that would allow users to quickly figure out a convenient place to gather. 

# What it Does
RendezVu grabs the current location (latitude and longitude) of each member in a group and uses those coordinates in an algorithm to calculate a central location. It then displays the resulting address and locations of all the users as markers on a google map that can be manipulated by the user. 

# How We Built It
Our application primarily revolves around the Google Maps API. We used Python Flask for our backend and Google App Engine was used to deploy the server. Using HTML and CSS, we designed a website to run the program.

# What’s Next?
In the future, we hope to add additional features that will increase the complexity of the program. One of the goals at the top of our list is to allow users to specify a group of people they wish to meet up with. Currently, the program grabs the locations of all users who log onto the website and calculates a central gathering point. RendezVu will be of more use to users if the user has the ability to pick and choose the people they specifically want to meet up with. Another feature we would like to add is user authentication. Implementing this feature will be an added security measure that verifies the identity of the user. User accounts can also keep logs of all the groups a user forms or is a member of, in case they choose to meetup with that same group again.

A long term goal is to connect RendezVu to other social media platforms (e.g. Facebook Messenger, Snapchat, Google Groups). People already use social media to communicate with their friends, therefore implementing our program into established applications will provide additional convenience for the user. Users will not have to to open a new browser to find the best meeting point between their friends, but can do it straight from the messaging application they already have and use. 

# How to Run
Clone the file and open the main.py file. Run this python script and use the link given in the console to navigate to the browser.
