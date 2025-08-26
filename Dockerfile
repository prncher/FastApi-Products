FROM python:3.10-alpine
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
# indicates the port from the host. If the host is using 4000 from env file, change the expose.
EXPOSE 8080
CMD ["fastapi","run", "./services/products.py","--port","8080"]
