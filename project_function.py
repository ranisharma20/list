def atm_hindi():
    global pin
    global banking
    print("apka swagtat hai")
    print("ab apna card dale ")
    print("apni banking darg kare:\n1.nikalna\n2.jma kre\n3.jach kre:")
    banking=input("vikalp chuniy=")
    pin=int(input("apna pin number lickhe ="))
    atm=50000
    if pin==9625:
        if banking=="3":
            print(atm)
        elif banking=='1':
            a=int(input('rashi darj kare shesh rashi nikale ='))
            remaining=atm-a
            print(remaining)
        elif banking=="2":
            a=int(input('jma rashi darj kare ='))
            total_amount=atm+a
            print(total_amount)
        else:
            print('chodna')
    else:
        print('pin glth hai')
    print('🙏 bank ko istemaal krne k leay dhneya baad 🙏')
def atm_english():
    
    print("welcome bank of india")
    print("enter your card")
    lang=input('enter your lang=hindi /english  =')
    if lang=="hindi":
        atm_hindi()
    if lang=="english":
        print("1.withdraw \n2.deposit \n3.balance equiry\n 4.quit  englis:")
        banking=input("choose option=")
        atm=50000
        pin=int(input("please enter your pin ="))
        if pin==9625:
            if banking=="3":
                print(atm)
            elif banking=='1':
                a=int(input('enter amount withdraw balance  ='))
                remaining=atm-a
                print(remaining)
            elif banking=="2":
                a=int(input('enter amount deposit  ='))
                total_amount=atm+a
                print(total_amount)
            else:
                print('quit')
        else:
            print('pin is wrong')
        print('🙏 Thankyou for using banking 🙏')
atm_english()