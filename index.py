from string import Template

str_templ = Template("${name} chased squirrels at the ${place}")

str1 = str_templ.substitute(name="Luna", place="park")
print(str1)

# Since the substition uses keyword arguments, we can pass in a dictionary instead

data = {
    "name": "Luna",
    "place":  "park"
}

str2 = str_templ.substitute(data)
print(str2)
