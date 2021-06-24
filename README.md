# Steps Monitoring Server

## Install

- docker
- docker-compose

## Setup

### 1. Clone

```bash
git clone git@github.com:ITK13201/steps-monitoring-server.git
cd steps-monitoring-server
```

### 2. docker build

```bash
docker-compose build
```

## Usage

### Start container

```bash
docker-compose up -d
```

### Stop container

```bash
docker-compose down
```

### Logging

```bash
docker-compose logs -f
```

### Migrate

```bash
docker-compose exec app python manage.py migrate
```

### Create superuser

```bash
docker-compose exec app python manage.py createsuperuser
```
