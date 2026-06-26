from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    
    notes = ""
    summary = ""

    if request.method == "POST":
        notes = request.form["notes"]
        summary = "TEST WORKS"
        response = requests.post(
            "http://localhost:1234/api/v1/chat",
            headers={
                "Content-Type": "application/json"
            },
            json={
                "model": "gemma-1.1-2b-it",
                "input": f"Summarize these notes:{notes}\n\n",
                "context_length": 8000
            }
        )

        
        answer = response.json()
        summary = answer["output"][0]["content"]

    if len(notes) > 2500:
        summary = "Error: Maximum 2500 characters allowed."

    return render_template(
        "index.html",
        notes=notes,
        summary=summary,
        lenghtofnotes=len(notes)
    )


if __name__ == "__main__":
    app.run(debug=True)
