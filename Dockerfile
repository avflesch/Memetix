# Use Python 3.9 as base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies including Solana CLI tools
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    pkg-config \
    libssl-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Solana CLI
RUN sh -c "$(curl -sSfL https://release.solana.com/v1.17.0/install)"
ENV PATH="/root/.local/share/solana/install/active_release/bin:$PATH"

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Install any additional project dependencies
RUN pip install -e .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
ENV SOLANA_NETWORK="devnet"

# Expose port if needed (e.g., for API)
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Create volume for persistent data
VOLUME ["/app/data"]

# Command to run tests
CMD ["pytest", "-v", "--cov=memesphere"]

# Alternative command to run the application
# CMD ["python", "-m", "memesphere.main"]
