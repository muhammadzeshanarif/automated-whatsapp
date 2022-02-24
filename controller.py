"""This is automated WhatsApp controller, It controls all the process."""
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from reader import Reader
from chrome_web_driver import ChromeWebDriver


original_message = Reader.get_whatsapp_message()
numbers = Reader.get_whatsapp_numbers()
numbers_count = len(numbers)

driver = ChromeWebDriver()
driver.load_whatsapp()

print('Sending ... ')
count = 1
for number in numbers:
    if not number:
        continue
    print('{count}: {number}'.format(count=count, number=number))
    driver.send(number, original_message)
    count = count + 1
