class BinaryHeap:
    def __init__(self):
        self._heap = []

    def insert(self, item):
        # import ipdb;ipdb.set_trace()
        self._heap.append(item)
        cur_idx = (len(self._heap) - 1)
        while (cur_idx - 1) // 2 >= 0:
            parent_idx = (cur_idx - 1) // 2
            if self._heap[cur_idx] < self._heap[parent_idx]:
                self._heap[cur_idx], self._heap[parent_idx] = (
                    self._heap[parent_idx],
                    self._heap[cur_idx],
                )
            cur_idx = parent_idx

    def delete(self):
        import ipdb;ipdb.set_trace()
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        result = self._heap.pop()
        cur_idx = 0
        while 2 * cur_idx + 1 < len(self._heap):
            if 2 * cur_idx + 2 > len(self._heap) - 1:
                min_child_idx = 2 * cur_idx + 1
            elif self._heap[2 * cur_idx + 1] < self._heap[2 * cur_idx + 2]\
                    :
                min_child_idx = 2 * cur_idx + 1
            else:
                min_child_idx = 2 * cur_idx + 2
            if self._heap[cur_idx] > self._heap[min_child_idx]:
                self._heap[cur_idx], self._heap[min_child_idx] = (
                    self._heap[min_child_idx],
                    self._heap[cur_idx],
                )
            else:
                return result
            cur_idx = min_child_idx
        return result



    def _get_min_child(self, parent_idx):
        if 2 * parent_idx + 2 > len(self._heap) - 1:
            return 2 * parent_idx + 1
        if self._heap[2 * parent_idx + 1] < self._heap[2 * parent_idx + 2]:
            return 2 * parent_idx + 1
        return 2 * parent_idx + 2

    def get_heap(self):
        return self._heap


obj = BinaryHeap()
obj.insert(5)
obj.insert(9)
obj.insert(2)
obj.insert(7)
print(obj.get_heap())
obj.delete()
print(obj.get_heap())
