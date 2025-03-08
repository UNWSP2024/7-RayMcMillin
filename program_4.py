# Ray McMillin, 3/7/25, 3D Coordinates Code

import math

def distance(point1, point2):
  
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)

def main():
    while True:
        try:
            x1, y1, z1 = map(float, input("Enter the first point (x1 y1 z1): ").split())
            x2, y2, z2 = map(float, input("Enter the second point (x2 y2 z2): ").split())
            point1 = (x1, y1, z1)
            point2 = (x2, y2, z2)
            
            result = distance(point1, point2)
            print(f"The distance between the points is: {result:.2f}")
            break
        except ValueError:
            print("Invalid input. Please enter three numerical digits. (ex. 1 2 3)")

if __name__ == "__main__":
    main()
