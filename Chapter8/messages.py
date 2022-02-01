from message_activity import *
#from message_activity import show_messages, send_messages
#import message_activity as ma
#from message_activity import show_messages as shm, send_messages as sem
#import message_activity

sent_messages = []
messages = ['abc','def','ghi']

show_messages(messages)
print('sent_messages', sent_messages)
print('messages', messages)

sent_messages = send_messages(messages)
print('sent_messages', sent_messages)
print('messages', messages)
'''
ma.show_messages(messages)
print('sent_messages', sent_messages)
print('messages', messages)

ma.sent_messages = send_messages(messages)
print('sent_messages', sent_messages)
print('messages', messages)
'''