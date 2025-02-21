def get_brightness(light_intensity):
  chars = ".,-~:;=!*#$@"
  index = int(light_intensity * (len(chars) -1))
  return chars[index]

def project_3d_to_2d(x, y ,z, viewer_distance=5.0):
  x_proj = (viewer_distance * x) / (viewer_distance + z)
  y_proj = (viewer_distance * y) / (viewer_distance + z)

  light_intensity = min(max(z / 10.0, 0.0), 1.0)

  pixel = get_brightness(light_intensity)

  return x_proj, y_proj, pixel

x, y, z = 2.0, 3.0, 4.0
x_proj, y_proj, pixel = project_3d_to_2d(x, y, z)

print(f"Initial 3D point: ({x:.2f}, {y:.2f}, {z:.2f}")
print(f"After 3D point: ({x_proj:.2f}, {y_proj:.2f})")
print(f"ASCII display: {pixel}")
