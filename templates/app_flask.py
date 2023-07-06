from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# To render Homepage template
@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('./index.html')

# For calling the Postman API
@app.route('/via_postman', methods=['POST'])
def calculator():
    if(request.method == 'POST'):
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        
        if(operation=='add'):
            output = num1 + num2
            result= 'The sum of '+str(num1)+' and '+str(num2) + ' is '+str(output)        
        
        if(operation=='substract'):
            output = num1 - num2
            result= 'The difference of '+str(num1)+' and '+str(num2) + ' is '+str(output)            
        
        if(operation=='multiply'):
            output = num1 * num2
            result= 'The product of '+str(num1)+' and '+str(num2) + ' is '+str(output)            
        
        if(operation=='divide'):
            output = num1 / num2
            result= 'The quotient when '+str(num1)+' is divided by '+str(num2) + ' is '+str(output)
            
        return jsonify(result)
    
    
if __name__ == '__main__':
    app.run(debug=True)