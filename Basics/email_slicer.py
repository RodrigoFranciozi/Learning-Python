email = input('Qual o seu email?:').strip()

user_name = email[:email.index("@")]
domain_name = email[email.index("@")+1:]

output = "'Your user name is '{}' and your domain name is '{}'".format(user_name,domain_name)

print(output)