def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        arr = []
        for row in range(m):
            d = []
            for col in range(n):
                d.append(0)
            arr.append(d)
        for i in indices:
            f = i[0]
            s = i[1]
            for x in range(n):
                arr[f][x] += 1
            for y in range(m):
                arr[y][s] += 1  
        counter = 0
        for row in range(m):
            for col in range(n):
                if arr[row][col] %2 != 0:
                    counter += 1
        return counter
