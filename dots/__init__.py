

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class DotCollection:
    def __init__(self, dots):
        self.dots = dots

    def is_on_same_line(self):
        dot_len = len(self.dots)
        # 1 or 0 dots is not a line
        if dot_len < 2:
            return False
        # 2 dots is always a line
        if dot_len == 2:
            return True

        # find function to describe line between first two dots
        dot1 = self.dots[0]
        dot2 = self.dots[1]

        # is line vertical?
        if dot1.x == dot2.x:
            for dot in self.dots[2:]:
                if dot1.x != dot.x:
                    return False
            return True
            
        # determine coefficient
        try:
            c = (dot1.y - dot2.y) / (dot1.x - dot2.x)
        except ZeroDivisionError:
            c = 0    

        # determine y-intercept
        b = dot1.y - dot1.x * c

        # make sure other dots are on this line
        for dot in self.dots[2:]:
            if dot.x * c + b != dot.y:
                return False

        return True

