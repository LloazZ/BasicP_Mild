dis = int(input("ระยะทาง (km) : "))

if dis >= 5 and dis <= 50:
    print("ค่าส่ง 10 บาท")
elif dis >=51 and dis <= 100:
    print("ค่าส่ง 15 บาท")
elif dis >=101 and dis <= 300:
    print("ค่าส่ง 25 บาท")
elif dis >=301 and dis <= 500:
    print("ค่าส่ง 35 บาท")
elif dis > 500:
    print("ค่าส่ง 45 บาท")
else:
    print("ส่งฟรี")