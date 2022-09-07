from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
from sys import platform


BASE_URL = 'https://web.whatsapp.com'
SEND_MESSAGE_URL = BASE_URL + '/send?phone={number}&text={message}'
RETRY_LIMIT = 1
DELAY = 30

ERROR_MESSAGE = 'There is something wrong, Please check WhatsApp is connected and loaded properly.'
FAILED_MESSAGE = 'Failed to send message to {number}'

options = Options()
if platform == 'win32':
	options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

class ChromeWebDriver(object):
    """Chrome web driver"""

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def load_whatsapp(self):
        self.driver.get(BASE_URL)
        input('Please login to your WhatsApp and press Enter to continue.')

    def send(self, number, message, is_message_quoted=False):
        """Send WhatsApp message and retry """
        quoted_message = message if is_message_quoted else quote(message)
        try:
            for i in range(RETRY_LIMIT):
                url = SEND_MESSAGE_URL.format(number=number, message=quoted_message)
                self.driver.get(url)
                try:
                    send_button = WebDriverWait(self.driver, DELAY).until(
                        EC.element_to_be_clickable((By.CLASS_NAME , 'epia9gcq'))
                    )
                except Exception as exc:
                    retry_count = i + 1
                    print(ERROR_MESSAGE)
                    print(FAILED_MESSAGE.format(number=number))
                    print('Retrying {retry_count}/{retry_limit}'.format(retry_count=retry_count, retry_limit=RETRY_LIMIT))
                    print(str(exc))
                else:
                    sleep(2)
                    send_button.click()
                    sleep(4)
                    return True
        except Exception as exc:
            print(FAILED_MESSAGE.format(number=number))
            print(str(exc))

        return False
