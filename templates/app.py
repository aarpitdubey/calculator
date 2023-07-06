from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# To render Homepage
@app.route('/', methods=['GET', 'POST']) 
def homepage():
    return render_template('index.html')

@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method=='POST'):
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2 = int(request.form['num2'])
        
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
         
        return render_template('results.html',result=result)

@app.route('/via_postman', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if (request.method=='POST'):
        operation=request.json['operation']
        num1=int(request.json['num1'])
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
         
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)