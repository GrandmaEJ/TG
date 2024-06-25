from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate(problem):
    try:
        # host/api/math=12+13 or anything 
        #but link এ / সাপোর্ট করে না , তাই রিপ্লেস করে কাজ করতে হবে 
        problem = problem.replace('x', '*').replace('÷', '/')
        result = eval(problem)
        
        # এখন রেজাল্ট পাঠাবো   json আকারে 
        
        return {
            "status" : 200,
            "results" : result,
            "anything" : " your name or anything"
            }
            
    except:
        return { "status" :400 }
            
        
        




@app.route('/api/math=<problem>', methods=['GET'])
def math(problem):
    result = calculate(problem)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)