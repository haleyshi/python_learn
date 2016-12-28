# -*- coding: UTF-8 -*-

from poplib import POP3_SSL

pop3server = POP3_SSL('pop-mail.outlook.com', 995)
pop3server.user('me@hotmail.com')
pop3server.pass_('secret')
rsp, msg, size = pop3server.retr(pop3server.stat()[0])   ## Get the 1st message

#print msg
sep = msg.index('')
recvBody = msg[sep+1:]  ## Strip header
print recvBody
