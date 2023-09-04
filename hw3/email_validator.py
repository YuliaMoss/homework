# 3. Написати валідатор для пошти. Користувач вводить пошту, а програма повинна перевірити,
# що в пошті є символ '@' і '.', і якщо це так, вивести "YES", інакше "NO"
email = str(input("Enter your email: "))

right_email = True if "@" in email and "." in email else False
if right_email:
    print("YES")
else:
    print("NO")
