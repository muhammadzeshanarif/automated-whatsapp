"""This is automated WhatsApp controller, It controls all the process."""
import numbers
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from reader import Reader
from chrome_web_driver import ChromeWebDriver


original_message = Reader.get_whatsapp_message()
receivers_info = Reader.get_receivers_info()
receivers_count = len(receivers_info)

driver = ChromeWebDriver()
driver.load_whatsapp()

print('Sending to {} numbers... '.format(receivers_count))
count = 1

successful_receivers = []
failed_receivers = []
for index, receiver_info in enumerate(receivers_info): # 03334497842,Muhammad Zeshan Arif, 5B
    name = receiver_info[0]
    number = receiver_info[1]
    if not number:
        continue
    print('{count}: {number}'.format(count=count, number=number))
    user_message = original_message.format(name=name)
    if driver.send(number, user_message):
        successful_receivers.append(receiver_info)
    else:
        failed_receivers.append(receiver_info)

    count = count + 1


print('*' * 100)
print('Final Report')
print('-' * 100)
print('Successful message count {} / {}'.format(len(successful_receivers), receivers_count))
print('Failed message count {} / {}'.format(len(failed_receivers), receivers_count))
print('-' * 100)
print('Successfully sent on following numbers')
print('-' * 100)
print(successful_receivers)
print('-' * 100)
print('Failed to send on following numbers')
print('-' * 100)
print(failed_receivers)
print('*' * 100)