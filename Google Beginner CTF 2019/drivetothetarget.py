import re, requests, time

# Final target coordinates:
# 51.4921, -0.1929
# CTF{Who_is_Tardis_Ormandy}

DELTA = 0.001
lat = 51.49141
lon = -0.194
token = 'gAAAAABfArR9G40_ysxDxbFiuQHdUbpCYlTtdpS09n8uCNSDy9nUDHN5RQfS_UyBHdDn6kGzRLuik-3uuCLgHzthO1Osu107nj042Ofx5v6ZWz-JIhdRhe8g_eQYVVQX5Qzh-EGJqMYV'

foundLat = True
foundLon = False

def send_request():
    ploads = {'lat': lat, 'lon': lon, 'token': token}
    print(ploads)
    return requests.get('https://drivetothetarget.web.ctfcompetition.com/', params=ploads)

# Move to the right latitude
while not foundLat:
    recieve = send_request()
    text = recieve.text
    # print(text)
    token_loc = re.search('name="token" value=".*">', text)
    if token_loc:
        token = token_loc.group(0)[20:-2]
    speed_loc = re.search(' \d*km/h', text)
    if speed_loc: print('Speed:{}'.format(speed_loc.group(0)))
    if 'You are getting away' in text:
        print('Verdict: Away')
        print('FOUND {} {} {}'.format(lat, lon, token))
        foundLat = True
        break
    elif 'You are getting closer' in text:
        print('Verdict: Closer')
        lat -= DELTA
    elif 'this is too fast!' in text:
        print('Verdict: Too fast')
    else:
        print('Verdict: ???')
        print(text)
        lat -= DELTA
        input()
    lat = round(lat * 100000) / 100000
    time.sleep(3.8)

# Move to the right longitude
while not foundLon:
    recieve = send_request()
    text = recieve.text
    # print(text)
    token_loc = re.search('name="token" value=".*">', text)
    if token_loc:
        token = token_loc.group(0)[20:-2]
    speed_loc = re.search(' \d*km/h', text)
    if speed_loc: print('Speed:{}'.format(speed_loc.group(0)))
    if 'You are getting away' in text:
        print('Verdict: Away')
        print('FOUND {} {} {}'.format(lat, lon, token))
        foundLon = True
        break
    elif 'You are getting closer' in text:
        print('Verdict: Closer')
        lon -= DELTA
    elif 'this is too fast!' in text:
        print('Verdict: Too fast')
    else:
        print('Verdict: ???')
        print(text)
        lon -= DELTA
        input()
    lon = round(lon * 100000) / 100000
    time.sleep(4.75)