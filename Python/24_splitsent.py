import re

def split_into_sentences(text):
  """
  Tách luồng văn bản thành các câu.

  Args:
    text: Luồng văn bản đầu vào.

  Returns:
    Danh sách các câu.
  """

  # Xác định các dấu ngắt câu.
  sentence_delimiters = re.compile(r"[.!?]")

  # Tách luồng văn bản thành các chuỗi con.
  sentences = sentence_delimiters.split(text)

  # Xử lý các chuỗi con.
  processed_sentences = []
  for sentence in sentences:
    sentence = sentence.strip()
    sentence = sentence.capitalize()
    processed_sentences.append(sentence)

  return processed_sentences

# Đọc luồng văn bản từ stdin.
text = input()

# Tách luồng văn bản thành các câu.
sentences = split_into_sentences(text)

# In ra các câu.
for sentence in sentences:
  print(sentence)

