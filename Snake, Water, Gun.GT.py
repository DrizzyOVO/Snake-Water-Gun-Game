# import random
#
# i = 0
# while (i<=9):
#     i = i + 1
#     cms = 0
#     mms = 0
#
#     lst = ["snake", "water", "gun"]
#     cm = random.choice(lst)
#
#     mm = input("\n Enter 's' for Snake, 'w' for Water, 'g' for Gun")
#     if mm == "s":
#         if cm == "snake":
#             print("comp's snake v/s your snake", "\n It's a tie")
#             cms = cms + 0
#             mms = mms + 0
#         elif cm == "water":
#             print("comp's water v/s your", mm, "\n you win")
#             cms = cms + 0
#             mms = mms + 1
#         elif cm == "gun":
#             print("comp's gun v/s your", mm, "\n comp wins")
#             cms = cms + 1
#             mms = mms + 0
#
#     elif mm == "w":
#         if cm == "water":
#             print("comp's water v/s your water", "\n It's a tie")
#             cms = cms + 0
#             mms = mms + 0
#         elif cm == "snake":
#             print("comp's snake v/s your water", "\n comp wins")
#             cms = cms + 1
#             mms = mms + 0
#         elif cm == "gun":
#             print("comp's gun vs your water", "\n you win")
#             cms = cms + 0
#             mms = mms + 1
#
#     elif mm == "g":
#         if cm == "gun":
#             print("comp's gun v/s your gun", "\n It's a tie")
#             cms = cms + 0
#             mms = mms + 0
#         elif cm == "snake":
#             print("comp's snake v/s your gun", "\n you win")
#             cms = cms + 0
#             mms = mms + 1
#         elif cm == "water":
#             print("comp's water v/s your gun", "\n comp wins")
#             cms = cms + 1
#             mms = mms + 0
#
#     else:
#         print("Type either 's', 'w' or 'g'")
#         continue
#
#
#     if i == 10:
#         if int(cms) > int(mms):
#             print("\n UNFORTUNATELY:-(", "\n THE COMP WINS THIS GAME")
#         elif int(cms) < int(mms):
#             print("\n CONGRATULATIONS!!!!!!! YOU WIN THE GAME", "\n WINNER WINNER CHICKEN DINNER")
#     else:
#         continue










