"""Vector module"""

class Vector:
    """Class Vector"""
    vector = []
    name = ""

    def __init__(self, vector, name=""):
        """Constructor

        @param param vector: a list
        @param param name: the name you want for the
        vector
        """
        self.vector = vector
        self.name = name
    
    def set_name(self, name):
        """Assigns a name
        
        @param param name: A string
        @raise TypeError if name isn't a string
        """
        if type(name) is not str:
            raise TypeError("El nombre debe de ser una string")

        self.name = name
    
    def create_vector(self):
        """Fills the vector with user input"""

        for i in range(4):
            element = float(input(f"Elemento [{i+1}]: "))
            self.vector.append(element)

        self.print_vector()

    def validate_vector(self):
        """Validates if vector isn't a Zero vector

        @param param vector: an array []
        @returns false if is a zero-vector and if not true
        """

        zero_counter = 0
        flag = bool
        for element in self.vector:
            if element == 0:
                zero_counter += 1

        flag = False if zero_counter == len(self.vector) else True

        return flag

    def multiply_vectors(self, vector):
        """Multiply matrix times vector or vector w/vector
        
        @param param vector: an array []
        """
        for i in range(len(self.vector[0])):
            for j in range(len(self.vector)):
                self.vector[i] += self.vector[i][j] * vector[j]

    def minus_vector(self, vector):
        """Reduces two vectors
        
        @param param vector: an array []
        @returns a Vector Object
        """
        temp_vector = []

        for i in range(len(self.vector)):
            temp_vector.append(self.vector[i] - vector.vector[i])

        return Vector(temp_vector)

    def print_vector(self):
        """Prints the elements of the Vector"""
        print(f"Vector {self.name}:", end=" ")
        print("|", end=" ")
        for element in self.vector:
            print(f"{element}", end=" ")

        print("|")