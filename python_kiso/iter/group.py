class Group:
    def __init__(self):
        self.persons = []
        self.index = 0      # next() が返す要素のインデックス

    def add(self, person):
        self.persons.append(person)
        return self

    def __iter__(self):
        u""" next() メソッドの定義されているイテレータオブジェクトを返す """
        return self

    def next(self):
        u""" コンテナ内の次の要素を返す

        呼出される度に次の要素を返す。
        次の要素がないときは、StopIteration 例外を投げる。
        """
        if self.index >= len(self.persons):
            self.index = 0
            raise StopIteration
        result = self.persons[self.index]
        self.index += 1
        return result
