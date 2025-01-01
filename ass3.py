#ques 1
# sa=int(input("Enter the total amount of shopping "))

# if sa>=100:
#       disc=10
#       dis= sa*disc//100
#       nsa=sa-dis
#       print(f"THE TOTAL AMOUNT IS {sa}. AFTER DISCOUNT OF {disc}% the amount to pay is {nsa}")
# else:
#     print(f"the amount is {sa}")

# ques 2
# item = int(input("enter the number of items"))
# amount = 15000
# if item>=5:
#         dis=amount*0.15
#         dicount=amount-dis
#         print(f"The total amount is {dicount}")
# else:
#     print(f"The amount is {amount}")

# ques 3
# price = 10000
# is_member=input("Are you a member (Y/N)").lower()
# if is_member!="y" and is_member!="n":
#                                    print(f"{is_member} is an inappropriate answer")
# else:                                     
#      if is_member=="y":
#                  print(f"you are a member, you will have to pay {price*.80}")
#      else:
#            print(f"you are not a member you will have to pay {price*.95}")  

# ques 4
# price=int(input("enter the total amount? "))
# holiday=input("IS TODAY A HOLIDAY?(Y/N)").lower()
# if holiday!="y" and holiday!="n":
#                                    print(f"{holiday} is an inappropriate answer")
# else:                                     
#      if holiday=="y":
#                  print(f"you are a member, you will have to pay {price*.75}")
#      else:
#            print(f"you are not a member you will have to pay {price*.90}")  

# ques5
# item=int(input("enter the total number of items? "))
# amount=int(input("enter amount"))
# if item%2==0:
#          print(f"The total amount is {amount*0.5}")
# else:
#     print(f"the total amount is {amount}")      

# # ques6
# item=int(input("Enter the total price of the item"))
# luxdis=item*0.15
# stantax=item*0.08
# if item>=500:
          
#             print(f"The price of the item after luxury tax will be {item+luxdis}")
# else:
#      print(f"the price of the item after sandard tax will be {item+stantax}")      
# 
#  ques7
# item=int(input("Enter the total price of the item"))
# luxdis=item*0.20
# stantax=item*0.10
# if item>=50000:
          
#             print(f"The price of the item after luxury tax will be {item+luxdis}")
# else:
#      print(f"the price of the item after sandard tax will be {item+stantax}") 

# ques 8      
# tax= int(input("Enter the income? "))
# if tax>=100000:
#             print("High tax")
# elif 30000<=tax<100000:
#                      print("Medium tax")
# else :
#     print("Low tax")                     

    #  ques 9                   
# item = input("Is thev item essential (Y/N)").lower()
# itemprice= int(input("enter price"))
# if item!="y"  and   item!="n":
#     print("PLEASE TELL WETHER IT IS ESSENTIAL OR NOT")
# else:
#     if item=="y":
#                  print(f"you are a member, you will have to pay {item*.75}")
#     else:
#         print()    

# ques 10
# original_price = float(input("Enter the original price: "))
# tax_free = input("Is today a tax-free day? (yes/no): ").strip().lower() == "yes"

# final_price = calculate_price(original_price, tax_free)
# print(f"The final price is: ${final_price:.2f}")
                    
# ques11
# total_purchase = int(input("the total purchase amount"))
# shipping=5
# if total_purchase>50:
#                  print(f"The total purchase after shipping charges will be ${total_purchase+shipping}")   
# else:
#     print(f"The total amount is ${total_purchase}")     
# 
# ques12
# code="DISCOUNT10"
# AMOUNT= int(input("Enter the amount? "))  
# discount=AMOUNT*0.85
# discountcode=input("Enter discount code? ") 
# if code==discountcode:
#                     print(f"by applying the coupn code your amount is {discount}")
# else:
#     print(f"you've entered the wrong coupon and your amount is {AMOUNT}")                    
# 1. Pass/Fail based on score
# score = int(input("Enter the student's score: "))
# if score >= 40:
#     print("Pass")
# else:
#     print("Fail")

# # 2. Grade Assignment
# if score >= 90:
#     grade = "A"
# elif score >= 75:
#     grade = "B"
# elif score >= 50:
#     grade = "C"
# else:
#     grade = "F"
# print(f"Grade: {grade}")

# # 3. Bonus Marks
# completed_assignments = input("Did the student complete all assignments? (yes/no): ").lower()
# if completed_assignments == "yes":
#     score += 5  # Add bonus marks
#     print("Bonus marks added.")
# else:
#     print("No bonus marks added.")
# print(f"Final Score with Bonus: {score}")

