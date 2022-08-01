# nhập chiều cao và cân nặng
cao = float(input())
nang = float(input())
# tính bmi
bmi = nang/(cao**2)
# xét bmi
if bmi < 18.5:
    print("BMI:", bmi, "- Gầy", "- Ráng ăn nhiều zô!!!")
elif bmi >= 18.5 and bmi < 24.9:
    print("BMI:", bmi, "- Bình thường", "- Tốt lắm!")
elif bmi >= 25 and bmi < 30:
    print("BMI:", bmi, "- Nguy cơ béo phì", "- Hơi béo nhaa")
elif bmi >= 30 and bmi < 35:
    print("BMI:", bmi, "- Béo phì cấp độ I", "- Giảm cân đêyy")
elif bmi >= 35 and bmi < 40:
    print("BMI:", bmi, "- Béo phì cấp độ II", "- Giảm cân gấpp")
elif bmi >= 40:
    print("BMI:", bmi, "- Béo phì cấp độ III", "- Ét Ô Ét")
