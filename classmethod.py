class MyClass:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1

    @classmethod
    def create_instance(cls, data):
        instance = cls()
        instance.data = data
        return instance

instance = MyClass.create_instance("some data")
MyClass.increment_count()
print(instance.count)