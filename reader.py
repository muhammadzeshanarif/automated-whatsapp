"""This reads message and number from a file"""
class Reader(object):

    @staticmethod
    def get_whatsapp_message():
        message_file = open('message.txt', 'r')
        message = message_file.read()
        message_file.close()
        return message

    @staticmethod
    def get_receivers_info():
        receivers_info = []
        f = open('numbers.txt', 'r')
        for line in f.read().splitlines():
            if line != '':
                receiver_info = line.split(',')
                receivers_info.append(receiver_info)
        f.close()

        return receivers_info
