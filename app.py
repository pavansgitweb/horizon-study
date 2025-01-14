import requests
from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    # Target website URL
    base_url = "https://horizon3.framer.website"
    
    # Construct the full URL by appending the requested path
    target_url = f"{base_url}/{path}"
    
    # Fetch the source code of the target website
    response = requests.get(target_url)
    
    if response.status_code == 200:
        # Get the HTML content
        html_content = response.text

        # Inject the <style> with `!important` to override the display setting
        style_override = """
        <style>
            #__framer-badge-container {
                display: none !important;
            }
            .framer-bMdha .framer-1y8ghoz {
            --framer-paragraph-spacing: 20px !important;
            }
            .framer-image.framer-text {
                margin-inline: auto !important;
            }
            ul.framer-text, ol.framer-text {
                margin-top: auto !important;
            }
            p.framer-text:not(:first-child), div.framer-text:not(:first-child), h1.framer-text:not(:first-child), h2.framer-text:not(:first-child), h3.framer-text:not(:first-child), h4.framer-text:not(:first-child), h5.framer-text:not(:first-child), h6.framer-text:not(:first-child), ol.framer-text:not(:first-child), ul.framer-text:not(:first-child), blockquote.framer-text:not(:first-child), .framer-image.framer-text:not(:first-child)
            {
                margin-top: auto !important;
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
        return f"Failed to fetch the website. Status code: {response.status_code}, Contact - pavansh555@gmail.com or @pavan._.hegde on insta", response.status_code

if __name__ == '__main__':
    app.run(debug=True)
