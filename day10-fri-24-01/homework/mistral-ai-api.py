import os
import re
from mistralai import Mistral
import numpy as np
import matplotlib.pyplot as plt
import dotenv
import json

dotenv.load_dotenv()

PROMPT = """
Given a user's request for plotting a function, return this exact format:
function_name(parameters) = x_min:x_max

For basic functions:
- y=x: linear(1*x + 0)
- y=x^2: quadratic(1,0,0)
- sin(x): sine(1)
- cos(x): cosine(1)

For polynomials (degree 1 to 4):
- y = x^3 - 3x^2 + 5x - 1 → polynomial(1,-3,5,-1)

For sine and cosine with parameters:
- sin(3x) → sine(3)
- cos(3x) → cosine(3)

If user wants to exit, return: exit()
If user did not type a function name or parameters, you should think of a function name and parameters base on the user's request.
If user did not type x_min and x_max, you should think of x_min and x_max base on the user's request.
If user typed only function name, you should think of x_min and x_max base on the user's request.
Whatever the user types, you should return the function name and parameters in this format: function_name(parameters) = x_min:x_max , you should think for it.
Example: "I need sine from -5 to 5" → "sine(1) = -5:5"

User request: {input}
"""

def extract_plot_request(user_input):
    client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])
    response = client.chat.complete(
        model="mistral-large-latest",
        messages=[{"role": "user", "content": PROMPT.format(input=user_input)}]
    )
    return response.choices[0].message.content

def parse_response(response):
    match = re.match(r"(?P<function>[a-z]+)\((?P<params>.*?)\)\s*=\s*(?P<x_min>-?\d+)\s*:\s*(?P<x_max>-?\d+)", response)
    if match:
        return match.group("function"), match.group("params"), float(match.group("x_min")), float(match.group("x_max"))
    else:
        return None, None, None, None
        
def plot_function(func_name, params, x_min, x_max):
    x = np.linspace(x_min, x_max, 500)
    if func_name == "linear":
        a, b = map(float, params.split("*x + "))
        y = a * x + b
    elif func_name == "quadratic":
        a, b, c = map(float, params.split(","))
        y = a * x**2 + b * x + c
    elif func_name == "sine":
        k = float(params)
        y = np.sin(k * x)
    elif func_name == "cosine":
        k = float(params)
        y = np.cos(k * x)
    elif func_name == "polynomial":
        coeffs = list(map(float, params.split(",")))
        y = np.polyval(coeffs, x)
    else:
        print("Unsupported function")
        return False

    plt.plot(x, y)
    plt.title(f"Plot of {func_name} function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()
    return True

def main():
    while True:
        user_input = input("What can I help you with your plot for today? : ")
        
        if "bye" in user_input.lower() or "exit" in user_input.lower():
            print("Have a nice day, Bye!")
            break

        response = extract_plot_request(user_input)
        func_name, params, x_min, x_max = parse_response(response)

        if func_name == "exit":
            print("Goodbye!")
            break
        elif all(v is not None for v in [func_name, x_min, x_max]):
            plot_function(func_name, params, x_min, x_max)
        else:
            print("Invalid request. Please try again.")

if __name__ == "__main__":
    main()
    