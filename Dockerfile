FROM python:3.12-slim

WORKDIR /app

COPY app/app.py .

ARG VERSION=unknown
ENV VERSION=$VERSION
ENV PORT=8080

EXPOSE 8080

CMD ["python", "app.py"]
