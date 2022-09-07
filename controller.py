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

print('Sending to {} numbers... '.format(numbers_count))
count = 1

successful_numbers = []
failed_numbers = []
for number in numbers:
    if not number:
        continue
    print('{count}: {number}'.format(count=count, number=number))
    if driver.send(number, original_message):
        successful_numbers.append(number)
    else:
        failed_numbers.append(number)

    count = count + 1


print('*' * 100)
print('Final Report')
print('-' * 100)
print('Successful message count {} / {}'.format(len(successful_numbers), numbers_count))
print('Failed message count {} / {}'.format(len(failed_numbers), numbers_count))
print('-' * 100)
print('Successfully sent on following numbers')
print('-' * 100)
print(successful_numbers)
print('-' * 100)
print('Failed to send on following numbers')
print('-' * 100)
print(failed_numbers)
print('*' * 100)