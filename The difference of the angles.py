def what_is_a_quarter(angel):
    # print('the received angel ' + str(angel) + ' deg')
    if 0 <= angel < 90:
        print('The angel in the 1 quarter' + ' ' + '(' + str(angel) + ' ' + 'deg' + ')')
        return angel
    elif 90 <= angel < 180:
        print('The angel in the 2 quarter' + ' ' + '(' + str(angel) + ' ' + 'deg' + ')')
        return angel
    elif 180 <= angel < 270:
        print('The angel in the 3 quarter' + ' ' + '(' + str(angel) + ' ' + 'deg' + ')')
        return angel
    else:
        print('The angel in the 4 quarter' + ' ' + '(' + str(angel) + ' ' + 'deg' + ')')
        return angel


def decrease(angel):
    print('The angle is more than 360 degrees (is:  ' + str(angel) + ')')
    angel_old = angel
    while angel > 360:
        angel = angel - 360

    print('The angle of ' + str(angel_old) + ' degrees corresponds to an angle of ' + str(angel) + ' degrees')
    return angel


def increase(angel):
    print('The angle is less than 0 degrees (is:  ' + str(angel) + ')')
    angel_old = angel
    while angel < 0:
        angel = angel + 360
    print('The angle of ' + str(angel_old) + ' degrees corresponds to an angle of ' + str(angel) + ' degrees')
    return angel


def distribution(angel):
    if 0 <= angel <= 360:
        return what_is_a_quarter(angel)
    elif angel > 360:
        return what_is_a_quarter(decrease(angel))
    else:
        return what_is_a_quarter(increase(angel))


def diff(angel_1, angel_2):
    values = [distribution(angel_1), distribution(angel_2)]
    diff_1 = max(values) - min(values)
    diff_2 = 360 - diff_1
    if diff_2 < diff_1:
        print('The difference between the angles is ' + str(diff_2) + ' degrees')
    else:
        print('The difference between the angles is ' + str(diff_1) + ' degrees')

angel_1 = int(input("Input any angle to find the difference between it and next one to be inputed: "))
angel_2 = int(input("Input a next one angle: "))
diff(angel_1, angel_2)



