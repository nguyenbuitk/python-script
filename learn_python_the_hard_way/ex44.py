# Tên biến: dad, child (không viết hoa chữ cái đầu)
# Tên class: Parent, Child (viết hoa chữ đầu)
# Tên hàm: override, implicit, altered (không viết hoa, dùng '_' nếu tên hàm có nhiều từ)


class Parent(object):
    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")
        
class Child(Parent):
    def override(self):
        print("CHILD implicit()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")
        
        
dad = Parent()
child = Child()

dad.implicit()
child.implicit()

dad.override()
child.override()

dad.altered()
child.altered()