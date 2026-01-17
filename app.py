import math

def hcf_lcm(num1, num2):
    hcf = math.gcd(num1, num2)
    lcm = abs(num1 * num2) // hcf

    return {
        "Hcf": hcf,
        "lcm": lcm
    }

if __name__ == "__main__":
    num1 = int(input("Enter first value: "))
    num2 = int(input("Enter second value: "))

    result = hcf_lcm(num1, num2)
    print("Hcf:", result["Hcf"])
    print("lcm:", result["lcm"])
