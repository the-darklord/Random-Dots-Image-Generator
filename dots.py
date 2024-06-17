import cv2
import numpy as np
import random

def generate_image_with_dots(image_size=(500, 500), max_dots=100):
    label_area_height = 150 + 10
    total_height = image_size[0] + label_area_height
    image = np.ones((total_height + 10, image_size[1] + 10, 3), dtype=np.uint8) * 255
    
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
    dot_radius = 5

    def draw_dot(color, count_key):
        while True:
            x = random.randint(label_area_height + dot_radius, total_height - dot_radius - 1)
            y = random.randint(dot_radius, image_size[1] - dot_radius - 1)
            if not any((x + dx, y + dy) in occupied_positions for dx in range(-dot_radius, dot_radius + 1) for dy in range(-dot_radius, dot_radius + 1)):
                cv2.circle(image, (y, x), dot_radius, color, -1)
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
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, f'Red: {counts["red"]}', (10, 50), font, 1, colors['red'], 2, cv2.LINE_AA)
    cv2.putText(image, f'Green: {counts["green"]}', (10, 100), font, 1, colors['green'], 2, cv2.LINE_AA)
    cv2.putText(image, f'Blue: {counts["blue"]}', (10, 150), font, 1, colors['blue'], 2, cv2.LINE_AA)
    
    return image

if __name__ == '__main__':
    number_of_images = int(input("Enter Number of Clock Images to generate : "))
    for i in range(1,number_of_images+1):
        image_with_dots = generate_image_with_dots()
        cv2.imwrite(f'images/dots_{i}.png', image_with_dots)
    print(f"Successfully generated {number_of_images} images")
    
