import _md5
from _hashlib import new

from pip._vendor.distlib.compat import raw_input

counter = 1

#getting hash here
pass_in = raw_input("please enter the md5 has :")

#getting password hash list
pwfile = raw_input("please enter the password file name : ")

try:

    pwfile = open(pwfile , "r")

except:
    print("\n File not found")
    quit()

#trying db for each possible password
for password in pwfile:
    filemd5 = _md5.new(new(password.strip()).hexdigest())
    print("Trying password number %d %s " % (counter, password.strip()))

    counter += 1

    if pass_in == filemd5:
        print("\n hash found. \n password is : %s" % password)
        break
else:
    print("\npassword not found")