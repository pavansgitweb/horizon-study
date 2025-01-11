from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # Read the large HTML file
    with open("templates/index.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    
    # Inject the <style> to hide the Framer badge
    style_injection = """
    <style>
        #__framer-badge-container {
            display: none !important;
        }
    </style>
    """
    # Insert the style into the <head> section
    modified_html = html_content.replace("<head>", f"<head>{style_injection}", 1) 

    # Serve the modified HTML
    response = make_response(modified_html)
    response.mimetype = "text/html"
    return response

if __name__ == '__main__':
    app.run(debug=True)
