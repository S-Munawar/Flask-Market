from app import app # Importing the app variable from the app package

# main
if __name__ == "__main__": # True when the script is run directly or else __name__ is set to the name of the module
    app.run(host='0.0.0.0', port=5000, debug=True) # Running the Flask application in debug mode that detect the changes in the code and restart the server automatically without needing to restart the server manually.
