README
=======
This application uses 3 external files to store some information:
- config.ini
- lastid.txt
- training_text.txt

config.ini
----------

Is the main configuration file of the app. Contains this parameters:
CONSUMER_KEY
CONSUMER_SECRET
ACCESS_TOKEN_KEY
ACCESS_TOKEN_SECRET

This 4 entries are keys that i got from twitter to allow the linking of my app to the twitter user.
I do not know if i can share some of this parameters. If you have a twitter official doc about that
share with me, please :-)

nickname

Is the screename of the user in twitter. Is used in HandleMsg.newmsg() to check if is mentioned in the
message that is parsing.

some other parameters will be added in a second time.

lastid.txt
-------------
contains the last id of the last message parsed. Is needed in order to restart the application without
parsing messages that has been previously parsed.
This file is created automatically on first startup.

training_text.txt
-----------------

contains all the messages text that has been is parsed. Is used by the markov_class to generate markov chains and text.
This file is created automatically on first startup.
