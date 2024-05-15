# f = open("C:/Users/abc/Downloads/python .txt","r")
# data = f.read()
# print(data)
# f.close()

# f = open("C:/Users/abc/Downloads/python .txt","a")
# data = f.write("\nI want to learn Machine Learning \nAfter that AI")
# f.close()

# with open("C:/Users/abc/Downloads/python .txt","a") as f:
#     data = f.write("\nI am a data analyst")
#     f.close()


# with open("C:/Users/abc/Downloads/python .txt","r") as f:
#     f.read()

# import os
#
# os.remove("C:/Users/abc/Downloads/python  - Copy.txt")


# with open("practice.txt","a") as f:
#     f.write("\nwe are learning File i/o \nusing python \nI like programming in python")

with open("practice.txt","r") as f:
    data = f.read()

    new = data.replace("python","java")
    print(new)

    with open("practice.txt", "w") as f:
        data = f.write(new)





