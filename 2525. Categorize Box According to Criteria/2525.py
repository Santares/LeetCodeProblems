class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        B = False
        H = False
        d_limit = 10 ** 4
        v_limit = 10 ** 9
        if length >= d_limit or width >= d_limit or height >= d_limit or length * width * height >= v_limit:
            B = True
        if mass >= 100:
            H = True

        if B and H:
            return "Both"
        elif B:
            return "Bulky"
        elif H:
            return "Heavy"
        else:
            return "Neither"