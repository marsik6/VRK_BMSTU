from flask import Flask, render_template, request
import tensorflow as tf

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('start.html')

def pr_prediction(params):
    model = tf.keras.models.load_model('models')
    pred = model.predict([params])
    return pred

@app.route('/pr/', methods=['POST', 'GET'])
def pr_predict():
    message = ''
    if request.method == 'POST':
        param_list = ('mn', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'y_my', 'x8', 'x9', 'x10', 'x11')
        params = []
        for i in param_list:
            param = request.form.get(i)
            params.append(param)
        params = [float(i.replace(',', '.')) for i in params]

        message = f'Спрогнозированное значение Прочности при растяжении для введенных параметров: {pr_prediction(params)} МПа'
    return render_template('main.html', message=message)


if __name__ == '__main__':
    app.run()