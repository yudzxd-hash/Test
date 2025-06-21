from flask import Flask, render_template, request, jsonify

   app = Flask(__chataa__)

   # Store messages in memory for simplicity (not recommended for production)
   messages = []

   @app.route('/')
   def index():
       return render_template('index.html', messages=messages)

   @app.route('/send_message', methods=['POST'])
   def send_message():
       username = request.form.get('username')
       message = request.form.get('message')
       if username and message:
           messages.append({'username': username, 'message': message})
       return jsonify({'status': 'OK'})

   if __name__ == '__main__':
       app.run(debug=True)