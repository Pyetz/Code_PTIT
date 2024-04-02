def Eulerian_Cycle(G, u):
  # Kiểm tra tính liên thông
  if not is_connected(G):
    return "Đồ thị không liên thông, không tồn tại chu trình Euler"

  # Kiểm tra bậc của mỗi đỉnh
  for v in G:
    if len(G[v]) % 2 == 1 and len(G[v]) != 1:
      return "Đồ thị không có chu trình Euler"

  # Khởi tạo
  stack = []
  CE = []
  stack.append(u)

  while stack:
    # Lấy đỉnh ở đầu ngăn xếp
    s = stack.pop()

    # Nếu danh sách kề của s chưa rỗng
    if G[s]:
      # Lấy đỉnh đầu tiên trong danh sách kề của s
      t = G[s].pop(0)

      # Đưa t vào stack
      stack.append(t)

      # Loại bỏ cạnh (s, t)
      G[s].remove(t)

    # Trường hợp danh sách kề của s rỗng
    else:
      # Đưa s ra khỏi ngăn xếp
      CE.append(s)

  # Lật ngược lại các đỉnh trong CE
  CE.reverse()

  return CE


# Ví dụ
G = [[1, 2], [3], [4], []]
u = 0

cycle = Eulerian_Cycle(G, u)

print("Chu trình Euler:", cycle)
