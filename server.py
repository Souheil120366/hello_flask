from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.errorhandler(404) 
def handle_error(error):
    # response.status_code = error.status_code
    res="<script>alert('Sorry! No response. Try again.')</script>"
    return res

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def success():
  return "Dojo!"

@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hi(name):
    if name.strip().isdigit():
        res="<script>alert('Please enter a string value!')</script>"
    else:
        res=f"Hi {name.capitalize()}!"
            
    return res
    

@app.route('/repeat/<times>/<text>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def repeat_text(text,times):
    if text.strip().isdigit():
        res="<script>alert('Please enter a string value!')</script>"
    else:
        if times.strip().isdigit():
            res=""
            res+= f"<p><b>{text}</b></p>"
            res= int(times)*res
        else:
            res="<script>alert('Please enter a number times value!')</script>"
    
    
    return res


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

