class user:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"\
                first name: {self.first_name}\n\
                last name: {self.last_name}\n\
                email: {self.email}\n\
                age: {self.age}\n\
                member: {str(self.is_rewards_member)}\n\
                points: {self.gold_card_points}\n") 

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            self.is_rewards_member = False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print ("Insufficient Fund")
        else:
            self.gold_card_points = self.gold_card_points - amount

    
user_james = user("james", "young", "jy@eami.com", 34)
user_josh = user("josh", "old", "jo@eami.com", 69)
user_michael = user("michael", "pretty", "mp@eami.com", 18)

user_james.spend_points(50)
user_josh.enroll()
user_josh.spend_points(80)
user_james.display_info()
user_josh.display_info()
user_michael.display_info()
user_josh.enroll()
user_michael.spend_points(40)
user_josh.display_info()
user_josh.enroll()
user_josh.display_info()
