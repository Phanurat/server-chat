# Dockerfile for Server
FROM python:3.10-slim

# ตั้งค่าพาธทำงาน
WORKDIR /app

# คัดลอกไฟล์ที่จำเป็นไปยัง container
COPY server.py .

# กำหนดคำสั่งในการรัน
CMD ["python", "server.py"]
