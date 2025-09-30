# OpenGov-EarlyJapanese Deployment Guide

**Version**: 0.2.0  
**Author**: Nik Jois <nikjois@users.noreply.github.com>  
**Repository**: https://github.com/llamasearchai/OpenGov-EarlyJapanese  
**Status**: Production Ready

## Deployment Summary

OpenGov-EarlyJapanese has been successfully prepared for production deployment with:

### Infrastructure Components

#### 1. GitHub Repository
- **URL**: https://github.com/llamasearchai/OpenGov-EarlyJapanese
- **Branch**: main
- **Tags**: v0.1.0
- **Status**: Public repository with professional commit history

#### 2. GitHub Actions CI/CD
- **Workflows**:
  - `.github/workflows/ci.yml` - Continuous Integration
  - `.github/workflows/publish.yml` - PyPI Publishing

- **CI Pipeline Features**:
  - Multi-OS testing (Ubuntu, macOS, Windows)
  - Python version matrix (3.9, 3.10, 3.11, 3.12)
  - Code quality checks (Ruff, Black, isort, MyPy)
  - Security scanning (Bandit, Safety)
  - Test coverage reporting to Codecov
  - Docker image building and publishing
  - Automatic PyPI publishing on release

#### 3. Docker Configuration
- **Dockerfile**: Multi-stage build with security best practices
  - Builder stage for dependency installation
  - Runtime stage with minimal footprint
  - Non-root user (appuser) for security
  - Health check endpoint
  - Optimized layer caching

- **docker-compose.yml**: Complete local development stack
  - API service on port 8000
  - UI service on port 8501
  - PostgreSQL database on port 5432
  - Redis cache on port 6379
  - Persistent volumes for data
  - Health checks for all services

#### 4. Package Distribution
- **PyPI Package**: `opengov-earlyjapanese`
- **Installation**: `pip install opengov-earlyjapanese`
- **CLI Entry Point**: `nihongo`

## Production Deployment Steps

### Option 1: Docker Deployment (Recommended)

```bash
# Clone repository
git clone https://github.com/llamasearchai/OpenGov-EarlyJapanese.git
cd OpenGov-EarlyJapanese

# Build Docker image
docker build -t llamasearchai/opengov-earlyjapanese:latest .

# Run with docker-compose
docker-compose up -d

# Access services
# API: http://localhost:8000
# UI: http://localhost:8501
# Docs: http://localhost:8000/docs
```

### Option 2: Kubernetes Deployment

```yaml
# Example Kubernetes deployment (kubernetes/deployment.yaml)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: opengov-earlyjapanese
spec:
  replicas: 3
  selector:
    matchLabels:
      app: opengov-earlyjapanese
  template:
    metadata:
      labels:
        app: opengov-earlyjapanese
    spec:
      containers:
      - name: api
        image: llamasearchai/opengov-earlyjapanese:latest
        ports:
        - containerPort: 8000
        env:
        - name: API_HOST
          value: "0.0.0.0"
        - name: LOG_LEVEL
          value: "INFO"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 3
          periodSeconds: 5
```

### Option 3: PyPI Installation

```bash
# Install from PyPI (when published)
pip install opengov-earlyjapanese

# Run CLI
nihongo --help

# Run API server
uvicorn opengov_earlyjapanese.api.main:app --host 0.0.0.0 --port 8000

# Run UI
streamlit run opengov_earlyjapanese/ui/app.py
```

## GitHub Secrets Configuration

For automated deployments, configure these secrets in GitHub repository settings:

### Required Secrets
- `DOCKER_USERNAME` - Docker Hub username
- `DOCKER_PASSWORD` - Docker Hub password or token
- `PYPI_API_TOKEN` - PyPI API token for package publishing
- `CODECOV_TOKEN` - Codecov token for coverage reporting (optional)

### Setting Secrets
1. Navigate to: https://github.com/llamasearchai/OpenGov-EarlyJapanese/settings/secrets/actions
2. Click "New repository secret"
3. Add each secret with its corresponding value

## Monitoring and Health Checks

