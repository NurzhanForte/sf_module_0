def game_core_v4(number):
    count = 0
    predict = np.random.randint(1,100) # генерируем случ число
    if number > predict: 
        x = number // predict 
        predict = predict * x
    elif number < predict: 
        x = predict // number
        predict = predict / x
    while number != predict: #условие выхода
        count+=1 #счетчик
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    print('otvet = ', predict)        
    return(count) # выход из цикла, если угадали