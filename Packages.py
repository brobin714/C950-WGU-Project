# Brandon Robinson - 006868740
# Packages.py
# C950 Assessment
#
# Packages class holds data related to individual classes


# Creating a package class to group the data
class Packages:
    # O(1) constant
    def __init__(self, p_id, address, city, state, zipcode, deadline, weight, notes, status, depart, arrive):
        self.p_id = p_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.depart = depart
        self.arrive = arrive

    # set_status() - sets package status at the specific point in time provided
    ## Necessary for ad hoc status setting during time package status queries
    ## The statuses are somewhat redundant since the package is still loaded onto the truck.
    ## I'm designating "at hub" to mean not currently en route or already delivered.
    # O(N) linear
    def set_status(self, cur_time):
        if self.arrive < cur_time:
            self.status = 'Delivered'
        elif self.depart < cur_time:
            self.status = 'En Route'
        else:
            self.status = 'At hub'

    def __str__(self):
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s' % (self.p_id, self.address, self.city, self.state, self.zipcode, self.deadline, self.weight, self.notes, self.status, self.depart, self.arrive)
