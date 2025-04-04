from flask import Flask, render_template, request, send_file
import matplotlib.pyplot as plt
import io
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot', methods=['GET', 'POST'])
def plot():
    if request.method == 'POST':
        data = request.form.get('data')
        try:
            data_list = [float(x.strip()) for x in data.split(' ')]
        except Exception:
            data_list = []
        plt.figure()
        plt.plot(data_list, marker='o', linestyle='-')
        plt.title("Простой график")
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        return send_file(img, mimetype='image/png')
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)