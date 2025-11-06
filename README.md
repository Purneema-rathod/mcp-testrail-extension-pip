🧰 Prerequisites
Python 3.12+

pip and virtualenv (optional: pyenv)

No VPN (for package installs)



💻 MAC / Linux Setup
1. Unzip the project 

Run this in terminal:
cd <path to where the zipfile is unzipped>

Example:cd Downloads (if the file is present in and unzipped in downloads folder)

cd mcp-testrail-tool-pip-fixed


2. Create and activate virtual environment

python3 -m venv .venv

source .venv/bin/activate

3. Install dependencies

pip install .


🪟 Windows Setup
1. Unzip the folder manually or:
Use File Explorer or PowerShel to unzip the file:
Expand-Archive .\mcp-testrail-tool-pip-fixed.zip -DestinationPath .\mcp-testrail-tool-pip-fixed 

cd .\mcp-testrail-tool-pip-fixed

2. Create and activate virtualenv

python -m venv .venv

.venv\Scripts\activate

3. Install with pip

pip install .


🔐 Create .env File (Same for Mac & Windows)
In the root of the unzipped folder:

TESTRAIL_URL=https://afterpay.testrail.io
TESTRAIL_USER=you@example.com
TESTRAIL_API_KEY=your-api-key




🧠 Enable in Goose
Go to Settings → Extensions → Add


Use these fields:

**Field -        Value**
Name -         Testrail
Description -  Testrail tools
Type -          StandardIO



Command
Full path to: .venv/bin/mcp-testrail-tool (or .venv\\Scripts\\... on Windows)

Example (Mac):

/Users/username/mcp-testrail-tool-pip-fixed/.venv/bin/mcp-testrail-tool

Example (Windows):

C:\Users\username\Downloads\mcp-testrail-tool-pip-fixed\.venv\Scripts\mcp-testrail-tool.exe





