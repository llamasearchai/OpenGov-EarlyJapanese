# Multi-stage Docker build for OpenGov-EarlyJapanese
# Author: Nik Jois <nikjois@llamasearch.ai>

# Stage 1: Builder
FROM python:3.11-slim as builder

LABEL maintainer="Nik Jois <nikjois@llamasearch.ai>"
LABEL description="AI-powered comprehensive Japanese language learning platform"
LABEL version="0.1.0"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        build-essential \
        git && \
    rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Set working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml ./
COPY README.md ./

# Copy source code
COPY opengov_earlyjapanese ./opengov_earlyjapanese

# Install dependencies
RUN /root/.cargo/bin/uv sync --frozen

# Stage 2: Runtime
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/app/.venv/bin:$PATH"

# Install runtime dependencies only
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl && \
    rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd -r appuser && \
    useradd -r -g appuser -u 1000 -m -s /bin/bash appuser

# Set working directory
WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder --chown=appuser:appuser /app/.venv /app/.venv
COPY --from=builder --chown=appuser:appuser /app/opengov_earlyjapanese /app/opengov_earlyjapanese

# Copy configuration and data
COPY --chown=appuser:appuser configs ./configs
COPY --chown=appuser:appuser data ./data

# Create directories for runtime data
RUN mkdir -p /app/media /app/models && \
    chown -R appuser:appuser /app/media /app/models

# Switch to non-root user
USER appuser

# Expose ports
EXPOSE 8000 8501

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Default command (FastAPI server)
CMD ["uvicorn", "opengov_earlyjapanese.api.main:app", "--host", "0.0.0.0", "--port", "8000"]

