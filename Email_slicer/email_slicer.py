email_id  = input('Enter your email address: ')

id = email_id[:email_id.index('@')]
domain = email_id[email_id.index('@')+1:]

print(f"Your user_id is {id} and your domain name is {domain}")