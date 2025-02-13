FROM python:3.9

# Set working directory inside container
WORKDIR /app

COPY src/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy application files
COPY src /app

# Expose port
EXPOSE 5000

# Run application
CMD ["python", "app.py"]