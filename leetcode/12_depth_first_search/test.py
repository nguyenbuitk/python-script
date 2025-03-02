class Example:
    def recursive_function(self, n, counter):
        if n == 0:
            return counter
        counter += 1
        return self.recursive_function(n - 1, counter)

example = Example()
result = example.recursive_function(5,0)
print("Result: ", result)