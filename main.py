
#Interactive mode function. Does the proper operation.

def interactiveMode():
    instruction = input("Please enter the instruction: \n ") #Takes the instruction
    instruction = instruction.split(" ") #Split it to be able to work easily
    # The first string of instruction is operation, this line checks if it is valid or not
    valid_Operation = checkOperation(instruction[0])

    # If operation is not valid, ask user to give proper instruction
    while (not valid_Operation) :
        instruction = input("Please enter correct instruction: \n ")
        instruction = instruction.split(" ")  # Split it to be able to work easily
        # The first string of instruction is operation, this line checks if it is valid or not
        valid_Operation = checkOperation(instruction[0])

    if (valid_Operation): #If operation is valid:
        binaryRepresentation = setTheInstructionType(instruction) #Gets the binary representation of the instruction
    
        if(binaryRepresentation!=("!"*32)): #Checks whether given binary representation is valid or not
            hexaRepresentation = convertToHex(binaryRepresentation)
            print("Hexadecimal representation is: 0x",hexaRepresentation, "\n")  # print the result
            print("Binary representation is: ",binaryRepresentation)



#This function takes the binary and converts it into hexa
def convertToHex(binaryRepresentation):
    #Dict type for matching binary-hexa
    lookup = {"0000":"0","0001":"1","0010":"2","0011":"3","0100":"4","0101":"5", "0110":"6","0111":"7","1000":"8",
              "1001":"9", "1010":"A", "1011":"B", "1100":"C", "1101":"D", "1110":"E", "1111":"F"}

    result = ""
    #The loop for converting binary
    for i in range(0,32,4):
        temp=binaryRepresentation[i:i+4] #Takes the first 4 bit of the binary
        result+=lookup[temp] #Check the dicts and add to result
    return result

#This function checks if the operation is valid or not
def checkOperation(instruction):
    file = open('lookuptable.txt','r');
    table = file.read()
    table=table.split("\n") #Split the string, so each line will be a operation
    valid=0

    #Loops checks if the operation is in de table
    for i in range(len(table)):
        if(instruction == table[i]):
             valid=1 #If it is in the table, it is valid.
    file.close()
    if (valid==1):
         return True
    return False

