"""python simple game, works well on python2"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import pandas as pd


def verify_cell_availabality(x_cor, y_cor, mat):
    """is cell available or not"""
    if mat[x_cor - 1][y_cor - 1] != '_':
        return 0
    return 1


def is_all_cells_filled_but_no_win(mat):
    """function name discribe funcationality"""
    for itr1 in mat:
        for itr2 in itr1:
            if itr2 == '_':
                return 0
    return 1


def is_xy_valid(x_cor, y_cor):
    """entered xy is valid or not"""
    if x_cor <= 3 and x_cor >= 1 and y_cor <= 3 and y_cor >= 1:
        return 1
    return 0


def win(mat):
    """checking the win scinario"""
    for row_itr in range(0, 3):
        if mat[row_itr][0] == mat[row_itr][1] and mat[row_itr][1] \
                == mat[row_itr][2] and mat[row_itr][0] != '_':
            return 1
    for col_itr in range(0, 3):
        if mat[0][col_itr] == mat[1][col_itr] and mat[1][col_itr] \
                == mat[2][col_itr] and mat[0][col_itr] != '_':
            return 1

    if mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2] and mat[1][1] \
            != '_':
        return 1

    if mat[0][2] == mat[1][1] and mat[1][1] == mat[2][0] and mat[1][1] \
            != '_':
        return 1

    return 0


def print_current_status(mat):
    """printing the current game"""
    matrix = \
        """
   1    2    3
  _______________
1|    |    |    |
 |_%s__|_%s__|_%s__|
2|    |    |    |
 |_%s__|_%s__|_%s__|
