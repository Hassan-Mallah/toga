from unittest import TestCase
from unittest.mock import Mock

from toga.sources import SimpleListSource, ListSource


class ListSourceTests(TestCase):
    def test_init_with_tuple(self):
        "A ListSource can be instantiated from tuples"
        source = ListSource(
            data=[
                ('first', 111),
                ('second', 222),
                ('third', 333),
            ],
            accessors=['val1', 'val2']
        )

        self.assertEqual(len(source), 3)

        self.assertEqual(source[0].val1, 'first')
        self.assertEqual(source[0].val2, 111)

        self.assertEqual(source[1].val1, 'second')
        self.assertEqual(source[1].val2, 222)

        listener = Mock()
        source.add_listener(listener)

        # Set element 1
        source[1] = ('new element', 999)

        self.assertEqual(len(source), 3)

        self.assertEqual(source[1].val1, 'new element')
        self.assertEqual(source[1].val2, 999)

        listener.data_changed.assert_called_once_with()

    def test_init_with_list(self):
        "A ListSource can be instantiated from lists"
        source = ListSource(
            data=[
                ['first', 111],
                ['second', 222],
                ['third', 333],
            ],
            accessors=['val1', 'val2']
        )

        self.assertEqual(len(source), 3)

        self.assertEqual(source[0].val1, 'first')
        self.assertEqual(source[0].val2, 111)

        self.assertEqual(source[1].val1, 'second')
        self.assertEqual(source[1].val2, 222)

        listener = Mock()
        source.add_listener(listener)

        # Set element 1
        source[1] = ['new element', 999]

        self.assertEqual(len(source), 3)

        self.assertEqual(source[1].val1, 'new element')
        self.assertEqual(source[1].val2, 999)

        listener.data_changed.assert_called_once_with()

    def test_init_with_dict(self):
        "A ListSource can be instantiated from dicts"
        source = ListSource(
            data=[
                {'val1': 'first', 'val2': 111},
                {'val1': 'second', 'val2': 222},
                {'val1': 'third', 'val2': 333},
            ],
            accessors=['val1', 'val2']
        )

        self.assertEqual(len(source), 3)

        self.assertEqual(source[0].val1, 'first')
        self.assertEqual(source[0].val2, 111)

        self.assertEqual(source[1].val1, 'second')
        self.assertEqual(source[1].val2, 222)

        listener = Mock()
        source.add_listener(listener)

        # Set element 1
        source[1] = {'val1': 'new element', 'val2': 999}

        self.assertEqual(len(source), 3)

        self.assertEqual(source[1].val1, 'new element')
        self.assertEqual(source[1].val2, 999)

        listener.data_changed.assert_called_once_with()

    def test_iter(self):
        "A list source can be iterated over"
        source = ListSource(
            data=[
                {'val1': 'first', 'val2': 111},
                {'val1': 'second', 'val2': 222},
                {'val1': 'third', 'val2': 333},
            ],
            accessors=['val1', 'val2']
        )

        self.assertEqual(len(source), 3)

        result = 0
        for row in source:
            result += row.val2

        self.assertEqual(result, 666)

    def test_clear(self):
        "A list source can be cleared"
        source = ListSource(
            data=[
                {'val1': 'first', 'val2': 111},
                {'val1': 'second', 'val2': 222},
                {'val1': 'third', 'val2': 333},
            ],
            accessors=['val1', 'val2']
        )

        self.assertEqual(len(source), 3)

        listener = Mock()
        source.add_listener(listener)

        # Clear the list
        source.clear()
        self.assertEqual(len(source), 0)

        listener.data_changed.assert_called_once_with()

    def test_insert_kwarg(self):
        "You can insert into a list source using kwargs"
        source = ListSource(
            data=[
                {'val1': 'first', 'val2': 111},
                {'val1': 'second', 'val2': 222},
                {'val1': 'third', 'val2': 333},
            ],
            accessors=['val1', 'val2']
        )

        self.assertEqual(len(source), 3)

        listener = Mock()
        source.add_listener(listener)

        # Insert the new element
        row = source.insert(1, val1='new element', val2=999)

        self.assertEqual(len(source), 4)
        self.assertEqual(source[1], row)
        self.assertEqual(row.val1, 'new element')
        self.assertEqual(row.val2, 999)

        listener.data_changed.assert_called_once_with()

    def test_insert(self):
        "You can insert into a list source using positional args"
        source = ListSource(
            data=[
                {'val1': 'first', 'val2': 111},
                {'val1': 'second', 'val2': 222},
                {'val1': 'third', 'val2': 333},
            ],
            accessors=['val1', 'val2']
        )

        self.assertEqual(len(source), 3)

        listener = Mock()
        source.add_listener(listener)

        # Insert the new element
        row = source.insert(1, 'new element', 999)

        self.assertEqual(len(source), 4)
        self.assertEqual(source[1], row)
        self.assertEqual(row.val1, 'new element')
        self.assertEqual(row.val2, 999)

        listener.data_changed.assert_called_once_with()

    def test_prepend_kwarg(self):
        "You can prepend to a list source using kwargs"
        source = ListSource(
            data=[
                {'val1': 'first', 'val2': 111},
                {'val1': 'second', 'val2': 222},
                {'val1': 'third', 'val2': 333},
            ],
            accessors=['val1', 'val2']
        )

        self.assertEqual(len(source), 3)

        listener = Mock()
        source.add_listener(listener)

        # Insert the new element
        row = source.prepend(val1='new element', val2=999)

        self.assertEqual(len(source), 4)
        self.assertEqual(source[0], row)
        self.assertEqual(row.val1, 'new element')
        self.assertEqual(row.val2, 999)

        listener.data_changed.assert_called_once_with()

    def test_prepend(self):
        "You can prepend to a list source using positional args"
        source = ListSource(
            data=[
                {'val1': 'first', 'val2': 111},
                {'val1': 'second', 'val2': 222},
                {'val1': 'third', 'val2': 333},
            ],
            accessors=['val1', 'val2']
        )

        self.assertEqual(len(source), 3)

        listener = Mock()
        source.add_listener(listener)

        # Prepend the new element
        row = source.prepend('new element', 999)

        self.assertEqual(len(source), 4)
        self.assertEqual(source[0], row)
        self.assertEqual(row.val1, 'new element')
        self.assertEqual(row.val2, 999)

        listener.data_changed.assert_called_once_with()

    def test_append_kwarg(self):
        "You can append to a list source using kwargs"
        source = ListSource(
            data=[
                {'val1': 'first', 'val2': 111},
                {'val1': 'second', 'val2': 222},
                {'val1': 'third', 'val2': 333},
            ],
            accessors=['val1', 'val2']
        )

        self.assertEqual(len(source), 3)

        listener = Mock()
        source.add_listener(listener)

        # Append the new element
        row = source.append(val1='new element', val2=999)

        self.assertEqual(len(source), 4)
        self.assertEqual(source[3], row)
        self.assertEqual(row.val1, 'new element')
        self.assertEqual(row.val2, 999)

        listener.data_changed.assert_called_once_with()

    def test_append(self):
        "You can append to a list source using positional args"
        source = ListSource(
            data=[
                {'val1': 'first', 'val2': 111},
                {'val1': 'second', 'val2': 222},
                {'val1': 'third', 'val2': 333},
            ],
            accessors=['val1', 'val2']
        )

        self.assertEqual(len(source), 3)

        listener = Mock()
        source.add_listener(listener)

        # Append the new element
        row = source.append('new element', 999)

        self.assertEqual(len(source), 4)
        self.assertEqual(source[3], row)
        self.assertEqual(row.val1, 'new element')
        self.assertEqual(row.val2, 999)

        listener.data_changed.assert_called_once_with()

    def test_remove(self):
        "You can remove an item from a list source"
        source = ListSource(
            data=[
                {'val1': 'first', 'val2': 111},
                {'val1': 'second', 'val2': 222},
                {'val1': 'third', 'val2': 333},
            ],
            accessors=['val1', 'val2']
        )

        self.assertEqual(len(source), 3)

        listener = Mock()
        source.add_listener(listener)

        # Remove the second element
        source.remove(source[1])

        self.assertEqual(len(source), 2)
        self.assertEqual(source[0].val1, 'first')
        self.assertEqual(source[0].val2, 111)

        self.assertEqual(source[1].val1, 'third')
        self.assertEqual(source[1].val2, 333)

        listener.data_changed.assert_called_once_with()