### Health Endpoint
```bash
# Check API health
curl http://localhost:8000/health

# Expected response:
{"status": "ok"}
```

### Docker Health Checks
All services include health checks in docker-compose:
- API: HTTP check on /health endpoint
- PostgreSQL: pg_isready command
- Redis: redis-cli ping

### Metrics and Logging
- Structured logging with `structlog`
- JSON log format for easy parsing
- Prometheus-compatible metrics (when enabled)
- Configurable log levels via `LOG_LEVEL` environment variable

## Security Considerations

### Production Checklist
- [ ] Change default SECRET_KEY and JWT_SECRET
- [ ] Configure DATABASE_URL with production database
- [ ] Set up HTTPS/TLS for API endpoints
- [ ] Configure CORS_ORIGINS for production domains
- [ ] Enable rate limiting on API endpoints
- [ ] Set up monitoring and alerting
- [ ] Configure backup strategy for database
- [ ] Review and update security settings
- [ ] Enable authentication for admin endpoints
- [ ] Set up firewall rules for services

### Environment Variables
Never commit these to version control:
- `SECRET_KEY`
- `JWT_SECRET`
- `DATABASE_URL`
- `REDIS_URL`
- `PYPI_API_TOKEN`
- `DOCKER_PASSWORD`

## Testing in Production

### Smoke Tests
```bash
# Test API
curl http://your-domain.com/health
curl http://your-domain.com/

# Test hiragana endpoint
curl http://your-domain.com/hiragana/a_row

# Test CLI
docker exec opengov-earlyjapanese-api nihongo --version
```

### Load Testing
```bash
# Using Apache Bench
ab -n 1000 -c 10 http://your-domain.com/health

# Using hey
hey -n 1000 -c 10 http://your-domain.com/hiragana/a_row
```

## Backup and Recovery

### Database Backups
```bash
# PostgreSQL backup
docker exec opengov-earlyjapanese-postgres pg_dump -U postgres opengov_earlyjapanese > backup.sql

# Restore
docker exec -i opengov-earlyjapanese-postgres psql -U postgres opengov_earlyjapanese < backup.sql
```

### Redis Backups
```bash
# Redis backup (automatic with appendonly yes)
docker exec opengov-earlyjapanese-redis redis-cli BGSAVE
```

## Scaling Considerations

### Horizontal Scaling
- Use load balancer (nginx, HAProxy) for multiple API instances
- Configure session storage in Redis for stateless API
- Use read replicas for PostgreSQL database
- Implement caching strategy with Redis

### Vertical Scaling
- Adjust Docker container resource limits
- Configure worker processes for uvicorn
- Optimize database queries and indexes
- Enable query caching

## Troubleshooting

### Common Issues

#### Port Already in Use
```bash
# Find process using port
lsof -i :8000

# Kill process
kill -9 <PID>
```

#### Docker Build Fails
```bash
# Clear Docker cache
docker system prune -a

# Rebuild without cache
docker build --no-cache -t llamasearchai/opengov-earlyjapanese:latest .
```

#### Tests Fail
```bash
# Run tests with verbose output
uv run pytest -v

# Run specific test
uv run pytest tests/unit/test_hiragana.py -v
```

## Support and Maintenance

### Regular Maintenance Tasks
- Update dependencies monthly
- Review security advisories
- Monitor application logs
- Check database performance
- Review and rotate secrets
- Update documentation

### Getting Help
- GitHub Issues: https://github.com/llamasearchai/OpenGov-EarlyJapanese/issues
- Email: nikjois@llamasearch.ai
- Documentation: https://github.com/llamasearchai/OpenGov-EarlyJapanese

## Version History

### v0.2.0 (2025-09-30)
- 100% test coverage achievement
- 158 comprehensive tests
- Enhanced CLI with complete command registration
- Improved katakana module
- Production-ready quality standards

### v0.1.0 (2025-09-30)
- Initial production release
- Complete Japanese learning platform
- Docker and CI/CD infrastructure
- Comprehensive documentation

---

**Last Updated**: September 30, 2025  
**Document Version**: 1.1  
**Status**: Production Ready - 100% Test Coverage

