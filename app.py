from db_init import create_db
from functions import delete_data, get_all_rows_from_table, insert_data, modify_data
import os 
from flask import Flask,render_template, request, redirect, url_for
import forms



def create_app(name):
    app = Flask(__name__)

    @app.route('/')
    def index():
        form = forms.LoginForm()
        return render_template('index.html',form=form)

    @app.route('/submitted',methods=['GET','POST'])
    def submitted():
        form=request.form
        if request.method == 'POST':
            print(form)
            name = form["name"]
            phone = form['phone']
            email = form['email']
            job = form['job']

            # insert data into database
            insert_data(name, phone, email, job)

        return render_template('submitted.html')

    @app.route('/database')
    def view_database():
        rows = get_all_rows_from_table()
        
        return render_template('entire_database.html', rows=rows)

    @app.route('/delete<the_id>',methods=['POST'])
    def delete(the_id):
        if request.method == 'POST':
            # if the checkbox was selected (for deleting entire row)
            delete_data(the_id)
        return redirect(url_for('view_database'))

    @app.route('/modify<the_id>/<modified_category>',methods=['GET','POST'])
    def modify_database(the_id ,modified_category):
        form=request.form
        if request.method == 'POST':
            # Get data from the form on database page
            user_input = form[modified_category]
            # modify the row from the database
            modify_data(the_id, modified_category, user_input)
            # redirect back to the database page
            return redirect(url_for('view_database'))
        return redirect(url_for('index'))


    return app






def launch( db='info.db', create=False):
    if create:
        create_db(db)
    os.environ['DATABASE_FILENAME'] = db
    app = create_app(__name__)
    app.secret_key = 'secret'
    app.run(host='0.0.0.0', port=5000)

# start the app
if __name__ == '__main__':
    launch()