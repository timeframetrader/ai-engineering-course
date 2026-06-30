import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()  # reads .env file and sets environment variables
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def _call(system_prompt, user_prompt):
    """Make a single Gemini call and return the raw response text."""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            response_mime_type="application/json",
        ),
        contents=user_prompt,
    )
    return response.text


def generate_tweets(text):
    """Turn a piece of content into 3 ready-to-post tweets."""
    raw = _call(
        system_prompt=(
            "You are a social media expert. "
            "Return a JSON array of exactly 3 tweet strings. "
            "Each tweet must be under 280 characters."
        ),
        user_prompt="Turn this into 3 tweets:\n\n" + text,
    )
    return json.loads(raw)


def generate_summary(text):
    """Summarise a piece of content into one short paragraph."""
    raw = _call(
        system_prompt=(
            "You are an expert summariser. "
            "Return a JSON object with a single key called 'summary'. "
            "The value should be one clear paragraph (2-4 sentences)."
        ),
        user_prompt="Summarise this content:\n\n" + text,
    )
    return json.loads(raw)["summary"]


def generate_image_prompts(text):
    """Generate 3 image prompts that could illustrate a piece of content."""
    raw = _call(
        system_prompt=(
            "You are a creative director who writes prompts for AI image generators. "
            "Return a JSON array of exactly 3 image prompt strings. "
            "Each prompt should be vivid, specific, and 1-2 sentences long."
        ),
        user_prompt="Write 3 image prompts to illustrate this content:\n\n" + text,
    )
    return json.loads(raw)


if __name__ == "__main__":
    sample = (
        "I am learning AI engineering. Today I built a content pipeline "
        "that takes long articles and turns them into tweets, summaries, "
        "and image generation prompts -- all automatically using an LLM."
    )

    print("=== TWEETS ===")
    for tweet in generate_tweets(sample):
        print("-", tweet)

    print("\n=== SUMMARY ===")
    print(generate_summary(sample))

    print("\n=== IMAGE PROMPTS ===")
    for prompt in generate_image_prompts(sample):
        print("-", prompt)
