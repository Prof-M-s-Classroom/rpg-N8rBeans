import openai
import os

openai.api_key = "Paste your OPENAI key here"


def generate_rpg_story():
    client = openai.OpenAI(api_key=openai.api_key)

    prompt = """Prompt: Create a story.txt file in the following format:

The story must have at least 8 unique decision points.

Each decision point must be its own line in the text file.

At least one shared child node (where multiple paths lead to the same event).

Clear choices at each event (e.g., “1) Open the door 2) Walk away”).

A minimum tree depth of 5 levels.

Use -1 for left/right if an event is a final outcome (leaf node).

Ensure each event has a unique event number.

The story should be engaging, with a clear sense of progression, suspense, and meaningful choices."""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI that generates structured RPG stories."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def save_story_to_file(filename, story_text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(story_text)


if __name__ == "__main__":
    story_text = generate_rpg_story()
    save_story_to_file("story.txt", story_text)