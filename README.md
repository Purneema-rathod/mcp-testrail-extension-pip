# 🧩 TestRail Extension for Goose

This extension connects **Goose** with **TestRail**, allowing Goose to fetch test runs, test results, and statuses directly from your TestRail instance — eliminating manual updates and streamlining QA automation.

---

## ⚙️ 1. Prerequisites

### 🪟 Windows
- **Python** ≥ 3.12.2 (recommended)  
  👉 [Download here](https://www.python.org/downloads/)
- **uv** (lightweight Python package manager)  
  ```bash
  pip install uv
  ```
- **Git** installed and added to PATH  
  👉 [Download Git](https://git-scm.com/downloads)

### 🍎 macOS
- **Python** ≥ 3.12.2 (via [pyenv](https://github.com/pyenv/pyenv) or [Homebrew](https://brew.sh))  
  ```bash
  brew install python@3.12
  ```
- **uv** installed globally  
  ```bash
  pip install uv
  ```
- **Full Disk Access for Goose**  
  *(System Settings → Privacy & Security → Full Disk Access → enable Terminal/Goose)*

---

## 📦 2. Setup Instructions

1. **Extract the ZIP**  
   Unzip `mcp-testrail-final-26thMay2025.zip` into a preferred location, e.g.:
   ```
   /Users/<username>/Downloads/mcp-testrail-final-26thMay2025/
   ```

2. **Create the Virtual Environment**  
   In Terminal (or Command Prompt), navigate into the extracted folder and run:
   ```bash
   uv sync
   ```
   This installs all required dependencies and creates a `.venv` environment compatible with Goose.

3. **Set TestRail Credentials (no manual `.env` file needed)**  
   Run this command in the same directory:

   ```bash
   echo -e "TESTRAIL_URL=https://afterpay.testrail.io\nTESTRAIL_USER=your-email@example.com\nTESTRAIL_API_KEY=your-api-key" > .env
   ```

   ✅ This automatically creates a `.env` file with your TestRail credentials.

---

## 🦢 3. Enable the Extension in Goose

Open **Goose → Settings → Extensions → Add New**, then fill out the following fields:

| **Field** | **Value** |
|------------|-----------|
| **Name** | Testrail |
| **Description** | Testrail tools |
| **Type** | StandardIO |
| **Command** | `uv run /full/path/to/.venv/bin/<folder-name>` |

---

### 💻 Example (macOS)
```bash
uv run /Users/purneema/Downloads/mcp-testrail-final-26thMay2025/.venv/bin/mcp-testrail-final-26thMay2025
```

### 🪟 Example (Windows)
```bash
uv run C:\Users\<YourName>\Downloads\mcp-testrail-final-26thMay2025\.venv\Scripts\mcp-testrail-final-26thMay2025.exe
```

> ⚠️ Make sure the path matches the extracted folder name and location on your system.

---

## ✅ 4. Verify Installation

Once enabled, restart Goose.  
You can test your setup by running this inside Goose:

```
/testrail get_test_runs
```

If configured correctly, you’ll see a list of TestRail runs retrieved from your instance.

---

## 🧠 Notes

- Keep the `.venv` folder in the same directory as the extension.  
- Use your **actual TestRail URL** (e.g., `https://afterpay.testrail.io`).  
- If Goose can’t detect the extension, check for typos in your **Command** path.  
- Re-run `uv sync` if you update dependencies or Python version.

---

## 👩‍💻 Author

**Purneema Suresh Rathod**  
Quality Engineering | Block
