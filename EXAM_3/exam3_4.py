def slope(a, b, c):
    if b == 0:
        return "Not available"
    else:
        output = -a / b
        if output != int(output):
            return f'{output}'
        else:
            return f'{int(output)}'

def xIntercept(a, b, c):
    if a == 0:
        return "Not available"
    else:
        output = -c / a
        if output != int(output):
            return f'{output}'
        else:
            return f'{int(output)}'

def yIntercept(a, b, c):
    if b == 0:
        return "Not available"
    else:
        output = c / b
        if output != int(output):
            return f'{output}'
        else:
            return f'{int(output)}'

def main():
    print("Linear equation")
    a, b, c = input("Enter a, b, c : ").split()
    
    try:
        a, b, c = int(a), int(b), int(c)
        
        slope_result = slope(a, b, c)
        x_intercept_result = xIntercept(a, b, c)
        y_intercept_result = yIntercept(a, b, c)
        
        print(f"Slope = {slope_result}")
        print(f"X-intercept = {x_intercept_result}")
        print(f"Y-intercept = {y_intercept_result}")
    except ValueError:
        print("Slope = Not available")
        print("X-intercept = Not available")
        print("Y-intercept = Not available")

if __name__ == "__main__":
    main()