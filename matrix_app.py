# matrix_app.py - Консольное приложение для работы с матрицами (Вариант 4)
# Нахождение минимального элемента и его индексов

def input_matrix():
    """
    Функция для ввода матрицы с клавиатуры
    Возвращает: матрицу (список списков)
    """
    print("=== Ввод матрицы ===")
    
    # Ввод размерности
    while True:
        try:
            n = int(input("Введите количество строк (N): "))
            m = int(input("Введите количество столбцов (M): "))
            
            if n <= 0 or m <= 0:
                print("Размерность должна быть положительной!")
                continue
            break
        except ValueError:
            print("Ошибка! Введите целое число.")
    
    matrix = []
    print(f"\nВведите элементы матрицы {n}x{m}:")
    
    for i in range(n):
        row = []
        for j in range(m):
            while True:
                try:
                    value = float(input(f"Элемент [{i}][{j}]: "))
                    row.append(value)
                    break
                except ValueError:
                    print("Ошибка! Введите число.")
        matrix.append(row)
    
    return matrix

def print_matrix(matrix):
    """Красивый вывод матрицы"""
    if not matrix:
        print("Матрица пуста")
        return
    
    print("\n=== Матрица ===")
    for i, row in enumerate(matrix):
        # Форматированный вывод строки
        row_str = "│ "
        for value in row:
            row_str += f"{value:8.2f} "
        row_str += "│"
        print(row_str)
    print()

def find_min_element(matrix):
    """
    Нахождение минимального элемента и его индексов
    Возвращает: (минимальное_значение, строка, столбец)
    """
    if not matrix or not matrix[0]:
        return None, -1, -1
    
    min_value = matrix[0][0]
    min_i, min_j = 0, 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_i, min_j = i, j
    
    return min_value, min_i, min_j

def find_max_element(matrix):
    """
    Дополнительная функция: нахождение максимального элемента
    """
    if not matrix or not matrix[0]:
        return None, -1, -1
    
    max_value = matrix[0][0]
    max_i, max_j = 0, 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_i, max_j = i, j
    
    return max_value, max_i, max_j

def calculate_statistics(matrix):
    """Расчет статистики матрицы"""
    if not matrix:
        return {}
    
    stats = {
        'rows': len(matrix),
        'cols': len(matrix[0]),
        'total_elements': len(matrix) * len(matrix[0]),
        'sum': 0,
        'min': matrix[0][0],
        'max': matrix[0][0]
    }
    
    # Инициализируем индексы
    min_i = min_j = max_i = max_j = 0
    
    # Проходим по всем элементам
    for i in range(stats['rows']):
        for j in range(stats['cols']):
            value = matrix[i][j]
            stats['sum'] += value
            
            if value < stats['min']:
                stats['min'] = value
                min_i, min_j = i, j
            
            if value > stats['max']:
                stats['max'] = value
                max_i, max_j = i, j
    
    # Добавляем индексы
    stats['min_indices'] = (min_i, min_j)
    stats['max_indices'] = (max_i, max_j)
    stats['average'] = stats['sum'] / stats['total_elements']
    
    return stats

def main():
    """Основная функция приложения"""
    print("=" * 50)
    print("ПРОГРАММА ДЛЯ РАБОТЫ С МАТРИЦАМИ")
    print("Вариант 4: Нахождение минимального элемента и его индексов")
    print("=" * 50)
    
    while True:
        print("\nМЕНЮ:")
        print("1. Ввести новую матрицу")
        print("2. Найти минимальный элемент")
        print("3. Найти максимальный элемент")
        print("4. Показать статистику матрицы")
        print("5. Показать матрицу")
        print("6. Пример работы с тестовой матрицей")
        print("0. Выход")
        
        choice = input("\nВыберите действие (0-6): ")
        
        if choice == '0':
            print("\nДо свидания!")
            break
        
        elif choice == '1':
            matrix = input_matrix()
            print("\nМатрица успешно введена!")
        
        elif choice == '2':
            if 'matrix' not in locals() or not matrix:
                print("Сначала введите матрицу!")
                continue
            
            min_val, min_i, min_j = find_min_element(matrix)
            
            if min_val is not None:
                print(f"\n=== Минимальный элемент ===")
                print(f"Значение: {min_val}")
                print(f"Индексы: строка {min_i}, столбец {min_j}")
                print(f"Позиция: элемент [{min_i}][{min_j}]")
            else:
                print("Матрица пуста!")
        
        elif choice == '3':
            if 'matrix' not in locals() or not matrix:
                print("Сначала введите матрицу!")
                continue
            
            max_val, max_i, max_j = find_max_element(matrix)
            
            if max_val is not None:
                print(f"\n=== Максимальный элемент ===")
                print(f"Значение: {max_val}")
                print(f"Индексы: строка {max_i}, столбец {max_j}")
                print(f"Позиция: элемент [{max_i}][{max_j}]")
            else:
                print("Матрица пуста!")
        
        elif choice == '4':
            if 'matrix' not in locals() or not matrix:
                print("Сначала введите матрицу!")
                continue
            
            stats = calculate_statistics(matrix)
            
            print(f"\n=== Статистика матрицы ===")
            print(f"Размер: {stats['rows']}x{stats['cols']}")
            print(f"Всего элементов: {stats['total_elements']}")
            print(f"Сумма всех элементов: {stats['sum']:.2f}")
            print(f"Среднее значение: {stats['average']:.2f}")
            print(f"Минимальный элемент: {stats['min']:.2f}")
            print(f"  Индексы: {stats['min_indices']}")
            print(f"Максимальный элемент: {stats['max']:.2f}")
            print(f"  Индексы: {stats['max_indices']}")
        
        elif choice == '5':
            if 'matrix' not in locals() or not matrix:
                print("Сначала введите матрицу!")
                continue
            
            print_matrix(matrix)
        
        elif choice == '6':
            # Тестовая матрица для демонстрации
            test_matrix = [
                [3.5, 2.1, 5.7],
                [1.2, 4.8, 0.5],
                [7.3, 2.9, 6.4]
            ]
            
            print("\n=== Тестовая матрица 3x3 ===")
            print_matrix(test_matrix)
            
            min_val, min_i, min_j = find_min_element(test_matrix)
            max_val, max_i, max_j = find_max_element(test_matrix)
            
            print(f"Минимальный элемент: {min_val} на позиции [{min_i}][{min_j}]")
            print(f"Максимальный элемент: {max_val} на позиции [{max_i}][{max_j}]")
        
        else:
            print("Неверный выбор! Попробуйте снова.")

if __name__ == "__main__":
    main()