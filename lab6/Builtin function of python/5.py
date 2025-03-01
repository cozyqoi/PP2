def all_true(tpl):
    return all(tpl)

print(all_true((True, True, False)))  # False
print(all_true((1, "hello", 3.14)))   # True 
