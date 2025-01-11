import requests
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch the source code of the target website
    url = "https://horizon3.framer.website/"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Get the HTML content
        html_content = response.text

        # Inject the <style> with `!important` to override the display setting
        style_override = """
        <style>
            #__framer-badge-container {
                display: none !important;
            }
        </style>
        """
        # Insert the style into the <head> section
        modified_html = html_content.replace("<head>", f"<head>{style_override}", 1)

        # Serve the modified HTML
        flask_response = make_response(modified_html)
        flask_response.mimetype = "text/html"
        return flask_response
    else:
        # Handle errors if the website couldn't be fetched
        return f"Failed to fetch the website. Status code: {response.status_code}"
 
if __name__ == '__main__':
    app.run(debug=True)
