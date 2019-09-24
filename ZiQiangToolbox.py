print('''Welcome to use Tony's tool box given by Nick Fury!
I'd like to introduce to you proudly that this tool box has three fantastic functions!
The first one is to encode or decode using base64 method
The second one is to create a dictionary via keys and values given here, print JavaScript Object Notation, and provide a new dictionary with opposite connections
The third one is to create a QRCode jpg via txt given to desktop
So tell me which one would you like to use?(1,2,3)''');
fact = input()
if fact == '1':
    print('U want to encode or decode?(1=encode,2=decode)'),
    fxc=input()
    if fxc == '1':
        OCode= bytes(input("Please type what U wanna encode here:"),encoding="UTF-8")
        import base64
        Encode = base64.b64encode(OCode)
        print("The base64 str encoded is", str(Encode,'UTF-8'))
    elif fxc == '2':
        try:
            TCode= bytes(input("Please type what U wanna dncode here:"),encoding="UTF-8")
            import base64
            Decode = base64.b64decode(TCode)
            print("The base64 str decoded is", str(Decode,'UTF-8'))
        except:
            print("It seems that you didn't give me the correct things")
    else:
        print('You just made a mistake! 1 OR 2 PLEASE! Run again!')


elif fact == "2":
        try:
            Dic = {}
            print("Tell me what U wanna make as a dictionary\n")
            t = 0
            while t != "1":
                print("Key:")
                key = input()
                print("Value:")
                value = input()
                Dic[key]=value
                print("Another one? If not, type 1")
                t=input()
            print("The Original Dic is",Dic)
            import json
            J = json.dumps(Dic)
            print("JavaScript Object Notation made from the Dictionary is")
            print(J), print("The type of it is,",type(J))
            ADic = dict(zip(Dic.values(),Dic.keys()))
            print("The new Dictionary which the value is the old key and the key for the old value is")
            print(ADic),print("with type",type(ADic))
        except:
            print("There is something wrong! Check what U have typed!")


elif fact == '3':
    try:
        import qrcode
        print('Type where the txt U wanna give me here, location please'),
        fxe = input()
        f = open(fxe,'r',encoding='UTF-8')
        fc = f.read()
        f.close()
        print("This is what will be encoded to a QRCode,",fc)
        img = qrcode.make(fc)
        img.save('Target.jpg')
    except:
        print("There are something that I can't understand...")
else:
    print("Please check what U typed. Only 1,2,3 will lead to the functions")
