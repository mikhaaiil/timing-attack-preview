from flask import Flask, request
import time
from gevent import monkey
from gevent.pywsgi import WSGIServer

monkey.patch_all()

app = Flask(__name__)
SECRET_TOKEN = 'supersecret123'

def vulnerable_compare(a: str, b: str) -> bool:
    min_len = min(len(a), len(b))
    for i in range(min_len):
        if a[i] != b[i]:
            return False
        time.sleep(0.01)
    return len(a) == len(b)


@app.route('/check')
def check_token():
    token = request.args.get('token', '')
    start_compare = time.perf_counter()
    result = vulnerable_compare(token, SECRET_TOKEN)
    compare_time = (time.perf_counter() - start_compare) * 1000
    if result:
        return f"Access granted!", 200
    else:
        return f"Access denied!", 403


if __name__ == '__main__':
    print('runs on http://localhost:5000')
    print(f'token: {SECRET_TOKEN}')
    http_server = WSGIServer(('127.0.0.1', 5000), app)
    http_server.serve_forever()