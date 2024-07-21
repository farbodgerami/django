import random
import string
import base64
import hashlib

code_verifier = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(43, 128)))
 
code_verifier = base64.urlsafe_b64encode(code_verifier.encode('utf-8'))
print('lllllllllllll',str(code_verifier)) #b'SDg4WDdCVktITkhBWVlYQVpPU0VIUFZMVklIWU5GQjZWVzJSWllGREVEMkMxNUM='
code_challenge = hashlib.sha256(code_verifier).digest()
code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8').replace('=', '')
print(code_challenge) #Sjmudg2Fbn-9rILnSuabETRkn2yAksU9K55jjKCT7LI
 
# http://127.0.0.1:8000/o/authorize/?response_type=code&code_challenge=dEVlXvdp55KeO-XLnSv9URwwpvBRBIv9zrM2JU5KhXw&code_challenge_method=S256&client_id=r7Y6BmuF74Mhrf9UKaBtzMostcFDKLXIXOct2CnL&redirect_uri=http://127.0.0.1:8000/noexist/callback
