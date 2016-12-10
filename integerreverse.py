  def reverse_string(self,string):

        string = list(string)

        start = 0 

        end = len(string) -1

        while(start <= end):

            tmp = string[start]

            string[start] = string[end]

            string[end] = tmp

        

        return "".join(string)

    

    def reverse(self, x):

        pos = 1

        if x < 0:

            pos = 0

            x = -x

        num = str(x)

        

        num = self.reverse_string(num)

        

        x = int(num)

        

        if not pos:

            x = -x

        

        return x
