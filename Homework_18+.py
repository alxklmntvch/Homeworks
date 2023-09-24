import networkx as nx
"""Задание
1. Найти все простые циклы в графе.
2. Проверить, является ли дерево симметричным.
3. Определить, является ли граф деревом.
4. Найти диаметр дерева.
5.* Написать свой класс для работы с графом."""


# 1 пункт задания.
# Пустой граф
g = nx.Graph()

# Узлы графа
g.add_nodes_from([1, 2, 3, 4, 5])

# Связи узлов графа
g.add_edges_from([(1, 2), (2, 3), (3, 1), (3, 4), (4, 5), (5, 3)])

# Находит циклы в графе
print(nx.cycle_basis(g))


# 1, 4 и 5* пункт задания.
class TreeNode:
    """Конструктор реализации дерева"""
    def __init__(self, val=0, left=None, right=None):

        # Вершина дерева
        self.val = val

        # Левая сторона дерева
        self.left = left

        # Левая сторона дерева
        self.right = right


# Функция принимает корень дерева
def is_mirror(root):
    """Принимает корень дерева и выполняет функцию рекурсии двух сторон дерева"""
    return check_halves(root.left, root.right)


def check_halves(left, right):
    """Рекурсивный обход двух половин дерева"""
    if not left and not right:
        return 'Дерево симметрично'
    if left and right:
        if left.val == right.val:
            left_side = check_halves(left.left, right.right)
            right_side = check_halves(left.right, right.left)
            return left_side and right_side
    return 'Дерево не симметрично'


def get_diameter(root, diameter):
    """Определяет диаметр дерева"""

    # Если дерево пустое
    if root is None:
        return 0, diameter

    # высота левого и правого поддеревьев
    left_height, diameter = get_diameter(root.left, diameter)
    right_height, diameter = get_diameter(root.right, diameter)

    # расчет диаметра текущего узла
    max_diameter = left_height + right_height + 1

    # максимальный диаметр
    diameter = max(diameter, max_diameter)

    # высота поддерева с корнем в текущем узле
    return max(left_height, right_height) + 1, diameter


def diameter_tree(root):
    """Выводит итоговый диаметр дерева"""
    diameter = 0
    return get_diameter(root, diameter)[1]


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.right.right = TreeNode(3)
print(is_mirror(tree))
print('Диаметр дерева -', diameter_tree(tree))

# 3 пункт задания.
g = nx.Graph()
g.add_nodes_from([1, 2, 3, 4, 5])
g.add_edges_from([(1, 2), (2, 3), (2, 4), (1, 4)])
cycle = nx.cycle_basis(g)

# Если в графе есть цикл значит это граф. Если нету - дерево.
if cycle:
    print('Это граф')
else:
    print('Это дерево')

