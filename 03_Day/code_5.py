# Dictionary => key:value pair => mutable, unordered => {}

info = {
    "Name" : "Anshu",
    "CGPA" : 8.68,
    "Sub" : ["Maths, Science"]
}

info["Name"] = "Modi"
# print(info)

# print(type(info))
# print(info["Name"])

print(info.keys())
print(info.values())
print(info.items())
print(info.get("CGPA"))     # key daalo value milega

info.update({
    "City" : "Patna"
})
print(info)



# sets => collection of unique elements 
# s = {1,1,1,2}

# to create empty set
empty_s = set()
print(type(empty_s))

# s.add(10)
s.remove(10)

# print(type(s))
# print(s)
# print(len(s))