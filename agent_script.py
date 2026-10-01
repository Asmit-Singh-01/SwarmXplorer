import os, glob, json, time, random
from google import genai

# 1. Gather all existing polyglot files in SwarmXplorer
repo_files = glob.glob('**/*.py', recursive=True) + glob.glob('**/*.cpp', recursive=True) + glob.glob('**/*.js', recursive=True) + glob.glob('**/*.rs', recursive=True)

# Read file content snippets for context
context = ''
for fname in repo_files[:10]:
    try:
        with open(fname, 'r') as f:
            context += f'--- File: {fname} ---\n' + f.read()[:600] + '\n\n'
    except Exception:
        pass

client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])

# 2. Decide action: Modify existing file OR Create new module
target_file = random.choice(repo_files) if repo_files and random.random() > 0.5 else None

if target_file:
    prompt_task = f"Refactor and enhance the existing file '{target_file}' to add new features, optimize algorithms, or fix potential bugs without breaking architecture."
else:
    prompt_task = "Create a new production-ready polyglot module, simulation component, or algorithm (in Python, C++, JS Web visualizer, or Rust mesh network)."

prompt = f"""
You are a Senior Polyglot Systems Architect for SwarmXplorer: A Hardware-Agnostic Decentralized Swarm Intelligence Framework.
Current repo context:
{context}

Task: {prompt_task}

Provide output strictly as valid JSON only:
{{
  "filepath": "{target_file if target_file else 'relative path like algos/dynamic_nav.py or web/visualizer.js'}",
  "code": "full runnable production code with inline docstrings",
  "commit_message": "feat(swarm): clear conventional commit message"
}}
"""

response = None
for attempt in range(3):
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        break
    except Exception as e:
        print(f"Attempt {attempt+1} failed due to server load: {e}")
        time.sleep(5)

if not response:
    print("Google servers busy. Exiting cleanly.")
    exit(0)

text = response.text.strip()
if text.startswith('```json'):
    text = text[7:-3].strip()
elif text.startswith('```'):
    text = text[3:-3].strip()

data = json.loads(text)

# Ensure parent folder exists & write/update file
os.makedirs(os.path.dirname(data['filepath']), exist_ok=True)
with open(data['filepath'], 'w') as f:
    f.write(data['code'])

with open('commit_msg.txt', 'w') as f:
    f.write(data['commit_message'])
