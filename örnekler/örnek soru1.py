# Kullanıcının girdiği 5 basamaklı bir sayının basamaklarının toplamını ekrana yazdıran kodu yazınız.

user_value = input(f"5 Basamaklı bir sayı giriniz : ")
if len(user_value) == 5:
    first = int(user_value[0])
    second = int(user_value[1])
    third = int(user_value[2])
    fourth = int(user_value[3])
    fifth = int(user_value[4])
    sum_numbers = first + second + third + fourth + fifth
    print(sum_numbers)
else:
    print("Girdiğiiniz sayı 5 basamaklı değildir.")
