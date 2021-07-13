question_list = [
    "How many continents are there?",              # pehla question
    "What is the capital of India?",            # doosra question
    "NG mei kaun se course padhaya jaata hai?"    # teesra question
]

options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1] 
print("wlcome to dabar amla  kon bhnega carodpati ")
print("namskar adaab sasiyakal hello ")
print("yeh rha phla parshn apke sreen pr")
i=0
while(i<len(question_list)):
	print(i+1,question_list[i])
	a=0
	while(a<=(len(options_list))):
		print(a+1,options_list[i][a])
		a=a+1
	j=int(input("enter the solution_list"))
	if (j== solution_list[i]):
		print("congress")
	else:
		print("quit")
		#break
	i=i+1