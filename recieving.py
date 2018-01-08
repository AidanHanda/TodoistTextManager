import poplib
import email
import os

import time
import todoist

#Todoist Setup
api = todoist.TodoistAPI()
user = api.user.login(os.environ['TODOIST_EMAIL'], os.environ['TODOIST_PASSWORD'])


def getNewMail():
    '''
    Grabs new texted mail from gmail!
    :return:
    '''
    pop_conn = poplib.POP3_SSL('pop.gmail.com')
    pop_conn.user(os.environ['EMAIL_USERNAME'])
    pop_conn.pass_(os.environ['EMAIL_PASSWORD'])
    #Get messages from server:
    messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
    # Concat message pieces:
    messages = [b"\n".join(mssg[1]) for mssg in messages]
    #Parse message intom an email object:
    messages =  [email.message_from_bytes(mssg)  for mssg in messages]
    newMessages = [mess.get_payload().replace("'",'').split('-----Original Message-----')[0].strip() for mess in messages if mess['From'] == '6303634860@txt.att.net'] #Some pretty insane lexing
    pop_conn.quit()
    return newMessages

def addTask(entry):
    '''
    Adds a task to todoist
    :param entry: The content of the task to be added
    :return:
    '''
    api.add_item(entry)

for i in getNewMail():
    addTask(i)