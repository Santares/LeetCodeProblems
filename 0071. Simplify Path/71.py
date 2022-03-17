class Solution:
    def simplifyPath(self, path: str) -> str:
        # level = 0
        # res = ""
        stack = ["/"]
        temp = []
        for c in path:
            if c == "/":
                name = "".join(temp)
                temp = []

                if name == "":
                    pass
                elif name == "/":
                    stack.append(name)
                elif name == ".":
                    pass
                elif name == "..":
                    if len(stack) < 2:
                        pass
                    elif len(stack) == 2:
                        stack.pop()
                        # stack.pop()
                    else:
                        stack.pop()
                        stack.pop()
                else:
                    stack.append(name)
                    stack.append("/")

            else:
                temp.append(c)

        if temp:
            name = "".join(temp)
            if name == "/":
                pass
            elif name == ".":
                pass
            elif name == "..":
                if len(stack) < 3:
                    # stack.pop()
                    pass
                else:
                    stack.pop()
                    stack.pop()
            else:
                stack.append(name)

        if len(stack) > 1 and stack[-1] == "/":
            stack.pop()

        return "".join(stack)

    # online solutiion
    def simplifyPath2(self, path: str) -> str:
        dirs = path.split("/")
        ans = ""
        skip = 0
        for d in reversed(dirs):
            if d == "." or d == "":
                continue

            if d == "..":
                skip += 1
                continue

            if skip == 0:
                ans = d + "/" + ans
            else:
                skip -= 1

        return "/" + ans[:-1]

    #online solution
    def simplifyPath3(self, path: str) -> str:

        s = []

        for d in path.split("/"):
            if d != "." and d:
                if d == "..":
                    if s: s.pop(-1)
                else:
                    s.append(f"/{d}")

        return "".join(s) if s else "/"
