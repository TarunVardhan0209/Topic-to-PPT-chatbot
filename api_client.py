import os
import requests
from dotenv import load_dotenv
import re
import json

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
print("DEBUG: Loaded API Key =", API_KEY)

def clean_json_response(text):
    # Remove markdown code fences if present
    text = re.sub(r"```json|```", "", text).strip()

    # Try to load as JSON to confirm it's valid
    try:
        json.loads(text)
        return text
    except json.JSONDecodeError as e:
        print("DEBUG: JSON decoding failed:", e)
        raise ValueError("❌ Response is not valid JSON")

def get_ppt_json(topic):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
Create a PowerPoint presentation on '{topic}' with 7 to 9 slides.
Return only JSON like:
[
  {{"title": "Slide 1 Title", "content": "Bullet 1\\nBullet 2\\nBullet 3"}},
  ...
]
No explanation. Only the JSON array.
"""

    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    raw_text = response.json()["choices"][0]["message"]["content"]
    print("DEBUG: Raw API response:", raw_text[:200])  # Optional: print a preview

    return clean_json_response(raw_text)
