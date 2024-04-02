def Euler_Cycle(u):
  """
  Tìm chu trình Euler trong đồ thị G bắt đầu từ đỉnh u.

  Tham số:
    u: Đỉnh bắt đầu.

  Trả về:
    Danh sách các đỉnh trong chu trình Euler.
  """

  stack = []  # Khởi tạo một ngăn xếp rỗng.
  CE = []  # Khởi tạo mảng lưu trữ chu trình Euler.
  stack.append(u)  # Đưa đỉnh u vào ngăn xếp.

  while stack:
    # Lấy đỉnh ở đầu ngăn xếp.
    s = stack.pop()

    # Nếu danh sách cạnh của s còn cạnh nào.
    if Ke(s):
      # Lấy đỉnh đầu tiên trong danh sách cạnh.
      t = Ke(s).pop(0)

      # Đưa t vào ngăn xếp.
      stack.append(t)

      # Loại bỏ cạnh (s, t) khỏi đồ thị.
      E.remove((s, t))

    # Nếu danh sách cạnh của s rỗng.
    else:
      # Đưa s vào mảng CE.
      CE.append(s)

  # Lật ngược mảng CE để có chu trình Euler.
  CE.reverse()

  return CE


# Ví dụ sử dụng.
G = {
  "A": ["B", "C"],
  "B": ["A", "D"],
  "C": ["A", "E"],
  "D": ["B", "F"],
  "E": ["C", "F"],
  "F": ["D", "E"],
}

u = "A"
cycle = Euler_Cycle(u)

print("Chu trình Euler:", cycle)
