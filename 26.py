pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("케이크를 사라")
else:
    print("케이크를 사지마라")

#문제1
pocket = ['card', 'cash', 'phone']
if 'card' in pocket:
    print("버스를 타고 가라")
else:
    print("걸어가라")

#조건문에서 아무 일도 하지 않게 설정하고 싶다면?
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
