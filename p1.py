import datetime 

print('hello world')

# strings
message1 = 'Let us have a drink tonight.'
print(message1)

message2 = 'I/m looking for somesome to share in an advanture'
print(message2)

message3 = 'The phrase "Beam me up, Scotty" was never said on Star Trek.'
print(message3)

message4 = """One of my favorite lines from The Godfather is:
"I'am going to make him an offer he can't refuse."
do you know who said this?"""
print(message4)


# Types of numbers: int, float, complex
# operations: + - * /
# do not dive by 0

a = 8 / 2
print(a)

# Boolean values: True, False

now = datetime.datetime.today()
print(now)

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30,22,27, 0)
print(launch_date)
print(launch_time)
print(launch_datetime)

A = datetime.date(2000, 12, 8)
print(A)
print(A.strftime("%A, %B, %d, %Y"))

message ="A was born on {:%A, %B, %d, %Y}."
print(message.format(A))
