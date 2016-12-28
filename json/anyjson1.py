import anyjson

print anyjson.serialize(["test", 1, {"foo": 3.14159265}, "bar"])

print anyjson.deserialize("""["test", 1, {"foo": 3.14159265}, "bar"]""")