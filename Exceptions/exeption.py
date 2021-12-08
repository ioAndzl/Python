import os


def raise_exception(a):
    try:
        return a/0
    except Exception as e:
        print(f'The following error occured :{e}')
    else:
        print('else')
    finally:
        print('finally')    


if __name__=='__main__':
    print('there')
    raise_exception(2)