from flask import Flask, request, jsonify, render_template, redirect, url_for
import app_logic

app = Flask(__name__)

summary = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global summary
    if request.method == 'POST':
        input_text = request.form.get('input')
        max_length = int(request.form.get('max_length', 130))
        min_length = int(request.form.get('min_length', 30))

        if input_text:
            response = app_logic.query({
                "inputs": input_text
            }, max_length=max_length, min_length=min_length)
            summary = response[0]  # assuming the response is a list
        return redirect(url_for('summary_view'))

    return render_template('index.html')

@app.route('/summary', methods=['GET'])
def summary_view():
    global summary
    return render_template('summary.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)