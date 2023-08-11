class User:

    def __init__(self, first_name, last_name,email, age, is_reward_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = is_reward_member
        self.gold_card_points = gold_card_points

    def display_info(self):
        print('============================================')
        print('First Name:', self.first_name)
        print('Last Name:', self.last_name)
        print('Email:', self.email)
        print('Age:', self.age)
        print('Reward Member:', self.is_reward_member)
        print('Gold Card Points:', self.gold_card_points)
        print('============================================')

    def enrollment(self):    
        if self.is_reward_member:
            print('User already a member')
            return False
        else:
            self.is_reward_member = True
            self.gold_card_points = 200
            return True

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print('Not enough Gold card points')
        else:
            self.gold_card_points -= amount

person = User('Ryan', 'Kai', 'thisismyemail@yahoo.com', 21)
person1 = User('Chris', 'Johnson', 'myemail@gmail.com', 30)
person.enrollment()
person.enrollment()
person1.enrollment()
person.spend_points(50)
person1.spend_points(100)
person.display_info()
person1.display_info()