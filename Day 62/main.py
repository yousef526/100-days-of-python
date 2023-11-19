from wsgiref.validate import validator
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

coffee_rate = ['☕','☕☕','☕☕☕','☕☕☕☕','☕☕☕☕☕']
wifi_rate = ['✘','💪','💪💪','💪💪💪','💪💪💪💪','💪💪💪💪💪']
power_rate = ['✘','🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌🔌']

ATTRIBUTES = ['cafe','Location','Open','Close','Coffee','Wifi','Power']


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    Location = StringField('Location', validators=[
        DataRequired(),
        validators.URL("Please enter loaction on google map"),
        ])
    Open = StringField('Open eg.8AM', validators=[DataRequired()])
    Close = StringField('Close eg.5PM', validators=[DataRequired()])

    Coffee = SelectField(label='Coffee rating', validators=[DataRequired()],choices=coffee_rate)
    Wifi = SelectField('Wifi rating', validators=[DataRequired()],choices=wifi_rate)
    Power = SelectField('Power rating', validators=[DataRequired()],choices=power_rate)
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=["POST","GET"])
def add_cafe():
    form = CafeForm()
    values = ""
    if form.validate_on_submit():
        for att in ATTRIBUTES:
            values+=((eval(f'form.{att}.data'))+',')
        with open('cafe-data.csv',encoding='utf8' ,newline='',mode='a') as csv_file:
            csv_file.write('\n'+values)
            
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv',encoding='utf8' ,newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
