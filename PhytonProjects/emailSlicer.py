email=input("enter your email id").strip()
username=email[:email.index('@')]
domain=email[email.index('@')+1:]
print('username:',username,'domain:',domain)
