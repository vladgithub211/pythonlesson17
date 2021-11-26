def get_formatted_name(first_name, last_name):
#Возвращает аккуратно отформатированное полное имя
	full_name = f"{first_name} {last_name}"
	return full_name.title()

first_name = str(input("введите ваше имя "))
last_name = str(input("введите ашу фамилию "))
musician = get_formatted_name(first_name, last_name)
print(musician)
