from openai import OpenAI
import os
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class AIService:
    def generate_flashcards(self, skill_name: str, subdomain_name: str, count: int = 5):
        prompt = f"""
You are a learning assistant.

Generate {count} high-quality flashcards for learning.

Skill: {skill_name}
Subdomain: {subdomain_name}

Return ONLY valid JSON in this format:

[
  {{
    "front": "...",
    "back": "..."
  }}
]

No explanation. No markdown. Only JSON.
"""
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You generate structured flashcards."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
        )

        content = response.choices[0].message.content

        return json.loads(content)
