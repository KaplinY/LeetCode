class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        x = {}
        for i in range(len(mat)):
            x[i] = sum(mat[i])
        x = dict(sorted(x.items(), key=lambda item: item[1]))
        k_items = list(x)[:k]
        return(k_items)