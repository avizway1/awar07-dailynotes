# -------------------------------------------------------
# Stage: Base image
# -------------------------------------------------------
FROM python:3.11-slim

# Metadata labels (good practice)
LABEL maintainer="Aviz Academy"
LABEL description="Docker build test app"

# -------------------------------------------------------
# Set working directory inside container
# -------------------------------------------------------
WORKDIR /app

# -------------------------------------------------------
# Copy and install dependencies FIRST
# (Docker layer cache optimization — only re-runs if
#  requirements.txt changes, not every code change)
# -------------------------------------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# -------------------------------------------------------
# Copy application code
# -------------------------------------------------------
COPY app.py .

# -------------------------------------------------------
# Environment variables with defaults
# (Can be overridden at runtime with -e or --env-file)
# -------------------------------------------------------
ENV APP_ENV=production
ENV APP_PORT=8080
ENV APP_NAME="Aviz Docker Test App"

# -------------------------------------------------------
# Expose the port (documentation only — doesn't publish)
# -------------------------------------------------------
EXPOSE 8080

# -------------------------------------------------------
# Health check — Docker will call this every 30s
# -------------------------------------------------------
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

# -------------------------------------------------------
# ENTRYPOINT = always run python
# CMD        = default args (overridable at docker run)
# -------------------------------------------------------
ENTRYPOINT ["python"]
CMD ["app.py"]
