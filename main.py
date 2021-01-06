#
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#
countt_name1=0
countl_name1=0
t_name1=name1.lower().count("t")
r_name1=name1.lower().count("r")
u_name1=name1.lower().count("u")
e_name1=name1.lower().count("e")
l_name1=name1.lower().count("l")
o_name1=name1.lower().count("o")
v_name1=name1.lower().count("v")
# e
countt_name1= (t_name1+r_name1+u_name1+e_name1)*10
countl_name1= l_name1+o_name1+v_name1+e_name1
countt_name2=0
countl_name2=0
t_name2=name2.lower().count("t")
r_name2=name2.lower().count("r")
u_name2=name2.lower().count("u")
e_name2=name2.lower().count("e")
l_name2=name2.lower().count("l")
o_name2=name2.lower().count("o")
v_name2=name2.lower().count("v")
# e
countt_name2= (t_name2+r_name2+u_name2+e_name2)*10
countl_name2= l_name2+o_name2+v_name2+e_name2
add=countt_name1+countl_name1+countt_name2+countl_name2
if add<10 or add>90:
  print(f"Your score is {add}. You are like mentos and coke.")
elif add>40 or add<50:
  print(f"Your score is {add}. You are all right.")
else:
  print(f"Your score is {add}.")