#This function does the converting instruction into binary by checking the instruction
def setTheInstructionType(instruction):
    if instruction[0]=="add":
        #The code below splits the instruction to be able to make easier operation on it
        splittedInstruction = instruction[0] + " " + instruction[1] + " " + instruction[2] + " "+instruction[3]
        splittedInstruction = splittedInstruction.replace(",","")
        splittedInstruction = splittedInstruction.split(" ")

        #If it is add operation, this means it is R-type. Assign the proper values.
        #While assigning values into registers convert the instruction into binary
        rd = convertRegToBinary(splittedInstruction[1])
        rs = convertRegToBinary(splittedInstruction[2])
        rt = convertRegToBinary(splittedInstruction[3])
        opcode = "000000"
        shamt= "00000"
        funct = "100000"
        if(rd!=1 and rs!=1 and rt!=1):
            return opcode+rs+rt+rd+shamt+funct
        return "!"*32

    elif  instruction[0]=="sub":
        # The code below splits the instruction to be able to make easier operation on it
        splittedInstruction = instruction[0] + " " + instruction[1] + " " + instruction[2] + " " + instruction[3]
        splittedInstruction = splittedInstruction.replace(",", "")
        splittedInstruction = splittedInstruction.split(" ")
        # If it is sub operation, this means it is R-type. Assign the proper values.
        # While assigning values into registers convert the instruction into binary
        rd = convertRegToBinary(splittedInstruction[1])
        rs = convertRegToBinary(splittedInstruction[2])
        rt = convertRegToBinary(splittedInstruction[3])
        opcode = "000000"
        shamt = "00000"
        funct = "100110"
        if (rd != 1 and rs != 1 and rt != 1):
            return opcode + rs + rt + rd + shamt + funct
        return "!" * 32

    elif instruction[0] == "slt":
        # The code below splits the instruction to be able to make easier operation on it
        splittedInstruction = instruction[0] + " " + instruction[1] + " " + instruction[2] + " " + instruction[3]
        splittedInstruction = splittedInstruction.replace(",", "")
        splittedInstruction = splittedInstruction.split(" ")
        # If it is slt operation, this means it is R-type. Assign the proper values.
        # While assigning values into registers convert the instruction into binary
        rd = convertRegToBinary( splittedInstruction[1])
        rs = convertRegToBinary( splittedInstruction[2])
        rt = convertRegToBinary( splittedInstruction[3])
        opcode = "000000"
        shamt = "00000"
        funct = "101010"

        if (rd != 1 and rs != 1 and rt != 1):
            return opcode + rs + rt + rd + shamt + funct
        return "!" * 32


    elif instruction[0] == "sw":
        # The code below manipulates the instruction to be able to make easier operation on it
        splittedInstruction = instruction[0] + " " + instruction[1] + " " + instruction[2]
        splittedInstruction = splittedInstruction.replace("("," ")
        splittedInstruction = splittedInstruction.replace(")"," ")
        splittedInstruction = splittedInstruction.replace(",", "")
        splittedInstruction = splittedInstruction.split(" ")
        #The operation is sw, means that the instruciton in I-type. Assign the proper values.
        # While assigning values into registers convert the instruction into binary
        rt = convertRegToBinary(splittedInstruction[1])
        SixteenBitNumber = splittedInstruction[2]
        rs = convertRegToBinary(splittedInstruction[3])
        SixteenBitNumber = makeBinary(int(SixteenBitNumber)) #Convert SixteenBitNumber into binary by making it 16bit
        opcode = "101011"
        return opcode + rs + rt + SixteenBitNumber
    elif instruction[0] == "lw":
        # The code below manipulates the instruction to be able to make easier operation on it
        splittedInstruction = instruction[0] + " " + instruction[1] + " " + instruction[2]
        splittedInstruction = splittedInstruction.replace("("," ")
        splittedInstruction = splittedInstruction.replace(")"," ")
        splittedInstruction = splittedInstruction.replace(",", "")
        splittedInstruction = splittedInstruction.split(" ")
        # The operation is lw, means that the instruciton in I-type. Assign the proper values.
        # While assigning values into registers convert the instruction into binary
        rt = convertRegToBinary(splittedInstruction[1])
        SixteenBitNumber = splittedInstruction[2] #Convert SixteenBitNumber into binary by making it 16bit
        rs = convertRegToBinary(splittedInstruction[3])
        SixteenBitNumber = makeBinary(int(SixteenBitNumber))
        opcode = "100011"
        return opcode + rs + rt + SixteenBitNumber

    elif instruction[0] == "jr":
        #No proper manipulation on the instruction needed. First string is the operation, second is the adress.
        rs = convertRegToBinary(instruction[1])
        opcode="000000"
        funct = "001000"
        return opcode + rs + "00000"+"00000"+"00000" + funct #rt,rd,shamt = "00000", totally 32 bit

    elif instruction[0] == "move":
        # The code below manipulates the instruction to be able to make easier operation on it
        splittedInstruction = instruction[0] + " " + instruction[1] + " " + instruction[2]
        splittedInstruction = splittedInstruction.replace(",", "")
        splittedInstruction = splittedInstruction.split(" ")
        # The operation is move, means that the instruciton in R-type. Assign the proper values.
        # While assigning values into registers convert the instruction into binary
        # It is actually adding 0 to the register, basically it is add instruction.
        rt = convertRegToBinary(splittedInstruction[1])
        rd = "00000"
        shamt ="00000"
        rs = convertRegToBinary(splittedInstruction[2])
        opcode= "001000"
        return opcode + rs + rt + rd +shamt+"000000";

    elif instruction[0] == "addi":
        # The code below manipulates the instruction to be able to make easier operation on it
        splittedInstruction = instruction[0] + " " + instruction[1] + " " + instruction[2] + " " + instruction[3]
        splittedInstruction = splittedInstruction.replace(",", "")
        splittedInstruction = splittedInstruction.split(" ")
        # The operation is addi, means that the instruciton in I-type. Assign the proper values.
        # While assigning values into registers convert the instruction into binary
        rt = convertRegToBinary(splittedInstruction[1])
        rs = convertRegToBinary(splittedInstruction[2])
        SixteenBitNumber = splittedInstruction[3]; #Convert SixteenBitNumber into binary by making it 16bit

        if SixteenBitNumber[0] == "-": #If it is negative
            positiveSixteenBit = SixteenBitNumber.replace("-","") #First manipulate string,remove the sign
            twosComplement= 65535 - int(positiveSixteenBit) +1 #Then take two's complement of data
            twosComplement = makeBinary(twosComplement) #Convert it to binary
            SixteenBitNumber = twosComplement
        else:
            SixteenBitNumber = makeBinary(int(SixteenBitNumber))

        opcode="001000"
        return opcode+rs+rt+SixteenBitNumber

    elif  instruction[0]=="slti":
        # The code below manipulates the instruction to be able to make easier operation on it
        splittedInstruction = instruction[0] + " " + instruction[1] + " " + instruction[2] + " " + instruction[3]
        splittedInstruction = splittedInstruction.replace(",", "")
        splittedInstruction = splittedInstruction.split(" ")
        # The operation is slti, means that the instruciton in I-type. Assign the proper values.
        # While assigning values into registers convert the instruction into binary
        rt = convertRegToBinary(splittedInstruction[1])
        rs = convertRegToBinary(splittedInstruction[2])
        SixteenBitNumber = splittedInstruction[3]; #Convert SixteenBitNumber into binary by making it 16bit

        if SixteenBitNumber[0] == "-": #If it is negative
            positiveSixteenBit = SixteenBitNumber.replace("-", "") #First manipulate string,remove the sign
            twosComplement = 65535 - int(positiveSixteenBit) + 1 #Then take two's complement of data
            twosComplement = makeBinary(twosComplement) #Convert it to binary
            SixteenBitNumber = twosComplement
        else:
            SixteenBitNumber = makeBinary(int(SixteenBitNumber))

        opcode = "001010"
        return opcode + rs + rt + SixteenBitNumber

    elif  instruction[0] == "sll":
        # The code below manipulates the instruction to be able to make easier operation on it
        splittedInstruction = instruction[0] + " " + instruction[1] + " " + instruction[2] + " " + instruction[3]
        splittedInstruction = splittedInstruction.replace(",", "")
        splittedInstruction = splittedInstruction.split(" ")
        # The operation is sll, means that the instruciton in R-type. Assign the proper values.
        # While assigning values into registers convert the instruction into binary
        rd = convertRegToBinary(splittedInstruction[1])
        rt=convertRegToBinary(splittedInstruction[2])
        shamt=int(splittedInstruction[3])
        shamt = bin(shamt)[2:]
        shamt = (5 - len(shamt)) * "0" + shamt  # Complete it to 5 bits
        opcode = "000000"
        rs = "00000"
        funct ="000000"
        return opcode+rs+rt+rd+shamt+funct

    elif instruction[0] == "beq":
        # The code below manipulates the instruction to be able to make easier operation on it
        splittedInstruction = instruction[0] + " " + instruction[1] + " " + instruction[2] + " " + instruction[3] + " "+ instruction[4]
        splittedInstruction = splittedInstruction.replace(",", "")
        splittedInstruction = splittedInstruction.split(" ")
        # The operation is beq, means that the instruciton in I-type. Assign the proper values.
        # While assigning values into registers convert the instruction into binary
        rs = convertRegToBinary(splittedInstruction[1])
        rt = convertRegToBinary(splittedInstruction[2])
        label = splittedInstruction[3]
        #position is the variable for detecting the adress of the target
        position=detectLabels(label)
        dif = int(position)-int(splittedInstruction[4])

        if dif>=0:
            dif=makeBinary(dif)
        else: #if it is negative, take two's complement and make it binary
            dif = 65535 - int(dif) + 1
            dif=makeBinary(dif)
        opcode = "000100"

        return opcode + rs + rt +  dif

    elif instruction[0] == "bne":
        # The code below manipulates the instruction to be able to make easier operation on it
        splittedInstruction = instruction[0] + " " + instruction[1] + " " + instruction[2] + " " + instruction[3] + " " + instruction[4]
        splittedInstruction = splittedInstruction.replace(",", "")
        splittedInstruction = splittedInstruction.split(" ")
        # The operation is bne, means that the instruciton in I-type. Assign the proper values.
        # While assigning values into registers convert the instruction into binary
        rs = convertRegToBinary(splittedInstruction[1])
        rt = convertRegToBinary(splittedInstruction[2])
        label = splittedInstruction[3]
        # position is the variable for detecting the adress of the target
        position = detectLabels(label)
        dif = int(position)-int(splittedInstruction[4])

        if dif >= 0:
            dif=makeBinary(dif)
        else: #if it is negative, take two's complement and make it binary
            dif = 65535 - int(dif) + 1
            dif = makeBinary(dif)
        opcode = "000101"

        return opcode + rs + rt + dif


    elif instruction[0] == "jal":
        # The code below manipulates the instruction to be able to make easier operation on it
        splittedInstruction = instruction[0] + " " + instruction[1]
        splittedInstruction = splittedInstruction.replace(",", "")
        splittedInstruction = splittedInstruction.split(" ")

        label = splittedInstruction[1]
        # position is the variable for detecting the adress of the target
        position = detectLabels(label)
        position=makeBinary(position)
        position = 10*"0"+position
        opcode = "000011"
        return opcode + position

    elif instruction[0] == "j":
        splittedInstruction = instruction[0] + " " + instruction[1]
        splittedInstruction = splittedInstruction.replace(",", "")
        splittedInstruction = splittedInstruction.split(" ")

        label = splittedInstruction[1]
        position = detectLabels(label)
        position = makeBinary(position)
        position = 10 * "0" + position
        opcode = "000010"
        return opcode + position


    else:
        print(instruction)
        print("No operation is found. Please try again.")
        return "!"*32


