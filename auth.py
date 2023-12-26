```python
import os
import binascii
from datetime import datetime, timedelta

# Dictionary to store auth codes and their expiry times
auth_codes = {}

def generate_auth_code(user_id):
    """
    Generate a unique authentication code for a user.
    The code is valid for 1 hour.
    """
    auth_code = binascii.hexlify(os.urandom(24)).decode()
    expiry_time = datetime.now() + timedelta(hours=1)
    auth_codes[auth_code] = {'user_id': user_id, 'expiry_time': expiry_time}
    return auth_code

def validate_auth_code(auth_code):
    """
    Validate an authentication code.
    If the code is valid and has not expired, return True.
    Otherwise, return False.
    """
    if auth_code in auth_codes:
        if datetime.now() < auth_codes[auth_code]['expiry_time']:
            return True
    return False
```