class SimpleListSourceTests(TestCase):
    def test_init_dict(self):
        "A SimpleListSource can be instantiated with dicts"
        source = SimpleListSource(
            data=[
                {'val1': 'first', 'val2': 111, 'icon': 'path/to/first.png'},
                {'val1': 'second', 'val2': 222},
                {'val1': 'third', 'val2': 333},
            ]
        )

        self.assertEqual(len(source), 3)

        self.assertEqual(source[0].val1, 'first')
        self.assertEqual(source[0].val2, 111)
        self.assertEqual(source[0].icon.path, 'path/to/first.png')

        self.assertEqual(source[1].val1, 'second')
        self.assertEqual(source[1].val2, 222)

        listener = Mock()
        source.add_listener(listener)

        # Set element 1
        source[1] = {'val1': 'new element', 'val2': 999}

        self.assertEqual(len(source), 3)

        self.assertEqual(source[1].val1, 'new element')
        self.assertEqual(source[1].val2, 999)

        listener.data_changed.assert_called_once_with()

    def test_init_non_dict(self):
        "A SimpleListSource can be instantiated with non-dict values"
        source = SimpleListSource(
            data=[
                ['first', 111],
                ['second', 222],
                ['third', 333],
            ]
        )

        self.assertEqual(len(source), 3)

        self.assertEqual(source[0].value, ['first', 111])
        self.assertEqual(source[1].value, ['second', 222])

        listener = Mock()
        source.add_listener(listener)

        # Set element 1
        source[1] = ['new element', 999]

        self.assertEqual(len(source), 3)
        self.assertEqual(source[1].value, ['new element', 999])

        listener.data_changed.assert_called_once_with()
