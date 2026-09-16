import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, render_template, request, Response
import json
from google import genai

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)

SYSTEM_PROMPT = """
You are a senior venture capitalist and market research analyst.
Analyze the user's business idea and produce an exhaustive, professional breakdown covering:
1. Executive Summary & Value Proposition
2. Target Market Demographics & Customer Personas
3. Market Size & Opportunity (TAM, SAM, SOM concepts)
4. Competitor Landscape & Moat (Unfair Advantage)
5. Revenue Models & Monetization Strategies
6. Operational Challenges, Regulatory Risks, & Mitigation Plan
7. Recommended Go-To-Market (GTM) Strategy for Launch

Format your response cleanly in standard Markdown using bolding and clear lists.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze_idea():
    data = request.get_json() or {}
    user_idea = data.get("idea", "").strip()

    if not user_idea:
        payload = json.dumps({"error": "Please enter a business idea."})
        return Response(payload.encode("utf-8"), status=400, mimetype="application/json; charset=utf-8")

    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            payload = json.dumps({"error": "GEMINI_API_KEY is not configured."})
            return Response(payload.encode("utf-8"), status=500, mimetype="application/json; charset=utf-8")

        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{SYSTEM_PROMPT}\n\nUser Idea: {user_idea}"
        )
        
        # Return plain text directly encoded in UTF-8 bytes
        payload = json.dumps({"result": response.text})
        return Response(payload.encode("utf-8"), status=200, mimetype="application/json; charset=utf-8")
        
    except Exception as e:
        payload = json.dumps({"error": str(e)})
        return Response(payload.encode("utf-8"), status=500, mimetype="application/json; charset=utf-8")

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(debug=False, host="0.0.0.0", port=port)
