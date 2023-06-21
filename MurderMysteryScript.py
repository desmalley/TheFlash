
def dotterisor(role,name):
    line_length=50
    role_length=len(role)
    name_length=len(name)
    dot_length=50-(role_length+name_length)
    dot="."
    repeated_dot=dot*dot_length
    cast_line=role+repeated_dot+name
    print(cast_line)
    return cast_line
dotterisor("Director","Audrey Richards")
 