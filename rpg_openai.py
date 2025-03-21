# for extra credit, OpenAI API has been used to generate stories

import openai
import os

openai.api_key = "Key would go here, but removed for commit and push"


def generate_rpg_story():
    client = openai.OpenAI(api_key=openai.api_key)

    prompt = """Prompt: Print simple text for a story. Use pipe | between the node number, the description of the path, and between the path number options at the end.
    
Be sure there is at least one space surrounding the left and right of every pipe |, including the ones between the last 2 numbers.

Example for one line: 1 | You wake up in a dark cave. Do you: 1) Explore deeper 2) Look for an exit | 2 | 3

The story must have at least 10 decision points or lines, and no more than 15.
Each line should be up to 178 characters.

Each decision point must be its own line in the text file, including only two option paths.
The options should be more than one word and be an action.

Be sure to include least one shared child node (where multiple paths lead to the same event).
Do not structure each line with ascending child node numbers, somewhat randomize it.

Clear choices at each event (e.g., “1) Open the door 2) Walk away”).

A minimum tree depth of 5 levels. Ensure the minimum number of nodes from the root to any leaf is at least 3.

Ensure each event has a unique event number.

If the story ends, do not provide options for the user as the story is over.
If an event is a final outcome and the story ends, be sure to include -1 for both left and right nodes (like " | -1 | -1")

The story should be engaging, with a clear sense of progression, suspense, and meaningful choices.

Avoid mythical themes. The story should be more realistic with some comical oddities. Consider a time travel theme.

Consider using oddly relatable but mild millennial and gen z humor, and comedic, abrupt endings with niche detail.

Do not write any apostrophes like '.

Only use alphanumeric english characters."""

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