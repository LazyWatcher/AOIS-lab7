import random


class Matrix:
    def __init__(self, row=16, col=16):
        self.row = row
        self.col = col
        self.matrix = [[random.randint(0, 1) for _ in range(col)] for _ in range(row)]

    def printMatrix(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.matrix[i][j], end=" ")
            print()

    def set(self, x, y, value):
        self.matrix[x][y] = value

    def get(self, x, y):
        return self.matrix[x][y]

    def getWord(self, index):
        word = ''.join(str(self.matrix[(index + i) % self.row][index]) for i in range(self.col))
        return word

    def getAddressRow(self, index):
        row_str = ''.join(str(self.matrix[(index + i) % self.row][i]) for i in range(self.col))
        return row_str

    def printWord(self, index):
        print(f"Слово {index}: {self.getWord(index)}")

    def printAddressRow(self, index):
        print(f"Адресный столбец {index}: {self.getAddressRow(index)}")

    def setColumnWord(self, word, col):
        length = min(len(word), self.row)
        for i in range(length):
            self.matrix[(col + i) % self.row][col] = int(word[i])

    def processWordsByKey(self, key):
        key_length = len(key)

        for i in range(self.col):
            word = self.getWord(i)
            if word[:key_length] == key:
                V = word[:3]
                A = word[3:7]
                B = word[7:11]
                S = word[11:16]

                A_int = int(A, 2)
                B_int = int(B, 2)
                S_int = A_int + B_int
                S_new = f"{S_int:05b}"
                new_word = V + A + B + S_new

                return new_word

        return None

    def invertWord(self, word):
        inverted = ''.join('1' if ch == '0' else '0' for ch in word)
        return inverted

    def binary_addition(self, word1, word2):
        max_len = max(len(word1), len(word2))
        word1 = word1.zfill(max_len)
        word2 = word2.zfill(max_len)
        result = []
        carry = 0

        for i in range(max_len - 1, -1, -1):
            total_sum = carry
            total_sum += 1 if word1[i] == '1' else 0
            total_sum += 1 if word2[i] == '1' else 0
            result.append('1' if total_sum % 2 == 1 else '0')
            carry = 0 if total_sum < 2 else 1

        if carry != 0:
            result.append('1')

        result.reverse()
        return ''.join(result)

    def binary_multiplication(self, word1, word2):
        product = 0
        word1_int = int(word1, 2)
        word2_int = int(word2, 2)
        product = word1_int * word2_int
        return f"{product:0{len(word1)}b}".zfill(len(word1))

    def f6(self, word1, word2):
        inverted_word1 = self.invertWord(word1)
        inverted_word2 = self.invertWord(word2)
        part1 = self.binary_multiplication(inverted_word1, word2)
        part2 = self.binary_multiplication(word1, inverted_word2)
        result = self.binary_addition(part1, part2)
        return result[-16:]

    def f9(self, word1, word2):
        inverted_word1 = self.invertWord(word1)
        inverted_word2 = self.invertWord(word2)
        part1 = self.binary_multiplication(word1, word2)
        part2 = self.binary_multiplication(inverted_word1, inverted_word2)
        result = self.binary_addition(part1, part2)
        return result[-16:]

    def f4(self, word1, word2):
        inverted_word1 = self.invertWord(word1)
        result = self.binary_multiplication(inverted_word1, word2)
        return result[-16:]

    def f11(self, word1, word2):
        inverted_word2 = self.invertWord(word2)
        result = self.binary_addition(word1, inverted_word2)
        return result[-16:]

    def sortWords(self):
        words = [self.getWord(i) for i in range(self.col)]
        words.sort()
        for i, word in enumerate(words):
            self.setColumnWord(word, i)



matrix = Matrix()
print("Матрица:")
matrix.printMatrix()
print()

matrix.printWord(0)
matrix.printAddressRow(0)
print()




key = "111"
print(f"Ключ: {key}")
processed_word = matrix.processWordsByKey(key)
print("Слово по ключу:")
if processed_word:
    print(processed_word)
else:
    print("Слово не найдено")
print()



word1 = matrix.getWord(1)
word2 = matrix.getWord(0)

result1 = matrix.f6(word1, word2)
result2 = matrix.f9(word1, word2)
result3 = matrix.f4(word1, word2)
result4 = matrix.f11(word1, word2)

print(f"Первое слово: {word1}")
print(f"Второе слово: {word2}")
print(f"f6: {result1}")
print(f"f9: {result2}")
print(f"f4: {result3}")
print(f"f11: {result4}")
print()


print("До сортировки:")
matrix.printMatrix()
matrix.sortWords()
print("После сортировки:")
matrix.printMatrix()
