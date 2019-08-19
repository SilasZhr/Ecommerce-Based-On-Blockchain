from flask import Flask,render_template, request
import os
app = Flask(__name__)

@app.route('/',methods=['post','GET'])
def hello_world():
    flag = request.values.get('flag')
    #address = request.args.get('address')
    if flag == '1':
        result = os.popen(" java -jar blockchain-java-jar-with-dependencies.jar  createwallet").read()
    elif flag == '2':
        result = os.popen(" java -jar blockchain-java-jar-with-dependencies.jar  printaddresses").read()
    elif flag == '3':
        address = request.args.get('address')
        result = os.popen((" java -jar blockchain-java-jar-with-dependencies.jar  getbalance -address  %s")%(address)).read()
    elif flag == '4':
        address = request.args.get('address') 
        result = os.popen((" java -jar blockchain-java-jar-with-dependencies.jar  createblockchain -address %s")%(address)).read()
    elif flag == '5':
        result = os.popen(" java -jar blockchain-java-jar-with-dependencies.jar  printchain").read()
    elif flag == '6':
        source = request.args.get('from')
        target = request.args.get('to')
        amount = request.args.get('amount')
        result = os.popen((" java -jar blockchain-java-jar-with-dependencies.jar send -from %s -to %s -amount %s")%(source,target,amount)).read()
    return result

if __name__ == '__main__':
    app.run()
