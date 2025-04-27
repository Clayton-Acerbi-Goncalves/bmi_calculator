
user_name = input('Enter your first name: ').lower()
user_height = float(input('Enter your height: '))
user_weight = float(input('Enter your weight: '))

bmi = user_weight / user_height **2

print(f'{user_name} has a height of {user_height:.2f} meters')
print(f'Your weight is {user_weight} kg')
print(f'And your BMI is {bmi:.2f}')