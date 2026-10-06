correct_password = "python123"

login_successful = 'False'

for attempts_used in range (1,4):

    password = input()

    if password == correct_password:
        login_successful = 'True'
        break

print(login_successful)
print(attempts_used)
