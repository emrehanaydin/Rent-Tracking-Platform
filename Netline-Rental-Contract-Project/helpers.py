import os
import mysql.connector
import json
import datetime


class _JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        return json.JSONEncoder.default(obj)


class Helper:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="34.140.74.86",
            user="root",
            password="300718cc",
            db="data",
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def user_login_control(self, email, password):
        self.cursor.execute("SELECT * FROM `users` WHERE email=%s and password=%s", (email, password))
        users = self.cursor.fetchall()

        return len(users) > 0

    def save_tenant(self, data):
        name_surname = data.get('name_surname')
        TC_or_taxes = data.get('TC')
        phone = data.get('phone')
        email = data.get('email')
        address = data.get('address')
        address2 = data.get('address2')
        bank_account_no = data.get('bank_account_no')
        iban_no = data.get('iban_no')
        contract_date = data.get('contract_date')
        contract_start_date = data.get('contract_start_date')

        self.cursor.execute(
            "INSERT INTO `tenant_info`(name_surname, TC_or_taxes, phone, address, address2, email, bank_account_no, iban_no, contract_date, contract_start_date) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",

            (name_surname, TC_or_taxes, phone, address, address2, email, bank_account_no, iban_no,
             contract_date,
             contract_start_date))
        self.conn.commit()

    def get_tenants(self):
        self.cursor.execute("SELECT * FROM tenant_info ORDER BY created_date DESC")
        result = self.cursor.fetchall()
        return json.dumps(result, cls=_JSONEncoder)

    def get_rents(self):
        self.cursor.execute("SELECT * FROM rent_info ORDER BY created_date DESC")
        result = self.cursor.fetchall()
        return json.dumps(result, cls=_JSONEncoder)

    def get_taxes(self):
        self.cursor.execute("SELECT * FROM taxes ORDER BY created_date DESC")
        result = self.cursor.fetchall()
        return json.dumps(result, cls=_JSONEncoder)

    def get_insurance(self):
        self.cursor.execute("SELECT * FROM insurance_information ORDER BY created_date DESC")
        result = self.cursor.fetchall()
        return json.dumps(result, cls=_JSONEncoder)

    def get_dues(self):
        self.cursor.execute("SELECT * FROM dues_common_expenses ORDER BY created_date DESC")
        result = self.cursor.fetchall()
        return json.dumps(result, cls=_JSONEncoder)

    def add_user_save(self, data):
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        self.cursor.execute(
            "INSERT INTO `users` values (%s,%s,%s)",
            (name, email, password))
        self.conn.commit()

    def rent_info_save(self, data):
        rent_unit = data.get('rent_unit')  # kira birimi
        rent_price = data.get('rent_price')  # kira tutarı
        rent_date = data.get('rent_date')  # kira ödeme tarihi
        rent_payment_period = data.get('rent_payment_date')  # kira ödeme periyodu
        down_payment_unit = data.get('down_payment_unit')  # peşinat ödeme birimi
        advance_payment = data.get('advance_payment')  # peşinat tuturı
        deposit_unit = data.get('deposit_unit')  # depozit birimi
        deposit_price = data.get('deposit_price')  # depozit tutarı
        rent_increase = data.get('rent_increase')  # kira artışı olacak mı ?
        first_increase_period = data.get('first_increase_period')  # ilk artış dönem Tarihi
        rent_increase_period_date = data.get('rent_increase_period_date')  # Kira Artış Periyodu
        rent_increase_rate = data.get('rent_increase_rate')  # Kira artış oranı

        self.cursor.execute("INSERT INTO `rent_info` values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",

                            (rent_unit, rent_price, rent_date, rent_payment_period, down_payment_unit, advance_payment,
                             deposit_unit, deposit_price, rent_increase, first_increase_period,
                             rent_increase_period_date, rent_increase_rate
                             ))
        self.conn.commit()

    def taxes_save(self, data):
        residence_or_workplace = data.get('residence_or_workplace')  # konut ya da işyeri
        property_tax_price = data.get('property_tax_price')  # emlak vergisi tutarı
        property_tax_history = data.get('property_tax_history')  # emlak vergisi tatrihi
        garbage_tax_price = data.get('garbage_tax_price')  # çöp vergisi tutarı
        garbage_tax_history = data.get('garbage_tax_history')  # çöp vergisi tarihi
        property_tax_payment_period = data.get('property_tax_payment_period')
        garbage_tax_payment_period = data.get('garbage_tax_payment_period')

        self.cursor.execute("INSERT INTO `taxes` values (%s,%s,%s,%s,%s,%s,%s) ",

                            (residence_or_workplace, property_tax_price, property_tax_history, garbage_tax_price,
                             garbage_tax_history, property_tax_payment_period, garbage_tax_payment_period
                             ))
        self.conn.commit()

    def insurance_information_save(self, data):
        dask_company_name = data.get('dask_company_name')
        dask_price = data.get('dask_price')
        dask_company_iban_number = data.get('dask_company_iban_number')
        dask_payment_date = data.get('dask_payment_date')
        dask_last_date = data.get('dask_last_date')
        policy = data.get('policy')
        policy_price = data.get('policy_price')
        policy_company_account_number = data.get('policy_company_account_number')
        policy_company_iban_number = data.get('policy_company_iban_number')
        policy_payment_date = data.get('policy_payment_date')
        fire_policy = data.get('fire_policy')
        fire_policy_price = data.get('fire_policy_price')
        fire_policy_company_account_no = data.get('fire_policy_company_account_no')
        fire_policy_company_iban_no = data.get('fire_policy_company_iban_no')
        fire_policy_payment_date = data.get('fire_policy_payment_date')

        self.cursor.execute(
            "INSERT INTO `insurance_information`(dask_company_name,dask_price,dask_company_iban_number,dask_payment_date,dask_last_date,policy,policy_price,policy_company_account_number,policy_company_iban_number,policy_payment_date,fire_policy,fire_policy_price,fire_policy_company_account_no,fire_policy_company_iban_no,fire_policy_payment_date)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",

            (dask_company_name, dask_price, dask_company_iban_number,
             dask_payment_date, dask_last_date, policy, policy_price, policy_company_account_number,
             policy_company_iban_number, policy_payment_date, fire_policy, fire_policy_price,
             fire_policy_company_account_no, fire_policy_company_iban_no, fire_policy_payment_date
             ))

        self.conn.commit()

    def dues_inset_save(self, data):
        dues = data.get('dues')
        dues_price = data.get('dues_price')
        dues_account_no = data.get('dues_account_no')
        dues_iban_no = data.get('dues_iban_no')
        dues_payment_date = data.get('dues_payment_date')
        common_expenditure = data.get('common_expenditure')
        common_expenditure_contract_no = data.get('common_expenditure_contract_no')
        common_expenditure_description = data.get('common_expenditure_description')
        common_expenditure_key = data.get('common_expenditure_key')
        common_expenditure_payment_date = data.get('common_expenditure_payment_date')

        self.cursor.execute("INSERT INTO `dues_common_expenses` values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ",

                            (dues, dues_price, dues_account_no, dues_iban_no, dues_payment_date, common_expenditure,
                             common_expenditure_contract_no, common_expenditure_description, common_expenditure_key,
                             common_expenditure_payment_date
                             ))
        self.conn.commit()
