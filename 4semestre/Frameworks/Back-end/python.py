from flask import Flask, request

app= Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    numero = request.args.get('numero')
    numero2 = request.args.get('numero2')
    return  f'numero 1 :, {numero}. e numero 2 : {numero2}.'

if __name__ == '__main__':
    app.run(debug=True)