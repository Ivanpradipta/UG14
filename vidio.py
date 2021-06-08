def Password(string):
    import re
    huruf=re.findall('\w',string)
    special=re.findall('\W',string)
    space=re.findall('\s',string)

    if len(space)==0 and len(special)>=1 and len(string)>=6 and len(string)<=20 and len(huruf)>=1:
        print('password kuat')
    elif len(special)==0 or len(huruf)>=1 and len(space)==0 and len(string)>=6 and len (string)<=20:
        print('password lemah')
    elif len(space)>0 and len(special)>=1 and len(string)>=6 and len(string)<=20 and len(huruf)>=1:
        print('password invalid')
    elif len(string)<6 or len(string)>20 and len(space)==o and len(special)>=1 and len(huruf)>=1:
        print('paassword invalid')

pas=str(input('masukkan password:'))
Password(pas)
                       
