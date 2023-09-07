import random

def estimate_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            inside_circle += 1

    estimated_pi = 4 * inside_circle / num_points
    return estimated_pi

def main():
    try:
        num_points = int(input("Enter the number of random points to generate: "))
        if num_points <= 0:
            print("Please enter a positive integer.")
        else:
            pi_approximation = estimate_pi(num_points)
            print(f"Approximated value of pi using {num_points} random points: {pi_approximation}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()