#This function converts 16-bit adress into binary and make them 16-bit
def makeBinary(number):
    number = bin(number)
    number = number[2:] #Take after the 2 string to getting the just binary part
    extendTheNumber = 16-len(number) #determine the bit size of the number
    number=str(number)
    #Add the 0 for making it 16 bit
    for i in range(extendTheNumber):
        number= "0"+number
    
    return number


#This function converts registers into binary
def convertRegToBinary(register):
    if register=="$zero":
        return "00000"
    elif register=="$at":
        return "00001"
    elif register=="$v0":
        return "00010"
    elif register=="$v1":
        return "00011"
    elif register=="$a0":
        return "00100"
    elif register=="$a1":
        return "00101"
    elif register=="$a2":
        return "00110"
    elif register=="$a3":
        return "00111"
    elif register=="$t0":
        return "01000"
    elif register=="$t1":
        return "01001"
    elif register=="$t2":
        return "01010"
    elif register=="$t3":
        return "01011"
    elif register=="$t4":
        return "01100"
    elif register=="$t5":
        return "01101"
    elif register=="$t6":
        return "01110"
    elif register=="$t7":
        return "01111"
    elif register=="$s0":
        return "10000"
    elif register=="$s1":
        return "10001"
    elif register=="$s2":
        return "10010"
    elif register=="$s3":
        return "10011"
    elif register=="$s4":
        return "10100"
    elif register=="$s5":
        return "10101"
    elif register=="$s6":
        return "10110"
    elif register=="$s7":
        return "10111"
    elif register=="$t8":
        return "11000"
    elif register=="$t9":
        return "111001"
    elif register=="$k0":
        return "11010"
    elif register=="$k1":
        return "11011"
    elif register=="$gp":
        return "11100"
    elif register=="$sp":
        return "11101"
    elif register=="$fp":
        return "11110"
    elif register=="$ra":
        return "11111"
    else:
        print("Register is not found")
        print("\n")
        print(register)
        return 0

