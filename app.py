from flask import Flask, render_template,jsonify                #to create the Flask application.
import subprocess                                               #to run external commands (like executing a Python script).

app= Flask(__name__, static_folder='static')                    #to help Flask determine the root path of the application.

@app.route("/")                                                 # define a route for the root URL(homepage) ("/").
def index():
    return render_template("index.html")

@app.route("/run_script")
def run_script():
    try:
        # Use subprocess.check_output to capture the script output
        script_output = subprocess.check_output(["python", "C:\\Users\\shrey\\OneDrive\\Desktop\\projects\\alexa\\main.py"], text=True)
        # Split the output into a list of responses
        responses = script_output.strip().split('\n')
        return jsonify({"responses": responses})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Error executing script: {e}"})


if __name__ == "__main__":
    app.run(debug=True)

