value = 10
print("In the global scope, value has been set to:", value, "\n")
read_global()
    print("Back in the global scope, value is still:", value, "\n")
shadow_global()
print("Back in the global scope, value is still:", value, "\n")
change_global()
print("back in the global scope, value has now changed to: ", value, "\n")

