import datetime


def validate(func):
    def wrapper(self, *args, **kwargs):
        amount = str(args[0])
        index = amount.index('.')
        if len(amount) - index - 1 > 2:
            print('输入格式有误,小数点后最多保留两位')
        else:
            func(self, *args, **kwargs)
    return wrapper


class Bank(object):
    account_log= []

    def __init__(self, name):
        self.name = name
    @validate
    def deposit(self, amount):
        user.balance += amount
        self.write_log('存入', amount)
    @validate
    def withdrawl(self, amount):
        if amount > user.balance:
            print("余额不足")
        else:
            user.balance -= amount

    def write_log(self, type, amount):
        now = datetime.datetime.now()
        create_time = now.strftime('%Y-%m-%d %H:%M:%S')
        data = [self.name, user.username, create_time, type, amount, f'user.balance:.2f']
        Bank.account_log.append(data)

class ZhaoShang(Bank):
    def __init__(self, name):
        self.name = name

class User(object):
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    def print_log(self):
        print(Bank.account_log)

# bank = Bank('招商银行')

bank = ZhaoShang('招商银行股份有限公司')
user = User('andy', 1000)

def show_menu():
    menu = '''
操作菜单
    0:退出
    1:存款
    2:取款
    3:打印交易信息
    '''
    print(menu)


while True:
    show_menu()
    num = int(input('请根据菜单编号输入'))
    if num == 0:
        print('您已退出系统')
        break
    elif num == 1:
        print('存款')
        amount = float(input('请输入存款金额'))
        bank.deposit(amount)
        print(f'当前余额是{user.balance:.2f}')
    elif num == 2:
        print('取款')
        amount = float(input('请输入存款金额'))
        bank.withdrawl(amount)
        print(f'当前余额是{user.balance:.2f}')
    elif num == 3:
        print('查看记录')
        user.print_log()
    else:
        print('输入有误')

