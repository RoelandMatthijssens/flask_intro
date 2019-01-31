from flask_intro import app

@app.route('/lists')
def list_lists():
    return "lists"
