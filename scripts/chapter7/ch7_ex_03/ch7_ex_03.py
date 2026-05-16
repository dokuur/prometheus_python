fname = input("Please, enter a file name: ")
count = 0

if fname == 'la la la bla bla bla':
    print(f'{fname} for you - It\'s a prank!'.upper())
    exit()

try:
    ofnm = open(fname)
except:
    print(f'File {fname} can\'t be openned or file doesn\'t exist.')
    exit()



for line in ofnm:
    count += 1

print("Total line number is:",count)
