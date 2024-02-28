# Klavyeden girdiğiniz üç sayıyı büyükten küçüğe doğru sıralayın ve ordaki sayının diğer 2 sayı ile arasındaki farkı bulacak ifadeyiz yazın.

number1 = int(input(f"Lütfen ilk sayıyı giriniz : "))
number2 = int(input(f"Lütfen ikinci sayıyı giriniz : "))
number3 = int(input(f"Lütfen üçüncü sayıyı giriniz : "))

list_numbers = [number1, number2, number3]
list_numbers.sort(reverse=True)
print(f"Girdiğiniz üç sayının büyükten küçüğe sıralı hali : {list_numbers}")

difference_first_second_numbers = list_numbers[0] - list_numbers[1]
difference_third_second_numbers = list_numbers[1] - list_numbers[2]

print(f"İlk sayının medyan ile farkı : {difference_first_second_numbers}")
print(f"Son sayının medyan ile farkı : {difference_third_second_numbers}")
