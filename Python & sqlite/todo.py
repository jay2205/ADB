import sqlite3
from bottle import route, run, template

@route('/todo')
@route('/todo/<status:int>')
def todo_list(status =1):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    if (status >= 0):
        c.execute("SELECT id, task FROM todo WHERE status LIKE '"+str(status)+"'" )
    else:
        c.execute("SELECT id, task FROM todo")
    result = c.fetchall()
    output = template('make_table', rows=result)
    return output

run()
