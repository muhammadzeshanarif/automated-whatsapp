# automated-whatsapp

A terminal automation app to send bulk whatsapp messages

## How to configure and use this repo

1. Open the Terminal / CMD app on your machine
2. Clone this repo on your machine `git clone git@github.com:zeshanarifios/automated-whatsapp.git`
3. Navigate to the directory you've just cloned, its name would be `automated-whatsapp`
4. Create a virutal environment using this command: `python3 -m venv vauto`
5. Activate the virual environment you just created using this command: `source vauto/bin/activate`
6. Install all the requirements using this command: `pip3 install -r requirements.txt`
7. Once the virtual environment starts, you're all set to send messages now
8. Update the `numbers.txt` file with the whatsapp phone numbers that you want to send a message to
9. Update the `message.txt` file with the message you want to send to the numbers you've added in the previous step
10. Now you just need to run this command: `python3 controller.py` and follow along!
