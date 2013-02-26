''' serve.py
simple twilio responder
'''
from flask import Flask, request, abort, render_template

app = Flask(__name__)
app.config.from_envvar('LAUREL_SETTINGS')


@app.route('/api/1/voice/incoming', methods=['POST'])
def api_v1_incoming_voice():
    ''' twilio will post data here when a call is received
    we respond to fresh calls with a welcome message and instructions
    post requests also come here after digits are pressed
    the system will respond to digits with an mp3
    '''
    # make sure the post request originated from Twilio
    if request.form['AccountSid'] != app.config['TWILIO']['account_sid']:
        abort(403)

    # collect digits entered on the keypad, if any
    digits = request.form.get('Digits', None)

    if not digits:
        # this is a brand new call into the system
        return render_template('welcome.xml')
    
    # digits were pressed - find the relevant mp3
    points = app.config['POINTS']
    if digits not in points.keys():
        # requested point not found
        return render_template('point_not_found.xml')

    # valid submission
    mp3 = app.config['POINTS'][digits]
    return render_template('point.xml', mp3=mp3)


if __name__ == '__main__':
    app.run(
        host = app.config['HOST']
        , port = int(app.config['PORT'])
    )
