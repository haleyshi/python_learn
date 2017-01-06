from base64 import encodestring, decodestring

str = 'username:password'
b64str = encodestring(str)
print 'BEGIN'
print str
print b64str
print b64str[:-1]  # Remove the last char CRLF
print decodestring(b64str)

longstr = 'llllllllllllllllllllllllllloooooooooooooooooooooooooooooooooooooooooooooonnnnnnnnnnnnnnnnnnnnnngggggggggggggggggstring'
print encodestring(longstr)  ## MAX to 76 chars + CRLF for each line

print 'END'