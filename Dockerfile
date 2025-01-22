# Use Python 3.11 for better performance
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies and clean up in same layer
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    pkg-config \
    libssl-dev \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    # Install Solana CLI in same layer
    && sh -c "$(curl -sSfL https://release.solana.com/v1.17.0/install)" \
    && echo 'export PATH="/root/.local/share/solana/install/active_release/bin:$PATH"' >> ~/.bashrc

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    SOLANA_NETWORK="devnet" \
    PATH="/root/.local/share/solana/install/active_release/bin:$PATH"

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy and install application
COPY . .
RUN pip install -e .

# Create non-root user for security
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Expose port for API
EXPOSE 8000

# Configure healthcheck
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Create volume for persistent data
VOLUME ["/app/data"]

# Default to running tests, but can be overridden
CMD ["pytest", "-v", "--cov=memetix"]
