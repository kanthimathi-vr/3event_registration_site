from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)
EVENT_FILE = 'events.json'

def load_events():
    try:
        with open(EVENT_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route('/')
def index():
    events = load_events()
    return render_template('index.html', events=events)

@app.route('/event/<int:event_id>', methods=['GET', 'POST'])
def event(event_id):
    events = load_events()
    event = next((e for e in events if e['id'] == event_id), None)
    if not event:
        return "Event not found", 404

    if request.method == 'POST':
        # Registration logic here — you can store or email registration
        return redirect(url_for('event', event_id=event_id, registered='yes'))

    registered = request.args.get('registered') == 'yes'
    return render_template('event.html', event=event, registered=registered)

if __name__ == '__main__':
    app.run(debug=True)
