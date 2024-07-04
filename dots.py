import cv2
import numpy as np
import random
import os
import csv

def generate_image_with_dots(image_size=(1080,1920), max_dots=100):
    image = np.ones((image_size[0], image_size[1], 3), dtype=np.uint8) * 255
    
    colors = {
        'red': (0, 0, 255),
        'green': (0, 255, 0),
        'blue': (255, 0, 0)
    }
    
    counts = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    
    occupied_positions = set()

    def draw_dot(color, count_key):
        while True:
            dot_radius = random.randint(10,20)
            x = random.randint(dot_radius, image_size[0] - dot_radius - 1)
            y = random.randint(dot_radius, image_size[1] - dot_radius - 1)
            if not any((x + dx, y + dy) in occupied_positions for dx in range(-dot_radius, dot_radius + 1) for dy in range(-dot_radius, dot_radius + 1)):
                cv2.circle(image, (y, x), dot_radius - 1, color,-1)
                for dx in range(-dot_radius, dot_radius + 1):
                    for dy in range(-dot_radius, dot_radius + 1):
                        occupied_positions.add((x + dx, y + dy))
                counts[count_key] += 1
                break

    for _ in range(random.randint(1, max_dots)):
        draw_dot(colors['red'], 'red')
    
    for _ in range(random.randint(1, max_dots)):
        draw_dot(colors['green'], 'green')
    
    for _ in range(random.randint(1, max_dots)):
        draw_dot(colors['blue'], 'blue')
    
    return image, counts

if __name__ == '__main__':
    if not os.path.exists('images'):
        os.makedirs('images')
    number_of_images = int(input("Enter Number of Clock Images to generate: "))
    with open('labels.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['File Name', 'Red Count', 'Green Count', 'Blue Count'])
        for i in range(1, number_of_images + 1):
            image_with_dots, counts = generate_image_with_dots()
            cv2.imwrite(f'images/dots_{i}.png', image_with_dots)
            writer.writerow([f'dots_{i}.png', counts['red'], counts['green'], counts['blue']])
    print(f"Successfully generated {number_of_images} images")
    