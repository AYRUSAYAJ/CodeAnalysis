from flask import Flask, render_template, request, redirect, url_for
import json
from langchain_community.llms import Ollama
ollama = Ollama(model="llama3")

def analyze_code(user_code):
    """metrics = {}
    for key, value in prompts.items():
        prompt = value + user_code
        #convert prompt to string
        prompt = str(prompt)
        formatted_response = ollama.invoke(prompt)
        metrics[key] = formatted_response"""
    """prompt = ""
    i = 1
    for key, value in prompts.items():
        prompt = f"i" + ". " + value + "\n"
        i += 1"""
    prompt = "1 : Calculate the complexity of the code,2: Determine the code coverage of the code,3: Identify code duplication in the code,4: Find all the issues in the code" + "Code : " + user_code + "Give the respone in the same format 1. 2. 3. 4. only give text based crisp and short answers for the given 4 prompts\n Give it in dictionary format in python. only generate {} part, no other sentances. Do not use any markdown. the output should be in python format"
    formatted_response = ollama.invoke(prompt)
    #print(prompt) 
    return formatted_response

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
    
    analysis_output = analyze_code(code_input)
    formatted_response = analysis_output

    # Find the start and end index of the dictionary part
    start_index = formatted_response.find("{")
    end_index = formatted_response.find("}")

    # Extract the dictionary part from the formatted_response
    data_str = formatted_response[start_index + 1:end_index]

    # Split the dictionary into individual key-value pairs
    pairs = data_str.split("\n")

    # Create an empty dictionary to store the key-value pairs
    result = {}

# Iterate over each key-value pair and add them to the dictionary
    for pair in pairs:
        key, value = pair.split(": ", 1)
        result[int(key)] = value.strip('"')

    # Convert the dictionary to a JSON string
    analysis_output_str = json.dumps(result)

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
