from flask import Flask, render_template_string
from datetime import datetime
import os
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get the top command output
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    # Format the server time to IST
    ist_time = datetime.now().astimezone().replace(tzinfo=None) + timedelta(hours=5, minutes=30)
    
    # Create HTML output
    html_content = f'''
    <html>
        <body>
            <h1>System Information</h1>
            <p>Name: Your Full Name</p>
            <p>Username: {os.getlogin()}</p>
            <p>Server Time in IST: {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</p>
            <h2>Top Output:</h2>
            <pre>{top_output}</pre>
        </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
