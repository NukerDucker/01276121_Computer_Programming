# กำหนดค่าคงที่สำหรับโหมดเพิ่มขึ้นและลดลง
INCREASING = '0'
DECREASING = '1'

def find_substrings(input_data):
    mode, numbers = input_data.split('/')
    numbers = [int(num) for num in numbers.split()] # แปลงตัวเลขเป็นลิสต์ของ int
    if len(numbers) < 2:
        return None
    # เริ่มต้น substring ด้วยตัวเลขตัวแรก
    substrings = [str(numbers[0])]
    for num in numbers[1:]:
        # ดึงตัวสุดท้ายจาก substring ล่าสุด
        last_number = int(substrings[-1][-1])
        
        # ตรวจสอบตามโหมดที่กำหนด
        if mode == INCREASING:
            is_next = num == last_number + 1
        elif mode == DECREASING: 
            is_next = num == last_number - 1
            
        # ถ้าตัวถัดไปตรงตามเงื่อนไข จะรวมตัวเลขเข้ากับ substring ล่าสุด
        if is_next:
            substrings[-1] += str(num)
        else:
            # ไม่ตรงก็สร้าง substring ใหม่
            substrings.append(str(num))
    # return ลิสต์ของ substrings โดยรวมตัวเลขในแต่ละ substring เข้าด้วยกันเป็นสตริง
    return [" ".join(list(substring)) for substring in substrings]

def main():
    print("*** Find Substrings ***")
    user_input = input("Enter mode (0 for increasing, 1 for decreasing) and numbers: ")
    substrings = find_substrings(user_input)
    if substrings is None:
        print("Error: You need at least 2 numbers.")
    else:
        for i, substring in enumerate(substrings, 1):
            print(f"Substring {i}: {substring}")
    print("===== End of program =====")

if __name__ == "__main__":
    main()