3|    |    |    |
 |_%s__|_%s__|_%s__|""" \
        % (
            mat[0][0],
            mat[0][1],
            mat[0][2],
            mat[1][0],
            mat[1][1],
            mat[1][2],
            mat[2][0],
            mat[2][1],
            mat[2][2],
        )
    print matrix


def rules():
    """rules of the game"""
    rules_vaiable = \
        """            ****************************************

            Game by Naveen Ranwa
            Player-1 is set as 0
            Player-2 is set as 1
            (x,y) co-ordinates are from x=1,2,3 and y=1,2,3

            ****************************************
            """
    print rules_vaiable


def validate_user(num):
    """validating the user credentials"""
    is_user_exist = 0
    print 'Enter userName of player %s:' % num
    usr_name = raw_input()
    print 'Enter password of player %s:' % num
    password = raw_input()
    user_database = pd.read_csv('/home/kpit/Desktop/database.csv', ',')

    # print(user_database.iat[0, 1])

    for (index, rows) in user_database.iterrows():
        if rows.iat[4] == usr_name:
            is_user_exist = 1
            if user_database.password[index] == password:
                return (1, rows.iat[0], rows.iat[4], rows.iat[5])
    if is_user_exist == 1:
        print 'Invalid username or password, try play_again'
    else:
        print "User Doesn't exist, try again"
    return (0, 0, 0)


def is_username_exist(user_name):
    """cheking user registered or not"""
    user_database = pd.read_csv('/home/kpit/Desktop/database.csv', ',')

    # print(user_database.iat[0, 1])

    for (index, _) in user_database.iterrows():
        if user_database.username[index] == user_name:
            return 1
    return 0


def is_email_exist(email):
    """checking the mail id exist"""
    user_database = pd.read_csv('/home/kpit/Desktop/database.csv', ',')

    # print(user_database.iat[0, 1])

    for (index, _) in user_database.iterrows():
        if user_database.mailID[index] == email:
            return 1
    return 0


def user_reg():
    """this register new user"""
    user_name = raw_input('Enter username: ')
    while is_username_exist(user_name):
        user_name = raw_input('Username already exist, enter new: ')

    password = raw_input('Enter the password: ')
    first_name = raw_input('Enter your first name: ')
    last_name = raw_input('Enter your Last name: ')
    email = raw_input('Enter the mail ID: ')
    while is_email_exist(email):
        email = raw_input('email already exist, enter new: ')

    new_list = [{
        'username': user_name,
        'password': password,
        'mailID': email,
        'First_name': first_name,
        'Last_name': last_name,
        'wins': 0,
    }]
    new_df = pd.DataFrame(new_list)
    new_df.to_csv(
        '/home/kpit/Desktop/database.csv',
        mode='a',
        encoding='utf-8',
        sep=',',
        index=False,
        header=False,
    )
    print 'Successfully registered'
    return


def pass_rest():
    """password register"""
    user_database = pd.read_csv('/home/kpit/Desktop/database.csv', ',')
    email = raw_input('Enter emailID to rest password:  ')
    if is_email_exist(email):
        for (index, rows) in user_database.iterrows():
            if user_database.mailID[index] == email:
                print(rows.iat[4], rows.iat[3])
                return
    else:
        print "email id doesn't exist"
    return


def update_wins(username):
    """updating the wins in database"""
    user_database = pd.read_csv('/home/kpit/Desktop/database.csv', ',')

    # print(user_database.iat[0, 1])

    for (index, rows) in user_database.iterrows():
        if rows.iat[4] == username:
            rows.iat[5] = int(rows.iat[5]) + 1
            user_database.wins[index] = rows.iat[5]

            # print(user_database)

            user_database.to_csv(
                '/home/kpit/Desktop/database.csv',
                mode='w',
                encoding='utf-8',
                sep=',',
                index=False,
                header=True,
            )
            return 1
    return 0


def choice1():
    """choice 1 i.e. signin and play"""
    user1 = validate_user('1')

    # print('hey')

    while user1[0] == 0:
        user1 = validate_user('1')
    user2 = validate_user('2')
    while user2[0] == 0 or user2[2] == user1[2]:
        if user2[2] == user1[2]:
            print "Same user can't login two times!!!"
        user2 = validate_user('2')
    play_again = 'Y'

    player1 = user1[1]
    player2 = user2[1]
    print 'Please wait loding the game....'
    time.sleep(3)
    while play_again == 'Y' and user2[0] == 1 and user1[0] == 1:
        mat = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        last_player = 0
        rules()

        print_current_status(mat)
        while win(mat) == 0 and is_all_cells_filled_but_no_win(mat) \
                == 0:
            if last_player == 0:
                current_player = player1
            else:
                current_player = player2
            print '%s Enter x cordinate:' % current_player
            x_cor = input()
            print '%s Enter y cordinate:' % current_player
            y_cor = input()
            if is_xy_valid(x_cor, y_cor) == 1:
                if verify_cell_availabality(x_cor, y_cor, mat) == 1:
                    mat[x_cor - 1][y_cor - 1] = last_player
                    last_player = last_player + 1
                    last_player = last_player % 2
                else:
                    print '********************'
                    print 'Cell already filled'
                    print '********************'
                    continue
            else:
                print '********************'
                print 'Invalid co-ordinates'
                print '********************'
                continue
            print_current_status(mat)
            play_again = check_for_win(mat, last_player, user1, user2)


def check_for_win(mat, last_player, user1, user2):
    """checking if someone won the game"""
    play_again = 'Y'
    if win(mat) == 1:
        if last_player == 0:
            update_wins(user2[2])
            print '********************'
            print '%s wins the game' % user2[1]
            print '********************'
        else:
            update_wins(user1[2])
            print '********************'
            print '%s wins the game' % user1[1]
            print '********************'
        print 'Do you want to play again? (Y/N)'
        play_again = raw_input()
    elif is_all_cells_filled_but_no_win(mat) == 1:
        print 'oops no one wins, game full'
        print 'Do you want to play again? (Y/N)'
        play_again = raw_input()
    return play_again


def main():
    """main function"""
    choice = raw_input('Login: 1, Signup: 2, ForgotPass: 3, Total wins: 4 -> ')

    if choice == '1':
        choice1()
    elif choice == '2':

        user_reg()
    elif choice == '3':
        pass_rest()
    elif choice == '4':
        valid = validate_user('')
        while valid[0] == 0:
            valid = validate_user(' ')
        print 'wait fetching data...'
        time.sleep(3)

        print 'Total no. wins so far: %s' % valid[3]
    else:
        print 'Invalid choice'
    return


if __name__ == '__main__':
    main()
