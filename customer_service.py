import random

#random.seed(0)

class Feedback(object):
    """defines the properties of customers requesting for customer service.
    And their level of satisfaction on service received"""

    def __init__(self, rating, staff = ["zinny", "Glory", "Claire",'Tom','Yung']):
        self.staff = staff
        self.rating = rating

    def customer(self, ):
        client = random.choice([{"name":"Peter", "feature": "angry, rude"}, {"name":"Banks","feature": "sad, withdrawn"},
                       {"name":"Mathew", "feature":"warm, edgy"}, {"name":"Groot", "feature":"nice, decided"}])
        return client['name'], client['feature']
    
    def rate(self):
        """ratings range from six to one. 6 indicating highest satisfaction
        and 1 strong dissatisfaction of service"""
        
        rate = random.choice(range(1,6))
        return rate

    def responder(self):
        """assigns a responder from the staff list"""
        responder = random.choice(self.staff)
        self.staff.remove(responder)
        return responder
    def get_feedback(self):
        customer = self.customer()
        for r in self.rating:
            if customer == r["customer"]:
                r["rating"] = (self.rate()+ r["rating"])/2
                return self.rating
        self.rating.append({"responder":self.responder(), "customer": customer, "rating": self.rate()})
        return self.rating
            


client = random.choice([{"name":"Peter", "feature": "angry, rude"}, {"name":"Banks","feature": "sad, withdrawn"},
                       {"name":"Mathew", "feature":"warm, edgy"}, {"name":"Groot", "feature":"nice, decided"}])
rating = [{"responder": "claire", "customer": "none", "rating": 0}]
    
feedback = Feedback(rating)


    
for i in range(1000):
    feedback.get_feedback()



    




        
