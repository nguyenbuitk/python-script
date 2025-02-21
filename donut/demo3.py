import math
import os
import time

def render_donut_y_rotation():
    R1, R2 = 1, 2  # Bán kính của vòng trong và vòng ngoài
    K1 = 30 # Hằng số chiếu phối cảnh
    K2 = 4  # Độ zoom (độ xa của hình)
    screen_width, screen_height = 80, 40  # Kích thước màn hình (ASCII)
    chars = ".,-~:;=!*#$@"  # Ký tự ASCII theo độ sáng
    A = 0  # Góc quay quanh trục y

    while True:
        z_buffer = [-float("inf")] * (screen_width * screen_height)
        output = [" "] * (screen_width * screen_height)

        for theta in range(0, 628, 20):  # Góc theta từ 0 đến 2π (0-360 độ)
            costheta, sintheta = math.cos(theta / 100), math.sin(theta / 100)

            for phi in range(0, 628, 3):  # Góc phi từ 0 đến 2π
              cosphi, sinphi = math.cos(phi / 100), math.sin(phi / 100)

              # Tọa độ 3D của điểm trên donut
              circle_x = R2 + R1 * costheta
              circle_y = R1 * sintheta

              # Xoay quanh trục y
              x = circle_x * math.cos(A)
              y = circle_y
              z = K2 + circle_x * math.sin(A)
              ooz = 1 / z

              # Chiếu sang tọa độ 2D
              xp = int(screen_width / 2 + K1 * ooz * x)
              yp = int(screen_height / 2 - K1 * ooz * y)

              # Tính ánh sáng
              luminance = math.floor((costheta * cosphi) * 8)
              if 0 <= xp < screen_width and 0 <= yp < screen_height and ooz > z_buffer[yp * screen_width + xp]:
                  z_buffer[yp * screen_width + xp] = ooz
                  output[yp * screen_width + xp] = chars[luminance]

        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n".join(["".join(output[i:i + screen_width]) for i in range(0, len(output), screen_width)]))
        A += 0.1# Tăng góc xoay quanh trục y
        time.sleep(0.03)

if __name__ == "__main__":
    render_donut_y_rotation()

