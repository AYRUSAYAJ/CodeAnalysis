from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Route to receive code input, save it, and redirect to display output
@app.route('/analyze', methods=['POST'])
def analyze():
    # Get code input from the form
    code_input = request.form.get('code_input')

    # For demonstration purposes, let's pretend we analyzed the code and got a dictionary output
    # Replace this with the actual analysis using the LLM model
    analysis_output = {
        'code_complexity': {
            'Function A': 8,
            'Function B': 5,
            'Function C': 10,
            'Function D': 7
        },
        'code_duplication': {
            'File 1': 3,
            'File 2': 2,
            'File 3': 4,
            'File 4': 1
        },
        'issues': ['Syntax error', 'Performance issue', 'Security vulnerability'],
        'improvements': ['Refactor function A', 'Optimize database query']
    }

    # Convert the dictionary to a JSON string
    analysis_output_str = json.dumps(analysis_output)

    # Redirect to the output page with the analysis output as a URL parameter
    return redirect(url_for('display_output', analysis_output=analysis_output_str))

# Route to display the output page
@app.route('/display_output')
def display_output():
    # Get analysis output from the URL parameter
    analysis_output_str = request.args.get('analysis_output')

    # Convert the JSON string back to a dictionary
    analysis_output = json.loads(analysis_output_str)

    # Render the output template with the analysis output
    return render_template('output.html', analysis_output=analysis_output)

if __name__ == '__main__':
    app.run(debug=True)