#This function takes the label and detects the adress of it
def detectLabels(label):
    file = open('input.src', 'r');
    table = file.read()
    table = table.split("\n")

    positionOfLabel=-1
    #This loop read the input table
    for i in range(len(table)):
        split = table[i].split(":") #Split them from the ":" sign, that means there is a label
        if(label==split[0]): #If they are match
            positionOfLabel = i
            break

    return positionOfLabel

#This function is for batch mode
def batchMode():
    #Reading file for getting input, writing file for the output
    reading_file = open('input.src', 'r')
    writing_file = open('output.obj', 'a')
    #Read the file and split it line by line
    code = reading_file.read()
    code = code.split("\n")
    #This loop traverse line by line and does it instructions
    for i in range(len(code)):
        if ":" in code[i]: #That means there is a label, act according to that
            code[i] = getRidOfComments(code[i]) #Get rid of comments
            #Take the instruction and split it for doing easier operations
            instruction = code[i]
            instruction = instruction.split(" ")
            valid_Operation = checkOperation(instruction[0]) #Check whether it is valid or not
        else:
            code[i]=getRidOfComments(code[i])
            instruction = code[i]
            valid_Operation= checkOperation(instruction[0])
        instruction.insert(4,str(i+1)) #Insert 4'th value as adress of the instructions
        if(valid_Operation): #If operation is valid
            print(instruction)
            binaryRepresentation = setTheInstructionType(instruction) #Convert it to binary
            hexadecimal=convertToHex(binaryRepresentation)
            print("Binary representation is: ", binaryRepresentation, "\n")
            print("Hexadecimal representation is: 0X",hexadecimal,"\n")
            writing_file.write("0X"+hexadecimal + "\n") #Write to output file
    writing_file.close()
    reading_file.close()

#This function for deleting the comment part of the instruction
def getRidOfComments(code):

    if ":" in code:
        x = code.split(":", 1)[1]
        x= x.split("#")[0]

    else:
        x = code.split("#")[0].split(" ")

    return x

# Gets the input for Interactive or Batch mode
print("Enter the mode that you want to work. ")
mode_selection = input("Interactive Mode(1) \nBatch Mode(2) ")

#Loop for entering the valid selection

while True:
    if(mode_selection=='1'): #If selection is 1 -> Interactive mode opens
        print("Interactive Mode is chosen.")
        interactiveMode()
        break
    elif(mode_selection =='2'):  #If selection is 2 -> Batch mode opens
        print("Batch Mode is chosen")
        batchMode()
        break
    else: # If the selection is not valid, try again!
        print("Wrong choice, try again! ")
        mode_selection = input("Interactive Mode(1) \nBatch Mode(2) ")

