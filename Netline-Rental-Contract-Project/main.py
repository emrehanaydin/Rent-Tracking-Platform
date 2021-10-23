from flask import Flask, render_template, request, jsonify
from helpers import Helper

app = Flask(__name__)
helper = Helper()


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/register')
def about():
    return render_template('register.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')

    if helper.user_login_control(email=email, password=password):
        return render_template('home.html')

    return render_template('login.html')


@app.route('/add_user', methods=['POST'])
def add_user():
    helper.add_user_save(data=request.form)

    return render_template('login.html')


@app.route('/tenant', methods=['POST'])
def tenant():
    helper.save_tenant(data=request.form)

    return render_template('home.html')


@app.route('/rent_info', methods=['POST'])
def rent_info():
    helper.rent_info_save(data=request.form)

    return render_template('home.html')


@app.route('/taxes', methods=['POST'])
def taxes():
    helper.taxes_save(data=request.form)

    return render_template('home.html')


@app.route('/insurance_information', methods=['POST'])
def insurance_information():
    helper.insurance_information_save(data=request.form)

    return render_template('home.html')


@app.route('/dues_information', methods=['POST'])
def dues_information():
    helper.dues_inset_save(data=request.form)
    return render_template('home.html')


@app.route('/exit')
def exit():
    return render_template('login.html')


@app.route('/get-tenants')
def get_tenants():
    tenants = helper.get_tenants()
    return render_template("home.html", tenants=tenants)


@app.route('/get-rents')
def get_rents():
    rents = helper.get_rents()
    render_template("home.html", rents=rents)


@app.route('/get-taxes')
def get_taxes():
    taxes = helper.get_taxes()
    render_template("home.html", taxes=taxes)


@app.route('/get-insurance')
def get_insurance():
    insurance = helper.get_insurance()
    render_template("home.html", insurance=insurance)


@app.route('/get-dues')
def get_dues():
    dues = helper.get_dues()
    render_template("home.html", dues=dues)



if __name__ == "__main__":
    app.run(debug=True)
