names = ["lawrence", 'akinyemi', "tofunmi", "opeyemi", "jerry"]
ages = [20,22,24,26,28]
countries=["nigeria","ghana", "egypt","england", "france"]
allowed_countries = ("italy", "kenya","togo", "brazil", "france")
 
# Conditional statements
if countries[-1] in allowed_countries:
    print(f"{names[-1]} is from an allowed country")
else:
    print(f"{names[-1]} is not from an allowed country")
 
# Summary
total_people = len(names)
allowed_count = sum(1 for country in countries if country in allowed_countries)
not_allowed_count = total_people - allowed_count

print(f"\nSummary")
print(f"Total number of people checked: {total_people}")
print(f"Number of people from allowed countries: {allowed_count}")
print(f"Number of people not from allowed countries: {not_allowed_count}")
 