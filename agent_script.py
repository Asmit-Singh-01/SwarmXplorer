import os, glob, json, time
from google import genai

# 1. Read existing code context across languages
repo_files = glob.glob('**/*.py', recursive=True) + glob.glob('**/*.cpp', recursive=True) + glob.glob('**/*.rs', recursive=True) + glob.glob('**/*.js', recursive=True) + glob.glob('**/*.md', recursive=True)
context = ''
for fname in repo_files[:10]:
    try:
        with open(fname, 'r') as f:
            context += f'--- File: {fname} ---\n' + f.read()[:600] + '\n\n'
    except Exception:
        pass

client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])

# Polyglot Prompt Injection
prompt = f"""
You are a Polyglot Systems Architect for SwarmXplorer: A Hardware-Agnostic Decentralized Swarm Intelligence Framework.
Do not restrict to Python. Output production code in Python, C++ (ROS2/hardware), Web Dashboard (JS/HTML/CSS), or Rust (Mesh Network) depending on the needs of a decentralized swarm intelligence framework.

Current repo context:
{context}

Task: Identify a missing production component and generate code.
Output strictly valid JSON only with keys:
{{
  "filepath": "relative path like web/dashboard.js or cpp/mesh_node.cpp or algos/p2p_sync.py",
  "code": "full runnable production code with detailed comments",
  "commit_message": "feat(core): brief conventional commit message"
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
    print("Google servers busy. Skipping safely.")
    exit(0)

text = response.text.strip()
if text.startswith('```json'):
    text = text[7:-3].strip()
elif text.startswith('```'):
    text = text[3:-3].strip()

data = json.loads(text)

# Directory check & write file
os.makedirs(os.path.dirname(data['filepath']), exist_ok=True)
with open(data['filepath'], 'w') as f:
    f.write(data['code'])

with open('commit_msg.txt', 'w') as f:
    f.write(data['commit_message'])
