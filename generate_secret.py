#first thought
# the below case of assignig dosent work because it will manually 
# creates the key when we run, but we wnant it to generate when a ction is
# initiated by the client

import secrets
secret = secrets.token_urlsafe(32)
print("Generated Secret key :", secret)

# but this below case will actully a not a good menthod becasue , ideally secrets should be generated
# on every import ot application start.
#so, geneating a key once, and storing it safely  and reusing it isbest.
# because if the methos generates a new secret everytime we restart application then previous codes will be invalid 
# and we should import everytime

#import secrets
#def get_secret_key():
#    return secrets.token_urlsafe(32)

#secret = get_secret_key