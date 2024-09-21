FROM alpine:latest
WORKDIR /app
COPY . .
RUN apk add cups-client python3 py3-dotenv