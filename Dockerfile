# 1. Use a Python base image
FROM python:3.11-slim

# 2. Set the working directory
WORKDIR /app

# 3. Copy requirements first (optimization for faster builds)
COPY requirements.txt .

# 4. Install pytest and pytest-cov
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the 'app' and 'tests' folders into the image
# This "ships" your entire project structure
COPY app/ ./app/
COPY tests/ ./tests/

# 6. Set Python path so 'pytest' can find your 'app' module
ENV PYTHONPATH=/app

# 7. The command to run when the container starts
# We include --cov=app to see that coverage report immediately
CMD ["pytest", "tests/", "-v"]