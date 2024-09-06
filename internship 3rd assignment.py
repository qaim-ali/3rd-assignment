import numpy as np
from sklearn.linear_model import LinearRegression
import statistics
import sympy
import matplotlib.pyplot as plt

# 1. Ask for user's name, age, and favorite number
name = input("Enter your name: ")
age = int(input("Enter your age: "))
fav_number = float(input("Enter your favorite number: "))

# 2. Generate a random array of 10 numbers using NumPy and calculate statistics
random_array = np.random.rand(10)
mean_value = np.mean(random_array)
median_value = np.median(random_array)
std_dev = np.std(random_array)

print(f"\nRandom Array: {random_array}")
print(f"Mean: {mean_value}, Median: {median_value}, Standard Deviation: {std_dev}")

# 3. Simple linear regression model using scikit-learn
X = np.array([[age]]).reshape(-1, 1)  # User's age as the feature
y = np.array([fav_number])  # User's favorite number as the target
reg_model = LinearRegression().fit(X, y)
predicted_value = reg_model.predict([[age]])

print(f"\nLinear Regression: For age {age}, predicted favorite number is {predicted_value[0]}")

# 4. Calculate correlation coefficient using statistics library
if len([age]) > 1 and len([fav_number]) > 1:
    correlation = statistics.correlation([age], [fav_number])
    print(f"\nCorrelation Coefficient between age and favorite number: {correlation}")
else:
    print("\nNot enough data points to calculate correlation coefficient (need at least two).")


# 5. Conditional statements to check the user's age
if age < 18:
    print("You're a minor!")
elif age == 21:
    print("You're 21, congratulations!")
else:
    print("You're an adult!")

# 6. Generate a list of prime numbers up to 100 using a loop and sympy
primes = []
for num in range(2, 101):
    if sympy.isprime(num):
        primes.append(num)

print(f"\nPrime numbers up to 100: {primes}")

# 7. Plot user's age vs favorite number using matplotlib
plt.scatter([age], [fav_number], color='blue', label='Age vs Favorite Number')
plt.xlabel('Age')
plt.ylabel('Favorite Number')
plt.title(f"{name}'s Age vs Favorite Number")
plt.legend()
plt.grid(True)
plt.show()


