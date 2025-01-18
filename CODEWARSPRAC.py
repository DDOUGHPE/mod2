# string = 'reverse this'[::-1]
# print(string)

# year = 1785
# year_bd = [int(x) for x in str(year)]
# year_bd[0:2]
# print(year_bd[0:2])

# def happy_birthday():
#     return print('you are old')

# happy_birthday()

def expanded_form(num):
    num = str(num)
    st =''
    for j, i in enumerate(num):
        if i != "0":
            st += " + {}{}".format(i, len(num[j+1:])*"0")
    return st.strip(' +')

print(expanded_form(5487))