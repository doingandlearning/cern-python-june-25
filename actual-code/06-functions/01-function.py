def print_msg(message, line_length=25, organisation="CERN"):
    print(message)
    print(f"- brought to you by {organisation}")
    print("-" * line_length)

print_msg("Lunch is in 25 minutes.", 25)
print_msg("Lunch is in 25 minutes.", 100)
# print_msg("Lunch is in 25 minutes.", 0)
print_msg("Lunch is in 20 minutes", 25, "BBC")
print_msg("Live long and prosper", organisation="Star Trek")
print_msg(organisation="Mandalorians", message="This is the way")
