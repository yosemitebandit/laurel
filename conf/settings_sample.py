''' config file for the laurel app
copy this somewhere safe and set an env var:
    $ export LAUREL_SETTINGS=/path/to/settings/file
'''

DEBUG = False

HOST = '0.0.0.0'
PORT = 5005

TWILIO = {
    'account_sid': 'ACabc123'
}

POINTS = {
    '1': 'https://s3.amazonaws.com/example/diner.mp3'
    , '2': 'https://s3.amazonaws.com/example/theater.mp3'
}
