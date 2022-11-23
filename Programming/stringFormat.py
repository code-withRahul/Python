# x="page not found"
# message="The error is "
# print(message + x)

# x=404
# message="The error is {} "
# print(message.format(x))

x=404 
y=200
message="Expected is {} but atual is {} "
print(message.format(x,y))

message="Expected is {1} but atual is {0} "
print(message.format(x,y))
