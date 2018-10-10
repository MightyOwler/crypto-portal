# Copy to auth.py
# This sample data should be enough to test the parts of the site
# which do not require a database connection

dbase = 'psola'
dbuser = 'username'
dbpass = 'password'
dbhost = 'localhost'

timestamp_public = "cert.pem"
timestamp_private = "key.pem"

# For Python 3, gitkey must be bytes
gitkey = b'github-secret'
sesskey = 'session-secret'
debug = True
