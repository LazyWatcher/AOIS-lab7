import unittest

from main import Matrix


class MyTestCase(unittest.TestCase):
    def test_something(self):
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
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
