class Message():
    def __init__(self, from_number, time_arrived, text_of_SMS):
        self.has_been_viewed = False
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text_of_SMS = text_of_SMS
        
    def __str__(self):
        return f'({self.from_number}, {self.time_arrived}, {self.text_of_SMS})'

class SMS_store():
    def __init__(self):
        self.storage = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.storage.append(Message(from_number, time_arrived, text_of_SMS))
    
    def message_count(self):
        return len(self.storage)

    def get_unread_indexes(self):
        return [self.storage.index(idx) for idx in self.storage if idx.has_been_viewed == False]
        pass

    def get_message(self, idx):
        self.storage[idx].has_been_viewed = True
        return self.storage[idx]
        pass

    def delete(self, idx):
        del(self.storage[idx])
        pass

    def clear(self):
        self.storage.clear()
        pass



import time
def menu(inbox):
    try:
        print("""
    1. See message
    2. Delete message
    3. Clear all storage
    4. Exit program
            """)
        num = int(input("Choose the number to continue: "))
        if num == 1:
            print(inbox.get_message(idx = int(input("Choose the index want to read: "))))
        elif num == 2:
            idx = int(input("Choose the index want to delete: "))
            inbox.delete(idx)
            print(f'Message index {idx} deleted')
        elif num == 3:
            check = input('Are you sure to clear all storage?(Enter yes or y) ')
            if check in ('y','Y','yes','Yes','YES'):
                inbox.clear()
        elif num == 4:
            return 'Done'
        any = input("Press Enter to proceed...")

    except IndexError as e:
        print('That index is not in storage. try other index')
        any = input("Press Enter to proceed...")

if __name__ == '__main__':
    my_inbox = SMS_store()
    my_inbox.add_new_arrival('010-6314-5112',time.ctime(time.time()), 'Hello')
    my_inbox.add_new_arrival('010-6314-5112',time.ctime(time.time()), 'Are you there?')
    my_inbox.add_new_arrival('010-6314-5112',time.ctime(time.time()), 'Answer to me!!!')
    my_inbox.add_new_arrival('010-6314-5112',time.ctime(time.time()), 'Sorry, really sorry')
    my_inbox.add_new_arrival('010-4832-8912',time.ctime(time.time()), "Hi, I'm Kim. nice to see you")

    while(True):
        print("\nMessages inbox: ", my_inbox.message_count())
        print("Unread Messages: ", my_inbox.get_unread_indexes())
        if menu(my_inbox) == 'Done':
            break
