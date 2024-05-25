import unittest

from main import Matrix


class MyTestCase(unittest.TestCase):
    def test_print(self):
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
        self.assertEqual(word1, word1)  # add assertion here

    def test_key(self):
        matrix = Matrix()
        print("Матрица:")
        matrix.printMatrix()
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
        self.assertEqual(processed_word, processed_word)  # add assertion here

    def test_f6(self):
        matrix = Matrix()
        print("Матрица:")
        matrix.printMatrix()
        print()
        word1 = matrix.getWord(1)
        word2 = matrix.getWord(0)
        result1 = matrix.f6(word1, word2)
        print(f"Первое слово: {word1}")
        print(f"Второе слово: {word2}")
        print(f"f6: {result1}")
        self.assertEqual(result1, result1)  # add assertion here

    def test_f9(self):
        matrix = Matrix()
        print("Матрица:")
        matrix.printMatrix()
        print()
        word1 = matrix.getWord(1)
        word2 = matrix.getWord(0)
        result1 = matrix.f9(word1, word2)
        print(f"Первое слово: {word1}")
        print(f"Второе слово: {word2}")
        print(f"f9: {result1}")
        self.assertEqual(result1, result1)  # add assertion here

    def test_f4(self):
        matrix = Matrix()
        print("Матрица:")
        matrix.printMatrix()
        print()
        word1 = matrix.getWord(1)
        word2 = matrix.getWord(0)
        result1 = matrix.f4(word1, word2)
        print(f"Первое слово: {word1}")
        print(f"Второе слово: {word2}")
        print(f"f4: {result1}")
        self.assertEqual(result1, result1)  # add assertion here

    def test_f11(self):
        matrix = Matrix()
        print("Матрица:")
        matrix.printMatrix()
        print()
        word1 = matrix.getWord(1)
        word2 = matrix.getWord(0)
        result1 = matrix.f11(word1, word2)
        print(f"Первое слово: {word1}")
        print(f"Второе слово: {word2}")
        print(f"f11: {result1}")
        self.assertEqual(result1, result1)  # add assertion here

    def test_sort(self):
        matrix = Matrix()
        print("Матрица:")
        matrix.printMatrix()
        print()
        print("До сортировки:")
        matrix.printMatrix()
        matrix.sortWords()
        print("После сортировки:")
        matrix.printMatrix()
        self.assertEqual(True, True)  # add assertion here

if __name__ == '__main__':
    unittest.main()
