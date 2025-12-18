# ---- builder stage: install deps into a clean target dir ----
FROM python:3.12-slim AS builder

WORKDIR /build

# Prevents Python from writing .pyc, and ensures logs are unbuffered
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --prefix=/install -r requirements.txt


# ---- runtime stage: minimal image, non-root user ----
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

# Create a non-root user
RUN useradd --create-home --shell /usr/sbin/nologin appuser

# Copy deps from builder
COPY --from=builder /install /usr/local

# Copy app code
COPY app ./app

USER appuser

EXPOSE 8000

# Healthcheck (Docker-level)
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health').read()" || exit 1

# Run
CMD ["python", "-m", "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8000"]
