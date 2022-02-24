"""This reads message and number from a file"""
class Reader(object):

    @staticmethod
    def get_whatsapp_message():
        message_file = open('message.txt', 'r')
        message = message_file.read()
        message_file.close()
        return message

    @staticmethod
    def get_whatsapp_numbers():
        numbers = []
        f = open('numbers.txt', 'r')
        for line in f.read().splitlines():
            if line != '':
                numbers.append(line)
        f.close()

        return numbers
