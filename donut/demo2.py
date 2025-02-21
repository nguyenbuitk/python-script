import math

# Hàm chiếu điểm 3D sang 2D
def project_3d_to_2d(x, y, z, viewer_distance=5.0):
    x_proj = (viewer_distance * x) / (viewer_distance + z)
    y_proj = (viewer_distance * y) / (viewer_distance + z)
    return int(x_proj * 10 + 20), int(y_proj * 10 + 10)  # Quy đổi tọa độ sang màn hình terminal

# Khởi tạo các đỉnh của khối lập phương
cube_vertices = [
    (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),  # Mặt trước
    (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)       # Mặt sau
]

# Các cạnh của khối lập phương (chỉ số từ mảng `cube_vertices`)
cube_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Mặt trước
    (4, 5), (5, 6), (6, 7), (7, 4),  # Mặt sau
    (0, 4), (1, 5), (2, 6), (3, 7)   # Nối giữa mặt trước và mặt sau
]

# Tạo màn hình rỗng (terminal 40x20)
screen = [[" " for _ in range(40)] for _ in range(20)]

# Dựng khối lập phương
for edge in cube_edges:
    # Lấy hai điểm đầu cuối của cạnh
    start = cube_vertices[edge[0]]
    end = cube_vertices[edge[1]]
    
    # Chiếu hai điểm sang 2D
    x1, y1 = project_3d_to_2d(*start)
    x2, y2 = project_3d_to_2d(*end)
    
    # Vẽ cạnh bằng cách nối các điểm
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))  # Số bước để vẽ
    for i in range(steps + 1):
        x = int(x1 + dx * (i / steps))
        y = int(y1 + dy * (i / steps))
        if 0 <= x < 40 and 0 <= y < 20:
            screen[y][x] = "#"

# Hiển thị màn hình
for row in screen:
    print("".join(row))

