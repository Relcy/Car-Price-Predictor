import flask
import pickle

import pandas as pd

with open(f'LinearRegressionModel.pk1', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('main.html'))

    if flask.request.method == 'POST':
        company = flask.request.form['company']
        name = flask.request.form['name']
        year = flask.request.form['year']
        fuel_type = flask.request.form['fuel_type']
        km_driven = flask.request.form['km_driven']

        input_variables = pd.DataFrame([[company, name, year, fuel_type, km_driven]],
                                       columns=['company', 'name', 'year', 'fuel_type', 'km_driven'], dtype=object)
        predicition = model.predict(input_variables)[0]
        return flask.render_template('main.html', original_input=
        {'Company': company,
         'Name': name,
         'Year': year,
         'Fuel_Type': fuel_type,
         'Km_Driven': km_driven},
                                     result=predicition, )


if __name__ == '__main__':
    app.run()
