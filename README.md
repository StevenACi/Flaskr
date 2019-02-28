# Flaskker

A test restful app that can run on a local network , with a single admin authentication.
In the future we can implement support for image files, etc.




creating the database or to reset:
CLI From project root:
flask initdb


General Notes for using Flask:

@app.route('/htmlpagename',methods=['GET','POST']) can specifiy functions
for specific pages. Any def prefaced by this will auto run as the client
requests the page.


installing and booting:

pip install -e .

set FLASK_APP=main.py <<--your main py script
set FLASK_DEBUG=1 <--- only set in testing!!!
flask run
