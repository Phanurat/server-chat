# สร้าง Docker image
docker build -t my-python-server .

# รัน Docker container จาก image ที่สร้างขึ้น
docker run -d -p 12345:12345 --name my-server my-python-server

# สร้าง Docker images
docker-compose build

# เริ่มบริการ
docker-compose up
