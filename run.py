from kyvue.app import app

if __name__ == "__main__":
    # Run the Flask application with debug mode enabled
    app.run(host="0.0.0.0", port=5000, debug=True)