# # 4. Attendance Eligibility
# attendance_percentage = float(input("Enter the student's attendance percentage: "))
# if attendance_percentage >= 75:
#     print("Eligible for the exam.")
# else:
#     print("Not eligible for the exam.")

# # 5. Scholarship Eligibility
# family_income = float(input("Enter the student's family income: "))
# if grade == "A" and family_income < 30000:
#     print("Eligible for scholarship.")
# else:
#     print("Not eligible for scholarship.")
# 13. Tiered Discounts
# def apply_discount(total_price):
#     if total_price <= 50:
#         print("No discount.")
#     elif 50 < total_price <= 100:
#         discount = total_price * 0.10
#         print(f"10% discount applied: -${discount:.2f}")
#         total_price -= discount
#     else:
#         discount = total_price * 0.20
#         print(f"20% discount applied: -${discount:.2f}")
#         total_price -= discount
#     return total_price

# # 14. Minimum Purchase Requirement
# def minimum_purchase(total_price):
#     if total_price < 20:
#         print("Minimum purchase of $20 is required.")
#     else:
#         print(f"Total amount: ${total_price:.2f}")

# # 15. Loyalty Points
# def loyalty_points(is_loyal):
#     if is_loyal:
#         print("Earn double loyalty points.")
#     else:
#         print("Earn standard loyalty points.")

# # D - Travel and Tickets
# # 16. Travel Discount
# def travel_discount(distance, ticket_price):
#     if distance > 500:
#         discount = ticket_price * 0.20
#         print(f"20% travel discount applied: -${discount:.2f}")
#         ticket_price -= discount
#     return ticket_price

# # 17. Child or Senior Discount
# def child_or_senior_discount(age, ticket_price):
#     if age < 12 or age > 60:
#         discount = ticket_price * 0.15
#         print(f"15% child/senior discount applied: -${discount:.2f}")
#         ticket_price -= discount
#     return ticket_price

# # 18. Ticket Type Pricing
# def ticket_type_pricing(is_weekend, ticket_price):
#     if is_weekend:
#         surcharge = ticket_price * 0.10
#         print(f"10% weekend surcharge applied: +${surcharge:.2f}")
#         ticket_price += surcharge
#     return ticket_price

# # 19. Baggage Fee
# def baggage_fee(baggage_weight):
#     if baggage_weight > 20:
#         extra_fee = (baggage_weight - 20) * 10  # $10 per kg over 20kg
#         print(f"Extra baggage fee: +${extra_fee:.2f}")
#         return extra_fee
#     return 0

# # 20. Early Bird Discount
# def early_bird_discount(days_in_advance, ticket_price):
#     if days_in_advance > 30:
#         discount = ticket_price * 0.10
#         print(f"10% early bird discount applied: -${discount:.2f}")
#         ticket_price -= discount
#     return ticket_price

# # Example usage:

# # 13. Apply discount based on total price
# total_price = float(input("Enter the total price: $"))
# total_price = apply_discount(total_price)

# # 14. Minimum purchase check
# minimum_purchase(total_price)

# # 15. Loyalty points check
# is_loyal = input("Is the customer a loyal member? (yes/no): ").lower() == "yes"
# loyalty_points(is_loyal)

# # D - Travel and Tickets
# # 16. Travel discount based on distance
# distance = float(input("Enter the travel distance in miles: "))
# ticket_price = float(input("Enter the ticket price: $"))
# ticket_price = travel_discount(distance, ticket_price)

# # 17. Child or Senior discount based on age
# age = int(input("Enter the passenger's age: "))
# ticket_price = child_or_senior_discount(age, ticket_price)

# # 18. Weekend ticket surcharge
# is_weekend = input("Is it a weekend? (yes/no): ").lower() == "yes"
# ticket_price = ticket_type_pricing(is_weekend, ticket_price)

# # 19. Baggage fee
# baggage_weight = float(input("Enter the baggage weight in kg: "))
# baggage_fee_amount = baggage_fee(baggage_weight)

# # 20. Early bird discount
# days_in_advance = int(input("Enter the number of days the ticket was booked in advance: "))
# ticket_price = early_bird_discount(days_in_advance, ticket_price)

# # Final ticket price after all discounts and fees
# final_price = ticket_price + baggage_fee_amount
# print(f"Final ticket price: ${final_price:.2f}")
