
print "Which script do you wants to run."
print "1.student_to_teacher"
print "2.battleship"
print "3.exam_stats"
#choice=""
choice=raw_input("Enter your choice a/b/c")
print choice
if choice=="a":
     import students_to_teacher

elif choice=="b":
    import battleship
elif choice=="c":
    import exam_stats
else :
    print "Wrong choice. please again enter the correct choice"
