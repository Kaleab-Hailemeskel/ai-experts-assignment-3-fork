# 🐍 Python Project: App & Test Suite

This project contains a Python application with a complete automated test suite using `pytest` and `pytest-cov`.

## 📁 Project Structure

- `app/`: Source code and business logic.
    
- `test/`: Unit and integration tests.
    
- `Dockerfile`: Container configuration for isolated testing.
    
- `requirements.txt`: Project dependencies (Requests, Dateutil, Pytest).
    

---

## 📥 Cloning and Setup

Before running tests, clone the repository to your local machine and navigate into the project root:



```Bash
# Clone the repository
git clone https://github.com/Kaleab-Hailemeskel/ai-experts-assignment-3-fork.git

# Enter the project directory
cd ai-experts-assignment-3-fork
```
## 🚀 Getting Started

### 1. Local Development

Use this method if you have Python 3.11+ installed and want to run tests quickly during development.

**Set up your environment:**



```Bash
# Create a virtual environment
python -m venv .venv

# Activate it
# On Windows: .venv\Scripts\activate
# On macOS/Linux: source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
**Run tests:**

Bash

```
# Run all tests
pytest

# Run tests with in a verbose 
pytest test/ -v

# Run tests with print command for custome debugging
pytest test/ -s
```
---

### 2. Docker Execution (Recommended)

Use this method to ensure your tests run in an environment identical to production, regardless of your local OS.

**Build the image:**

```Bash
docker build -t python-test-runner .
```

**Run the tests:**

```Bash
# The container will automatically run pytest and then remove itself (--rm)
docker run --rm python-test-runner
```

---

## 🧪 Testing Details

The test suite is configured to:

1. **Validate Logic:** Ensure functions in `app/` behave as expected.
    
2. **Check API Interactions:** Tests using the `requests` library.
    
3. **Date Parsing:** Validating ISO strings via `python-dateutil`.
    
4. **Enforce Coverage:** Aims for high code coverage visibility via `pytest-cov`.
    

---

## 🛠 Troubleshooting
- **Permission Denied (Docker):** If you get a "permission denied" error when trying to connect to the Docker daemon, you likely need `root` privileges. Use `sudo`:

```Bash
sudo docker build -t python-test-runner .
sudo docker run --rm python-test-runner
```

- **ModuleNotFoundError:** If running locally without a venv, ensure your `PYTHONPATH` includes the root directory: `export PYTHONPATH=$PYTHONPATH:.`
    
- **Docker Build Fail:** Ensure you are in the root directory (where the `Dockerfile` is located) when running the build command.
