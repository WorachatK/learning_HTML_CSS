from flask import Flask,render_template #อิมพอร์ตโมดูล

app = Flask(__name__)

@app.route('/')
def index():  #def  เป็นคำสำคัญสำหรับการสร้างฟังก์ชัน
   return render_template('index.html') #เรนเดอร์ไฟล์ที่ชื่อ index ที่อยู่ในไดเร้กทอรี่ที่ชื่อ templates


if __name__ == '__main__':
   app.run()