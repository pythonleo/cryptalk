from bottle import route, run


@route('/')
def index():
    return open("current.txt", encoding="utf-8", newline='').read()

run(host='0.0.0.0', port=80)
