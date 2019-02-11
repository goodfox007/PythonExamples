from flask import Flask, json, request
#from Simplifai1_Extractor2 import A

app = Flask(__name__)

@app.route('/simplifai_dataextractor1/', methods = ['POST'])
def determine_escalation():
    result=""
    #a = A()
    #jsondata = request.get_json()
    data=request.args.get('data1')
    #data = json.load(jsondata)
    print(data)
    #stuff happens here that involves data to obtain a result
    #result=result+" Phone : "+a.extract_phone_numbers(data)
    #result=result+"Email Address : "+a.extract_email_addresses(data)
    result=result+"ATLEAST SOMETHING CAME!"+" And U sent : "+data
    
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)



