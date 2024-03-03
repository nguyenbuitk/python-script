from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name:
        return 'Hello, {}!'.format(name)
    else:
        return 'Hello, stranger'

if __name__ == '__main__':
    app.run(debug=True)

# Trong ví dụ này, khi bạn truy cập vào URL http://localhost:5000/hello?name=John, Flask sẽ nhận thấy tham số name được gửi đi và sử dụng request.args.get('name') để lấy giá trị của tham số này (trong trường hợp này là 'John') và trả về "Hello, John!".