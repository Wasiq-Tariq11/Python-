class employee:
    start_time="10am"
    end_time="5pm"

class teacher(employee):
    def __init__(self,subject):
      self.subject=subject

T1=teacher("Maths")
print(T1.subject, T1.end_time)
