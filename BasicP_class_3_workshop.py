monster_hp = 100
spear = 30
sword = 25
bow = 20
Game = True
while Game:
    print("เกม Starburst Stream")
    print("1.โจมตีมอนเตอร์")
    print("2.หนี")
    choose = int(input("เลือก ( 1 / 2): "))
    if choose == 1:
        times = int(input("จะตีกี่รอบ: "))
        for i in range(times):
            print("รอบที่", i)
            weapons = input("จะใช้อาวุธไหนโจมตี (Sword / Spear / Bow): ")
            if weapons == "Sword":
                monster_hp -= sword
                print("เลือดมอนสเตอร์", monster_hp)
            elif weapons == "Spear":
                monster_hp -= spear
                print("เลือดมอนสเตอร์", monster_hp)
            elif weapons == "Bow":
                monster_hp -= bow
                print("เลือดมอนสเตอร์", monster_hp)
            else:
                print("เลือกได้แค่ 3 ชนิดนี้เท่านั้น")
    elif choose == 2:
        break
    else:
        print("เลือกตอบได้แค่ 1 กับ 2")

#ยังไม่เสร็จเหลือ monster_hp check ว่ามอนสเตอร์ตายหรือยังและเงื่อนไขว่าชนะหรือแพ้