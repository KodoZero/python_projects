print("Welcome to my Computer Quiz Game!")

playing = input("Do you want to play? \n")
score = 0

if playing.lower() != "yes":
    quit()

print("Okay! Lets play :)")

answer = input("\n1. What does BIOS stand for? \n")
if answer.lower() == "basic input/output system":
    print('Exactly right!')
    score += 1                                                                       
    print(f"You hold a new score of " + str(score) + '!')
else:
    print("Not quite.")
    print(f"You remain with a score of " + str(score) + '.\n')

answer = input("\n2. What does DHCP stand for? \n")
if answer.lower() == "dynamic host configuration protocol":
    print('Well done!')
    score += 1
    print(f"You hold a new score of " + str(score) + '!')
else:
    print("Try again.")
    print(f"You remain with a score of " + str(score) + '.\n')

answer = input("\n3. What does VPN stand for? \n")
if answer.lower() == "virtual private network":
    print('Spot on!')
    score += 1
    print(f"You hold a new score of " + str(score) + '!')
else:
    print("Incorrect.")
    print(f"You remain with a score of " + str(score) + '.\n')

answer = input("\n4. What does HTTP stand for? \n")
if answer.lower() == "hypertext transfer protocol":
    print('Nice Job!')
    score += 1
    print(f"You hold a new score of " + str(score) + '!')
else:
    print("Oops, thats not it.")
    print(f"You remain with a score of " + str(score) + '.\n')

answer = input("\n5. What does RAID stand for? \n")
if answer.lower() == "redundant array of independent disks":
    print('You got it!')
    score += 1
    print(f"You hold a new score of " + str(score) + '!')
else:
    print("Close, but not correct.")
    print(f"You remain with a score of " + str(score) + '.\n')

answer = input("\n6. What does MFA stand for? \n")
if answer.lower() == "multi-factor authentication":
    print("That's right!")
    score += 1
    print(f"You hold a new score of " + str(score) + '!')
else:
    print("Nope.")
    print(f"You remain with a score of " + str(score) + '.\n')

answer = input("\n7. What does DNS stand for? \n")
if answer.lower() == "domain name system":
    print('Bingo!')
    score += 1
    print(f"You hold a new score of " + str(score) + '!')
else:
    print("Wrong Answer.")
    print(f"You remain with a score of " + str(score) + '.\n')

answer = input("\n8. What does SSL stand for? \n")
if answer.lower() == "secure sockets layer":
    print('Perfect!')
    score += 1
    print(f"You hold a new score of " + str(score) + '!')
else:
    print("Sorry, that's wrong.")
    print(f"You remain with a score of " + str(score) + '.\n')

answer = input("\n9. What does UEFI stand for? \n")
if answer.lower() == "unified extensible firmware interface":
    print('Absolutely!')
    score += 1
    print(f"You hold a new score of " + str(score) + '!')
else:
    print("Nice try, but no.")
    print(f"You remain with a score of " + str(score) + '.\n')

answer = input("\n10. What does UPS stand for? \n")
if answer.lower() == "uninterruptible power supply":
    print('Nailed it!')
    score += 1
    print(f"You currently hold a score of " + str(score) + '!')
else:
    print("That's not right.")
    print(f"You remain with a score of " + str(score) + '.\n')


print(f"\nThank you for playing this short Quiz Game!")
print(f"You have a total score of " + score + '.')
if score != 10:
    print(f"\nTry again for a perfect score? :)")
else:
    print(f"\nWow, a perfect score! You sure are smart. :)")







