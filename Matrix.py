try:
    from fractions import Fraction
    import common_functions as cf
    from common_functions import getList as gL
except ImportError:
    print('A required File is missing, the program will now close')
    exit()
def opr(x,Sign,y):
    if Sign == '+':
        result = x+y
    elif Sign == '-':
        result == x-y
    elif Sign == '/':
        result = x/y
    elif Sign == '*':
        result = x*y
    elif Sign == '**':
        result = x**y
    elif Sign == '$':
        result = x**0.5
    else:
        pass
    return result
operand = {
    "++": lambda x, y: opr(x,'+',y),
    "--": lambda x, y: opr(x,'-',y),
    "/": lambda x, y: opr(x,'/',y),
    "*": lambda x, y: opr(x,'*',y),
    "^": lambda x, y: opr(x,'**',y),
    "P": lambda x, y: perm(x, y),
    "C": lambda x, y: comb(x, y),
    "!": lambda x, y: fact(x),
    "$": lambda x, y: opr(x,'$',y),
    '$$': lambda x, y: y ** (x*.5) 

}
def simplify(expr):
    numxChars = ""
    operation = 'none'
    numyChars = ""
    for char in expr:
        if char.isdigit():
            if operation is 'none':
                numxChars += char
            else:
                numyChars += char
        elif char in operand:
            operation = char
        elif char.isspace():
            pass
        elif char in ('+','-','.'):
            if operation is 'none':
                numxChars += char
            else:
                numyChars += char
        else:
            pass
    if numyChars == "":
        numyChars = 0
        operation = '++'
    else:
        pass
    ans = (operand[operation](float(numxChars), float(numyChars)))
    return ans
#This part Collect the raw input and change them to Numbers for the Matrix Cell
def appendd(V):
    X =[]
    n = len(V.split())
    def iterate(n, V):
        VV = V.split()
        for element in VV:
            if VV.index(element) == n:
                X.append(simplify(element))
                break
            elif element == ' ':
                pass
            else:
                X.append(simplify(element))
        return X
    return iterate(n, V)
def appendds(V):
    X =[]
    n = len(V)
    def iterate(n, V):
        for element in V:
            if V.index(element) == n:
                X.append(simplify(element))
                break
            elif element == ' ':
                pass
            else:
                X.append(simplify(element))
        return X
    return iterate(n, V)
#This function checks if a all items in a list are Unique
def checklist(X):
    value,n = 1,1
    while n < len(X):
        if X[n-1] != X[n]:
            value = 2
            break
        else:
            pass
        n=n+1
    return value
#This function assign and copy the Matrix to another
def matassignment(N,P,Q,X,M):
    global MatA, MatB,MatC,MatD,MatE,MatF,MatG,MatH,MatI,MatZ,matrices,matriceS,matrixSys_list,alpha,matAns,alphB,alphA,MatSys1,MatSys2,MatSys3,MatSys4,MatSys5,MatSys6,MatSys7,MatSys8,MatAns1,MatAns2,MatAns3
    if N == 1:
        if M == 'A':
            MatA = X
        elif M == 'B':
            MatB = X
        elif M == 'C':
            MatC = X
        elif M == 'D':
             MatD = X
        elif M == 'E':
             MatE = X
        elif M == 'F':
             MatF = X
        elif M == 'G':
             MatG = X
        elif M == 'H':
             MatH = X
        elif M == 'I':
             MatI = X
        elif M == 'Z':
            MatZ = X
        else:
             pass
        matrices = [MatA,MatB,MatC,MatD,MatE,MatF,MatG,MatH,MatI,MatZ]
        m = 'Mat'+M
        if m not in matrixlist:
            matrixlist.append(m)
        else:
            pass
    elif N == 2:
        if M == '1':
            MatSys1 = X
        elif M == '2':
            MatSys2 = X
        elif M == '3':
            MatSys3 = X
        elif M == '4':
            MatSys4 = X
        elif M == '5':
            MatSys5 = X
        elif M == '6':
            MatSys6 = X
        elif M == '7':
            MatSys7 = X
        elif M == '8':
            MatSys8 = X
        else:
            pass
        matriceS = [MatSys1,MatSys2,MatSys3,MatSys4,MatSys5,MatSys6,MatSys7,MatSys8]
    elif N == 3:
        XX = get_Mat(P,X)
        if Q == 1:
            if M == 'A':
                MatA = XX
            elif M == 'B':
                MatB = XX
            elif M == 'C':
                MatC = XX
            elif M == 'D':
                 MatD = XX
            elif M == 'E':
                 MatE = XX
            elif M == 'F':
                 MatF = XX
            elif M == 'G':
                 MatG = XX
            elif M == 'H':
                 MatH = XX
            elif M == 'I':
                 MatI = XX
            elif M == 'Z':
                 MatZ = XX
            else:
                 pass
            matrices = [MatA,MatB,MatC,MatD,MatE,MatF,MatG,MatH,MatI,MatZ]
            m = 'Mat'+M
            if m not in matrixlist:
                matrixlist.append(m)
            else:
                pass
        elif Q == 2:
            if M == '1':
                MatSys1 = XX
            elif M == '2':
                MatSys2 = XX
            elif M == '3':
                MatSys3 = XX
            elif M == '4':
                 MatSys4 = XX
            elif M == '5':
                 MatSys5 = XX
            elif M == '6':
                MatSys6 = XX
            elif M == '7':
                MatSys7 = XX
            elif M == '8':
                MatSys8 = XX
            else:
                pass
            matriceS = [MatSys1,MatSys2,MatSys3,MatSys4,MatSys5,MatSys6,MatSys7,MatSys8]
        else:
            if M == '1':
                MatAns1 = XX
            elif M == '2':
                MatAns2 = XX
            elif M == '3':
                MatAns3 = XX
            matAns = [MatAns1,MatAns2,MatAns3]
            m = 'MatAns'+M
            if m not in matrixlist:
                matrixlist.append(m)
            else:
                pass
    else:
        if M == '1':
            MatAns1 = X
        elif M == '2':
            MatAns2 = X
        elif M == '3':
            MatAns3 = X
        matAns = [MatAns1,MatAns2,MatAns3]
        m = 'MatAns'+M
        if m not in matrixlist:
            matrixlist.append(m)
        else:
            pass
#This functions modify the order of a matrix
def mat_reoder(q,m,n,V):
    global matriceS, alphA
    XXX=matriceS[alphA.index(V)];C=[]
    if q == 1:
        del XXX[0]; del XXX[0]
        C.append(m);C.append(n)
        for elements in XXX:
            C.append(elements)
    else:
        C.append(m);C.append(n)
        for elements in XXX:
            C.append(elements)
    matassignment(2,2,0,C,V)
#This function get the value of a Matrix
def get_Mat(q,X):
    global alpha,alphA,alphB,matrices,matAns,matriceS
    if X in alpha:
        XX = matrices[alpha.index(X)]; typ = 1
    elif 'X' in X:
        X = X.replace('X',''); typ = 2
        XX = matAns[alphB.index(X)]
        con=1
    elif 'Ans' in X:
        X = X.replace('Ans',''); typ = 2
        XX = matAns[alphB.index(X)]
        con=1
    elif q != 0 and q > 2:
        XX = matAns[alphB.index(X)]
    else:
        XX = matriceS[alphA.index(X)]; typ = 3
    return XX
#This function creates a new Matrix
def newmat(X):
    XX,t = [],0
    print('Your Matrix is Matrice ' + X + ' Enter the Order of your Matrix: ')
    start = input()
    while start.isalnum() == False:
        start = input('Error, you are to enter in form nxm: ')
    while 'x' not in start:
        start = input('Error, you are to enter in form nxm. E.g 2x2: ')  
    start = start.split('x')
    while t != 0:
        try:
            int(start[1])
            int(start[0])
            t = 0
        except ValueError:
            start = input('You did not enter the Order correctly\n You are to enter in form nxm. E.g 2x2: ')  
            start = start.split('x')
            t = 1
    col = 0
    XX.append(int(start[0]))
    XX.append(int(start[1]))
    row = input('Enter 1st row of the matrix  separated by space: ')
    pasx = 2
    while pasx != 500:
        if len(row.split()) == int(start[1]):
            pasx = 500
        else:
            pass
        check = 2
        while len(row.split()) != int(start[1]):
            print('Error, you are to Enter ' ,int(start[1]),' instead of ',len(row.split()),' values')
            row = input()
            while check != 0:
                try:
                    appendd(row)
                    check = 0;pasx = 500
                except ValueError:
                    print('Error, an unaccepted character is detected, Pls re-enter this row')
                    row = input()
                    check = 5; pasx = 2
            
        while check != 0:
            try:
                appendd(row)
                check = 0
            except ValueError:
                print('Error, an unaccepted character is detected, Pls re-enter this row')
                row = input()
                check = 5; pasx = 3
        row = appendd(row)
        for items in row:
            XX.append(items)
    col = col +1
    while col !=  int(start[0]):
        if col == int(start[0])-1:
            row = input('Good, Almost there, Now Enter the last row: ')
        else:
            row = input('Enter the next row: ')
        pasx = 2
        while pasx != 500:
            if len(row.split()) == int(start[1]):
                pasx = 500
            else:
                pass
            check = 2
            while len(row.split()) != int(start[1]):
                print('Error, you are to Enter ' ,int(start[1]),' instead of ',len(row.split()),' values')
                row = input()
                while check != 0:
                    try:
                        appendd(row)
                        check = 0
                    except ValueError:
                        print('Error, an unaccepted character is detected, Pls re-enter this row')
                        row = input()
                        check = 5; pasx = 2
            while check != 0:
                try:
                    appendd(row)
                    check = 0
                except ValueError:
                    print('Error, an unaccepted character is detected, Pls re-enter this row')
                    row = input()
                    check = 5; pasx = 3
        row = appendd(row)
        for items in row:
            XX.append(items)
        col = col +1
    print('You sucessfully created a new matrix, You can reference by entering ' + X + '\n You can now perform operation on your Matrix, Press 1 for options')
    return tuple(XX)        
#This section check a available matrices for use
def checkMat(X):
    global MatA, MatB,MatC,MatD,MatE,MatF,MatG,MatH,MatI,matrices,matrixlist,matrixSys_list,alpha,matAns,alphB,alphA,CHECKMAT2,CHECKMAT,MatSys1,MatSys2,MatSys3,MatSys4,MatSys5,MatSys6,MatSys7,MatSys8
    matrices,matriceS,matAns = [MatA,MatB,MatC,MatD,MatE,MatF,MatG,MatH,MatI],[MatSys1,MatSys2,MatSys3,MatSys4,MatSys5,MatSys6,MatSys7,MatSys8],[MatAns1,MatAns2,MatAns3]
    nn = 0
    if X == 1:
        print('Checking Matrices')
        while nn < len(matrices):
            if matrices[nn] != []:
                matt = 'Mat'+alpha[nn]
                if matt in matrixlist:
                    pass
                else:
                    matrixlist.append(matt)
                print(matt +' is created already')
            else:
                pass
            nn=nn+1
        nn = 0
        while nn < len(matAns):
            if matAns[nn] != []:
                matt = 'MatAns'+alphB[nn]
                if matt in matrixlist:
                    pass
                else:
                    matrixlist.append(matt)
                print(matt +' is also available')
            else:
                pass
            nn=nn+1
        if len(matrixlist) == 0:
            print('You have no Matrix')
        else:
            pass
        matrices = [MatA,MatB,MatC,MatD,MatE,MatF,MatG,MatH,MatI]
        matAns = [MatAns1,MatAns2,MatAns3]
        return len(matrixlist)
    elif X == 2:
        nn=0
        while nn < len(matriceS):
            if matriceS[nn] != []:
                matt = 'MatSys'+alphA[nn]
                if matt in matrixSys_list:
                    pass
                else:
                    matrixSys_list.append(matt)
            else:
                pass
            nn=nn+1
        x = 'Empty'; nn = 0
        while nn < len(matriceS):
            if matriceS[nn] == []:
                x =alphA[nn]
                break 
            else:
                pass
            nn=nn+1
        matriceS = [MatSys1,MatSys2,MatSys3,MatSys4,MatSys5,MatSys6,MatSys7,MatSys8]
        if x != 'Empty':
            return x
        else:
            CHECKMAT=CHECKMAT+1
            y = CHECKMAT % 8
            x = alphA[y]
            return x
    elif X == 4:
        x = 'Empty';nn=0
        while nn < len(matrices):
            if matrices[nn] == []:
                x = alpha[nn]
                break
            else:
                pass
            nn=nn+1
        if x != 'Empty':
            return x
        else:
            return 'Full'
        matrices = [MatA,MatB,MatC,MatD,MatE,MatF,MatG,MatH,MatI]
        matAns = [MatAns1,MatAns2,MatAns3]
        return len(matrixlist)
    else:
        nn =0
        while nn < len(matAns):
            if matAns[nn] != []:
                matt = 'MatAns'+alphB[nn]
                if matt in matrixAns_list:
                    pass
                else:
                    matrixAns_list.append(matt)
            else:
                pass
            nn = nn+1
        x = 'Empty'; nn =0
        while nn < len(matAns):
            if matAns[nn] == []:
                x = alphB[nn]
                break
            else:
                pass
            nn =nn+1
        if x != 'Empty':
            return x
        else:
            CHECKMAT2=CHECKMAT2+1
            y = CHECKMAT2 % 3
            x = alphB[y]
            return x
#This Matrix assign new Matrices
#It calls the newmaat function
def cr8newmat():
    global MatA, MatB,MatC,MatD,MatE,MatF,MatG,MatH,MatI,matrices,matrixlist,restricted,alpha, restricted
    cv = checkMat(1)
    print('You have ',cv, 'Matrices')
    show = input('Enter 1 to show your Matrices or nil if not interested: ')
    if show == '1':
        print(matrixlist)
    else:
        pass
    print('Do you want to create another Matrix or Edit one of your Matrices? ')
    quest = input('Press\n 1. To Create a New Matrix    2. To Edit one of your Matrices: ')
    if quest == '1':
        for items in matrices:
            if items == []:
                v = matrices.index(items)
                Type = alpha[v]
                MM = newmat(Type)
                if Type == 'A':
                    MatA = MM
                    matrixlist.append('MatA')
                elif Type == 'B':
                    MatB = MM
                    matrixlist.append('MatB')
                elif Type == 'C':
                    MatC = MM
                    matrixlist.append('MatC')
                elif Type == 'D':
                    MatD = MM
                    matrixlist.append('MatD')
                elif Type == 'E':
                    MatE = MM
                    matrixlist.append('MatE')
                elif Type == 'F':
                    MatF = MM
                    matrixlist.append('MatF')
                elif Type == 'G':
                    MatG = MM
                    matrixlist.append('MatG')
                elif Type == 'H':
                    MatH == MM
                    matrixlist.append('MatH')
                elif Type == 'I':
                    MatI = MM
                    matrixlist.append('MatI')
                else:
                    pass
                break
            else:
                pass
    elif quest == '2':
        print(matrixlist)
        shel = input('Enter the number of the Matrix you want to Edit: ')
        p=0
        while p != 5:
            while shel.isdigit() == False:
                shel = input('Error, You are to enter a digit which is the index number of the Matrix you to Edit: ')
            shel = int(shel)
            while shel > len(matrixlist):
                print('Error, the digit you enter is out of range\nYou only have ', len(matrixlist),' matrices so the max integer you can eneter is ',len(matrixlist))
                shel = input()
            shel = int(shel)
            vv = matrixlist[shel-1]
            if vv in restricted:
                print('Sorry, you are restricted from editing that Matrix, Pls choose another: ')
                shel = input()
            elif vv == 'MatZ':
                print('Sorry, that Matrix is reserved for the System, you are not allowed to edit it, Pls choose another: ')
            else:
                p =5
        Type = vv.replace('Mat','')
        MM = newmat(Type)
        matassignment(1,0,0,MM,Type)
#This fuction initialize the matrix data
def matriceint():
    global MatA, matrices, matrixlist
    # Data Input
    MatA,t = [],1
    start = input('To Start press 1 for Menu: ')
    if start == '1':
        print('Press\n 1. Enter Matrix Data    2. Your Matrices: ')
        start = input()
        if start == '1':
            start = input('Your Matrix is Matrix A, Enter the Order of your Matrix: ')
            while start.isalnum() == False:
                 start = input('Error, you are to enter in form nxm: ')
            while 'x' not in start:
                start = input('Error, you are to enter in form nxm. E.g 2x2: ')  
            start = start.split('x')
            while t != 0:
                try:
                    int(start[1])
                    int(start[0])
                    t = 0
                except ValueError:
                    start = input('You did not enter the Order correctly\n You are to enter in form nxm. E.g 2x2: ')  
                    start = start.split('x')
                    t = 1
            col = 0
            MatA.append(int(start[0]))
            MatA.append(int(start[1]))
            row = input('Enter 1st row of the matrix  separated by space: ')
            pasx = 2
            while pasx != 500:
                if len(row.split()) == int(start[1]):
                    pasx = 500
                else:
                    pass
                check = 2
                while len(row.split()) != int(start[1]):
                    print('Error, you are to Enter ' ,int(start[1]),' instead of ',len(row.split()),' values')
                    row = input()
                    while check != 0:
                        try:
                            appendd(row)
                            check = 0
                        except ValueError:
                            print('Error, an unaccepted character is detected, Pls re-enter this row')
                            row = input()
                            check = 5; pasx = 2
                while check != 0:
                    try:
                        appendd(row)
                        check = 0
                    except ValueError:
                        print('Error, an unaccepted character is detected, Pls re-enter this row')
                        row = input()
                        check = 5; pasx = 3
            row = appendd(row)
            for items in row:
                MatA.append(items)
            col = col +1
            while col !=  int(start[0]):
                if col == int(start[0])-1:
                    row = input('Good, Almost there, Now Enter the last row: ')
                else:
                    row = input('Enter the next row: ')
                pasx = 2
                while pasx != 500:
                    if len(row.split()) == int(start[1]):
                        pasx = 500
                    else:
                        pass
                    check = 2
                    while len(row.split()) != int(start[1]):
                        print('Error, you are to Enter ' ,int(start[1]),' instead of ',len(row.split()),' values')
                        row = input()
                        while check != 0:
                            try:
                                appendd(row)
                                check = 0
                            except ValueError:
                                print('Error, an unaccepted character is detected, Pls re-enter this row')
                                row = input()
                                check = 5; pasx = 2
                    while check != 0:
                        try:
                            appendd(row)
                            check = 0
                        except ValueError:
                             print('Error, an unaccepted character is detected, Pls re-enter this row')
                             row = input()
                             check = 5; pasx = 3
                row = appendd(row)
                for items in row:
                    MatA.append(items)
                col = col +1
            matrixlist.append('MatA')
            print('You sucessfully created Matrix A, You can reference by entering A\n You can now perform operation on your Matrix, Press 1 for options')
        else:
            print('Sorry, you have no matrix')
            return matriceint()
    MatA = tuple(MatA)
    matrices = [MatA,MatB,MatC,MatD,MatE,MatF,MatG,MatH,MatI]
#Creates Identity Matrices
def IdentityMat(X):
    Id_Mat = []
    Id_Mat.append(X)
    Id_Mat.append(X)
    row=1
    while row < X+1:
        col = 1
        while col < X +1:
            if col == row:
                Id_Mat.append(1)
            else:
                Id_Mat.append(0)
            col=col+1
        row = row+1
    return Id_Mat
#Creates Diagonal Matrix
def DiagonalMat(X,n):
    Id_Mat = []
    Id_Mat.append(X)
    Id_Mat.append(X)
    row=1
    while row < X+1:
        col = 1
        while col < X +1:
            if col == row:
                Id_Mat.append(n)
            else:
                Id_Mat.append(0)
            col=col+1
        row = row+1
    return Id_Mat
#This function performs row opretaions on a Matrix when called
def rowopr(R,C,X,P1,P2,Sign,XX,Z):
    global MatSys1,MatSys2,MatSys3,MatSys4,MatSys5,MatSys6,MatSys7,MatSys8,matrices,matrixlist,alpha,alphA,matriceS
    matriceS= [MatSys1,MatSys2,MatSys3,MatSys4,MatSys5,MatSys6,MatSys7,MatSys8]
    XXX=matriceS[alphA.index(XX)]
    X1,X2,RR,row=[],[],[],0
    if R == C:
        if R == 1:
            C = XXX[0]
        elif R == XXX[0]:
            C=1
        else:
            C = C-1
    if R<C:
        row,rowl=R-1,C-2
        #This extract the primary row in the matrix
        while row < R:
            col,L = 2+XXX[1]*row,[]
            c=col
            while col < XXX[1]*R + 2:
                X1.append(XXX[c])
                del XXX[c]
                col = col + 1
            row = row + 1
        #This extract the second row in the matrix
        while rowl < C-1:
            col,L = 2+XXX[1]*rowl,[]
            c=col
            while col < XXX[1]*(C-1) + 2:
                if X == 1:
                    X2.append(XXX[c])
                    del XXX[c]
                else:
                    X2.append(XXX[c])
                    c=c+1
                col = col + 1
            rowl = rowl + 1
    else:
        row,rowl=C-1,R-2
        while row < C:
            col,L = 2+XXX[1]*row,[]
            c=col
            while col < XXX[1]*C + 2:
                X1.append(XXX[c])
                del XXX[c]
                col = col + 1
            row = row + 1
        while rowl < R-1:
            col,L = 2+XXX[1]*rowl,[]
            c=col
            while col < XXX[1]*(R-1) + 2:
                if X == 1:
                    X2.append(XXX[c])
                    del XXX[c]
                else:
                    X2.append(XXX[c])
                    c=c+1
                col = col + 1
            rowl = rowl + 1
    RR.append(XXX[0])
    RR.append(XXX[1])
    if X==1:
        r=0
        #Interchanges rows
        if Z == 1:
            print('Interchanging Row ' + str(R) + 'and Row ' + str(C))
        else:
            pass
        if C>R:
            while r < XXX[0]:
                if r == R -1:
                    for items in X2:
                        RR.append(items)
                elif r ==C-1:
                    for items in X1:
                        RR.append(items)
                elif r < R-1:
                    col = 2
                    while col < XXX[1] + 2:
                        RR.append(XXX[col+r*XXX[1]])
                        col = col + 1
                elif r < C-1:
                    col = 2+XXX[1]*(r-1)
                    while col < 2+XXX[1]*r:
                        RR.append(XXX[col])
                        col = col + 1
                else:
                    col = 2
                    while col < 2+XXX[1]:
                        RR.append(XXX[col+(r-2)*XXX[1]])
                        col = col + 1
                r=r+1
        else:
            while r < XXX[0]:
                if r == C -1:
                    for items in X2:
                        RR.append(items)
                elif r ==R-1:
                    for items in X1:
                        RR.append(items)
                elif r < C-1:
                    col = 2
                    while col < XXX[1] + 2:
                        RR.append(XXX[col+r*XXX[1]])
                        col = col + 1
                elif r < R-1:
                    col = 2+XXX[1]*(r-1)
                    while col < 2+XXX[1]*r:
                        RR.append(XXX[col])
                        col = col + 1
                else:
                    col = 2
                    while col < 2+XXX[1]:
                        RR.append(XXX[col+(r-2)*XXX[1]])
                        col = col + 1
                r=r+1
    elif X == 2:
        XF=[]
        if Z == 1:
            #if second row multiplier is 0 it Multiplys the primary row
            #else Add or subtract d rows
            if P2 == 0:
                print('Multiplying Row ' + str(R) + 'by ' + str(P1))
            else:
                print(str(P1)+'('+str(R)+') ' +Sign+ ' '+ str(P2)+'('+str(C)+')')
        else:
            pass
                
        if C<R:
            if Sign=='+':
                r=0
                while r < len(X1):
                    XF.append(P2*X1[r]+P1*X2[r])
                    r=r+1
            elif Sign == '-':
                r=0
                while r < len(X1):
                   XF.append(P1*X2[r]-P2*X1[r])
                   r=r+1
        else:
            if Sign=='+':
                r=0
                while r < len(X1):
                    XF.append(P2*X2[r]+P1*X1[r])
                    r=r+1
            elif Sign == '-':
                r=0
                while r < len(X1):
                   XF.append(P1*X1[r]-P2*X2[r])
                   r=r+1
        r=0
        if R<C:
            while r < XXX[0]:
                if r == R -1:
                    for items in XF:
                        RR.append(items)
                elif r == C -1:
                    for items in X2:
                        RR.append(items)
                elif r < R-1:
                    col = 2
                    while col < XXX[1] + 2:
                        RR.append(XXX[col+r*XXX[1]])
                        col = col + 1
                elif r < C-1:
                    col = 2+XXX[1]*(r-1)
                    while col < 2+XXX[1]*r:
                        RR.append(XXX[col])
                        col = col + 1
                else:
                    col = 2
                    while col < 2+XXX[1]:
                        RR.append(XXX[col+(r-1)*XXX[1]])
                        col = col + 1
                r=r+1
        else:
            while r < XXX[0]:
                if r == R -1:
                    for items in XF:
                        RR.append(items)
                elif r == C -1:
                    for items in X1:
                        RR.append(items)
                elif r < C-1:
                    col = 2
                    while col < XXX[1] + 2:
                        RR.append(XXX[col+r*XXX[1]])
                        col = col + 1
                elif r < R-1:
                    col = 2+XXX[1]*(r-1)
                    while col < 2+XXX[1]*r:
                        RR.append(XXX[col])
                        col = col + 1
                else:
                    col = 2
                    while col < 2+XXX[1]:
                        RR.append(XXX[col+(r-1)*XXX[1]])
                        col = col + 1
                r=r+1
    else:
        pass
    matassignment(2,0,0,RR,XX)
#Finds the determinant of a matrix
def derterminat(X,p):
    XX = get_Mat(0,X)
    if XX[0] == XX[1]:
        if XX[0] == 2:
            return XX[2]*XX[5] - (XX[3] * XX[4])
        else:
            col = 1; M  = [];op = []
            mm=checkMat(2);matassignment(2,0,0,2,mm);mn=checkMat(2);matassignment(2,0,0,2,mn)
            XC = list(XX); XX=tuple(XX);M.append(XC[2]); del XC[2]
            while col < XC[0]:
                M.append(XC[2]*(-1)**col);del XC[2];col+=1
            col= 0; XC = tuple(XC);
            while col < XC[0]:
                row = 0; temp = [];
                XXC1 = list(XC);  vol = 0
                while vol < XX[0]-1:
                    del XXC1[vol*XXC1[0] + col + 2 - vol]; vol+=1
                if len(XXC1) > 6:
                    matassignment(2,0,0,XXC1,mm); mat_reoder(1,XX[0]-1,XX[0]-1,mm)
                    op.append(M[col]*derterminat(mm,1))
                else:
                    matassignment(2,0,0,XXC1,mn); mat_reoder(1,XX[0]-1,XX[0]-1,mn)
                    aneqn = derterminat(mn,1)
                    op.append(M[col]*aneqn)
                col+=1
            te = ''
            return sum(op)
    else: return 'Not Support by the Matrix'
#Finds the rank of a matrix
def rank(X):
    global MatA, MatB,MatC,MatD,MatE,MatF,MatG,MatH,MatI,matrices,matrixlist,alpha,GenList
    matrices = [MatA,MatB,MatC,MatD,MatE,MatF,MatG,MatH,MatI,MatZ]
    XXG,D = matrices[alpha.index(X)],[]
    row = 0
    while row < XXG[0]-1:
        col,C = 2,[]
        while col < XXG[0] + 2:
            try:
                C.append((XXG[col+row*XXG[0]])/(XXG[col+XXG[0]*(row+1)]))
            except ZeroDivisionError:
                0
            col = col +1
        if len(C) > 1:
            grap = checklist(C)
        else:
            grap = 1
        if grap == 1:
            D.append(grap)
        else:
            D.append(grap)
            break
        row = row + 1
    if XXG[0] == XXG[1]:
        q = derterminat(X,0)
        matrices = [MatA,MatB,MatC,MatD,MatE,MatF,MatG,MatH,MatI]
        XXG = matrices[alpha.index(X)]
        if q != 0:
            rankk = XXG[0]
        elif 2 not in D:
            rankk = 1
        else:
            rankk = XXG[0]-1
    elif XXG[0] > XXG[1]:
        rankk = XXG[1]
    else:
        rankk = XXG[0]
    return rankk
#Compares enteries of two matrices
def checkentries(Xh,I):
    n = 1
    while n < Xh[0] + 2:
        if n == Xh[0]+1:
            return 'Sucess'
            break
        else:
            z=1
            while z < Xh[0]+1:
                o = (z-1)*Xh[1]
                if Xh[o+n+1] != I[(z-1)*Xh[0]+n-1]:
                    return z,n
                    break
                else:
                    z=z+1
        n=n+1
#Finds the inverse of a matrix
def inversemat(zz,XX,Z,C):
    global matrices,matriceS,alpha,alphA
    y = checkMat(XX)
    con=0
    if C == 0:
        Valuee = checkMat(2)
    else:
        Valuee = C
    if XX[0] != XX[0]:
        matassignment(2,0,0,[],Valuee)
        if zz == 1:
            print('This is a Non-Singular Matrix, Thus, it has no Inverse')
        return Valuee
    if derterminat(XX,0) == 0:
        matassignment(2,0,0,[],Valuee)
        if zz == 1:
             print('This is a Singular Matrix, Thus, it has no Inverse')
        return Valuee
    else:
        RR =[]
        if 'X' in XX:
            con=1
        XXX = get_Mat(0,XX)
        XXX = list(XXX)
        if XXX[0] == XXX[1]:
            I = IdentityMat(XXX[0])
            RR.append(XXX[0]);RR.append(2*XXX[0])
            del XXX[0]; del XXX[0]; del I[0]; del I[0]; n=0
            while n < RR[0]:
                col = 0
                while col < RR[0]:
                    RR.append(XXX[col + RR[0]*n])
                    col=col+1
                coll=0
                while coll < RR[0]:
                    RR.append(I[coll + RR[0]*n])
                    coll=coll+1
                n=n+1
            matassignment(2,1,2,RR,Valuee)
            def rowtransforem(Valuee,I,Z):
                global matriceS, alphA
                Xh = matriceS[alphA.index(Valuee)];U = checkentries(Xh,I)
                v = 0
                if U == 'Sucess':
                    pass
                else:
                    S = U[0]
                    S1,S2=(U[0]-1)*Xh[0]+U[1],(U[0]-1)*Xh[1]+U[1]+1
                    TL=[]; p = U[0]
                    if U[0] >= U[1]:
                        while p < Xh[0]:
                            TL.append(Xh[(p)*Xh[1] +U[1]+1])
                            p = p+1
                        if I[S1-1] in TL:
                            item_num=TL.index(I[S1-1])
                            rowopr(S,item_num+U[0]+1,1,0,0,'-',Valuee,Z)
                            v = 2
                        else:
                            if (-1)*I[S1-1] in TL:
                                item_num=TL.index((-1)*I[S1-1])
                                rowopr(S,item_num+U[0]+1,1,0,0,'-',Valuee,Z)
                                rowopr(S,U[1],2,-1,0,'+',Valuee,Z)
                            else:
                                if I[S1-1] != 0 and Xh[S2] == 0:
                                    j =0
                                    while j < len(TL):
                                        if TL[j] != 0:
                                            break
                                        j+=1
                                    rowopr(S,j+U[0]+1,1,0,0,'-',Valuee,Z)
                                        
                    while v != 2:
                        Xh = matriceS[alphA.index(Valuee)]
                        if I[S1-1]==0:
                            p = U[1]-1;j = 0
                            while p < Xh[0]:
                                TL.append(Xh[(p)*Xh[1] +U[1]+1])
                                p = p+1
                            while j < len(TL):
                                if TL[j] != 0:
                                    break
                                j+=1
                            factor = Xh[S2]/Xh[(j+U[1]-1)*Xh[1]+U[1]+1]
                            rowopr(U[0],j+U[1],2,1,factor,'-',Valuee,Z)
                        else:
                            factor = 1/Xh[S2]
                            rowopr(U[0],U[1],2,factor,0,'+',Valuee,Z)
                        v = 2
                    return rowtransforem(Valuee,I,Z)
            rowtransforem(Valuee,I,Z)
            n =0
            RR = matriceS[alphA.index(Valuee)]
            while n < RR[0]:
                coll =1
                while coll < RR[0] + 1:
                    del RR[n*(RR[0]) + 2]
                    coll=coll+1
                n=n+1
            w = RR[0]
            Val = checkMat(2)
            matassignment(2,4,6,RR,Valuee)
            mat_reoder(1,w,w,Valuee)
    return Valuee
def transpose_mat(XX,c):
    global matrices,matriceS,alpha,alphA
    XXX,RR = get_Mat(0,XX),[]
    if c == '11':
        Valuee = checkMat(2)
    else:Valuee = c
    RR.append(XXX[1]); RR.append(XXX[0]); n=0
    while n < XXX[1]:
        s = 0
        while s < XXX[0]:
            RR.append(XXX[s*XXX[1]+n+2])
            s =s+1
        n=n+1
    matassignment(2,0,1,RR,Valuee)    
    return Valuee
def show_mat(X,Z):
    global MatA, MatB,MatC,MatD,MatE,MatF,MatG,MatH,MatI,MatSys1,MatSys2,MatSys3,MatSys4,MatSys5,MatSys6,MatSys7,MatSys8,matrices,matriceS,matrixlist,matrixAns_list,alphB,alpha,alphA,MatZ
    matrices = [MatA,MatB,MatC,MatD,MatE,MatF,MatG,MatH,MatI,MatZ]
    matriceS= [MatSys1,MatSys2,MatSys3,MatSys4,MatSys5,MatSys6,MatSys7,MatSys8]
    if Z == 1:
        if X in alpha:
            XXX = matrices[alpha.index(X)]
        else:
            X=X.replace('Ans','')
            XXX = matAns[alphB.index(X)]
    else:
        XXX = matriceS[alphA.index(X)]
    row = 0;
    if XXX == [] or XXX == 'Empty':
        return 'Empty'
    elif type(XXX) == float or type(XXX) == int:
        print(XXX)
    elif len(XXX) == 1:
        print(XXX[0])
    else:
        VV,V=[],[];LL =[]
        while row < XXX[0]:
            col,L = 2,[]
            while col <= XXX[1] + 2:
                if col == XXX[1]+2:
                    print(L)
                else:
                    if int(XXX[col+row*XXX[1]]) ==  XXX[col+row*XXX[1]]:
                        L.append(int(XXX[col+row*XXX[1]]));LL.append(str(int(XXX[col+row*XXX[1]])))
                    elif type(XXX[col+row*XXX[1]]) == float:
                        b = Fraction(XXX[col+row*XXX[1]]).limit_denominator()
                        num = b.numerator; denom = b.denominator
                        if denom == 1:
                            L.append(XXX[col+row*XXX[1]]);LL.append(str(XXX[col+row*XXX[1]]))
                        else:
                            L.append(str(num)+'/'+ str(denom));LL.append(str(num)+'/'+ str(denom))
                col = col + 1
            row = row + 1


def matopr(n,S,T,D,X,Si,Y,c,cg):
    LL=[];s =2;r = 0
    if D == 1:
        XX = get_Mat(S,X)
        if type(XX) == float:
            FG =2
        else:
            FG =1
    else:
        FG = 2
    if FG == 1:
        YY = get_Mat(T,Y)
        if Si == '+':
            if XX[0] == YY[0]:
                if XX[1] == YY[1]:
                    LL.append(XX[0]);LL.append(XX[1])
                    while s < len(XX):
                        LL.append(XX[s]+YY[s])
                        s=s+1
                else:
                    r = ''
                    if n == 1:
                        print('Sorry, this Matrices are not compatible for Addition')
            else:
                r = ''
                if n == 1:
                    print('Sorry, this Matrices are not compatible for Addition')
        elif Si == '-':
            if XX[0] == YY[0]:
                if XX[1] == YY[1]:
                    LL.append(XX[0]);LL.append(XX[1])
                    while s < len(XX):
                        LL.append(XX[s]-YY[s])
                        s=s+1
                else:
                    r = ''
                    if n== 1:
                        print('Sorry, this Matrices are not compatible for Subtraction')
            else:
                r = ''
                if n == 1:
                    print('Sorry, this Matrices are not compatible for Subraction')
        else:
            if XX[1] == YY[0]:
                p=0
                LL.append(XX[0]);LL.append(YY[1])
                while p < XX[0]:
                    q=0
                    while q < YY[1]:
                        r = 0; TL=[]
                        while r <YY[0]:
                            TL.append(XX[p*XX[1]+2+r]*YY[r*YY[1]+2+q])
                            r=r+1
                        LL.append(sum(TL))
                        q =q+1
                    p = p+1
            else:
                r = ''
                if n == 1:
                    print('Sorry. this Matrices are not compatible for Multiplication')
    else:
        voll = 2
        try:
            XX = get_Mat(S,X)
        except TypeError:
            voll = 1
        YY = get_Mat(T,Y)
        if voll != 1 and type(XX) == float:
            LL = XX*YY
        elif type(YY) != float:
            LL.append(YY[0]); LL.append(YY[1])
            while s < len(YY):
                LL.append(X*YY[s])
                s=s+1
        else:
            LL.append(XX[0]); LL.append(XX[1])
            while s < len(XX):
                LL.append(Y*XX[s])
                s=s+1
    if c == 0:
        c = checkMat(3)
        matassignment(4,0,0,LL,c)
    elif c == 1:
        matassignment(2,0,0,LL,cg)
        c = cg
    else:
        c = LL
    if r == '':
        if n ==1:
            c='Error'
        else: c = ''
    else:
        c=c
    return c
def mat_calculator(x,b,c,d):
    global ACV,GenList,matrixlist
    Matlist=['A','B','C','D','E','F','G','H','I','Z','Ans1','Ans2','Ans3','1','2','3']
    recog = ['T','I','i','n','M','S','^','/','(',')',Matlist,'s','Ans1','Ans2','Ans3','1','2','3','+','-','*']
    if x == 1:
        coll = input('Enter Your Expression: ');ACV = 0;ACQ=0
    else:
        coll = x
    coll = list(coll); S = '';n = 0;s=0; f=0;F=[];t='';vi = '';og = b;
    if b == 0:
        w = checkMat(2);matassignment(2,0,0,[4],w); y = checkMat(2);matassignment(2,0,0,[4],y)
        z = checkMat(2);matassignment(2,0,0,[4],z);b = checkMat(2);matassignment(2,0,0,[4],b);c = checkMat(2);matassignment(2,0,0,[4],c); d =checkMat(2);
        g=checkMat(3);
    else:
        w,y,z = b,c,d
    nn = 0;p=0
    while nn < len(coll):
        print(coll[nn],coll[nn] in recog)
        if coll[nn].isdigit()== True or coll[nn] == ' ':
            pass
        elif coll[nn] == 'I' and nn < len(coll)-1 and coll[nn+1] == 'n':
            pass
        elif coll[nn] in Matlist:
            if 'Mat'+coll[nn] in matrixlist:
                pass
            else:print('Mat'+coll[nn] +" not defined or doesn't exist");vi = 'Error';break
        elif coll[nn] in recog:
            pass
        elif coll[nn] not in recog:
            print('Unaccepted Character', coll[n]); vi = 'Error'
        else:
            print('Invalid Expression'); vi = 'Error'            
        nn+=1
            
    while n < len(coll) and vi != 'Error':
        if p > len(coll)+5:
            vi = 'Error';break
        if coll[n].isdigit():
            t += coll[n];n+=1
            while n < len(coll):
                if coll[n].isdigit():
                    t+=coll[n]
                else: n -= 1;break
                n+=1
        elif coll[n] == 'I' and n < len(coll)-1 and coll[n+1]== 'n':
            t += 'In'; n+=2
            while n < len(coll):
                if coll[n] == 'A' and n < len(coll)-3 and coll[n+1] == 'n' and coll[n+2] == 's':
                    t+='Ans'
                    if coll[n+3] in ('1','2','3'):
                        t+=coll[n+3]
                    n+=3
                elif coll[n] in Matlist:
                    t+=coll[n];break
                elif coll[n] == '(':
                    while n < len(coll):
                        if coll[n] != ')':
                            t+=coll[n]
                        else:t+=')'; break
                        n+=1
                else: n -= 1;break
                n+=1
        elif coll[n] == 'i' and n < len(coll)-1 and coll[n+1].isdigit():
            t += 'i'; t+=coll[n+1];n+=1
        elif coll[n] == 'i':
            t += 'i'
        elif coll[n] == 'M' or coll[n] == 'T' or coll[n] == 'S':
            t += coll[n];n+=1
            while n < len(coll):
                if coll[n] == 'A' and n < len(coll)-3 and coll[n+1] == 'n' and coll[n+2] == 's':
                    t+='Ans'
                    if coll[n+3] in ('1','2','3'):
                        t+=coll[n+3]
                    n+=3
                elif coll[n] in Matlist:
                    t+=coll[n]
                elif coll[n] == '(':
                    while n < len(coll):
                        if coll[n] != ')':
                            t+=coll[n]
                        else:t+=')'; break
                        n+=1
                else: n -= 1;break
                n+=1
        elif coll[n] in ('+','-','*'):
            t += coll[n]; s = 1
        elif coll[n] == '(':
            while n < len(coll):
                if coll[n] != ')':
                    t+=coll[n]
                else:t+=')';break
                n+=1
            if n < len(coll)-1 and coll[n+1] == '^':
                t+='^';n+=2; p = n
                while n < len(coll):
                    if coll[n].isdigit():
                        t+=coll[n]
                    elif p == n and coll[n] in ('-','+'):
                        t+=coll[n];
                    else:n-=1;break
                    n+=1
        else:
            while n < len(coll):
                if coll[n] == 'A' and n < len(coll)-3 and coll[n+1] == 'n' and coll[n+2] == 's':
                    t+='Ans'
                    if coll[n+3] in ('1','2','3'):
                        t+=coll[n+3]
                    n+=3
                elif coll[n] in Matlist:
                    t+=coll[n]
                else:
                    if coll[n] == '^':
                        t+='^';n+=1;p=n
                        while n < len(coll):
                            if coll[n].isdigit():
                                t+=coll[n]
                            elif p == n and coll[n] in ('-','+'):
                                t+=coll[n]
                            else:n-=1;break
                            n+=1
                    else:n-=1;break
                n+=1
        if s == 0 and f == 0:
            F.append(t)
        elif s != 0 and s ==0:
            F.append(t)
        elif s != 0:F.append(t);s =0
        t=''
        n +=1; p+=1
    q =0
    try:
        while q < len(F) and vi != 'Error':
            LL = get_Mat(0,w);X=''
            if F[q].isdigit():
                while q < len(F)-1:
                    if F[q+1] in Matlist:
                        if F[q] == '+':
                            vi = 'Error'
                            print("Error, Numbers can't be added to Matrices. You can Only Multiply Numbers and Matrix")
                        elif F[q] == '-':
                            print("Error, Numbers and Matrices can't undergo Subtraction. You can Only Multiply Numbers and Matrix")
                        else:
                            matopr(0,1,1,2,float(F[q]),'*',F[q+1],1,z);vi = 0;q+=1;break
                    elif F[q+1] == 'i':
                        if q < len(F)-2 and F[q+2].isdigit():
                            matassignment(2,0,0,DiagonalMat(F[q+2],float(F[q])),z);q+=2;break
                        else:matassignment(2,0,0,DiagonalMat(get_Mat(0,z)[0],float(F[q])),z);q+=1;break
                            
                    elif F[q+1] == '*':
                        if F[q+2] in Matlist:
                            matopr(0,1,1,2,float(F[q]),'*',F[q+2],1,z);q+=2;break
                        elif F[q+2] == 'i':
                            if q < len(F)-3 and F[q+3].isdigit():
                                matassignment(2,0,0,DiagonalMat(F[q+3],float(F[q])),z);q+=3;break
                            else:matassignment(2,0,0,DiagonalMat(get_Mat(0,z)[0],float(F[q])),z);q+=2;break
                    elif '(' in F[q+1]:
                        q+=1
                        matopr(0,1,1,2,float(F[q-1]),'*',d,1,z);break
                    elif F[q] == '*' and '(' in F[q+2]:
                        q+=2
                        D = list(F[q]); del D[0];del D[-1]; ij =''
                        for item in D:
                            ij += item
                        bv = get_Mat(0,b);mat_calculator(ij,b,c,d);matassignment(2,0,0,bv,b);
                        matopr(0,1,1,2,float(F[q-2]),'*',d,1,z);break
                    q+=1
            elif F[q] in ('+','-','*'):        
                S = F[q]
            elif list(F[q])[0] == '(':
                if '^' in F[q]:
                    D = F[q].split('^');DF=F[q].replace('^'+D[1],'')
                    try:
                        int(D[1]);gp = 1;Dj=DF;vb = 0
                        if int(D[1]) < 1:
                            vb = 1
                        while gp < abs(int(D[1])):
                            Dj+='*'+DF;gp+=1
                        if vb == 1:
                            bv = get_Mat(0,b);mat_calculator(Dj,b,c,d);matassignment(2,0,0,bv,b);inversemat(0,d,0,z)
                        else:
                            bv = get_Mat(0,b);mat_calculator(Dj,b,c,d);matassignment(2,0,0,bv,b);matassignment(3,0,2,d,z)
                    except TypeError:
                        pass
                else:
                    D = list(F[q]); del D[0];del D[-1]; ij =''
                    for item in D: 
                        ij += item
                    bv = get_Mat(0,b);mat_calculator(ij,b,c,d);matassignment(2,0,0,bv,b);matassignment(3,2,2,z,w);matassignment(3,2,2,d,z)
            elif len(list(F[q]))> 2 and list(F[q])[0] == 'I':
                ZZ= list(F[q]);rr = 0; del ZZ[0];del ZZ[0]
                while rr < len(ZZ):
                    X+=ZZ[rr];rr+=1
                if list(X)[0] == '(' :
                    D = list(X); del D[0];del D[-1]; ij =''
                    for item in D:
                        ij += item
                    bv = get_Mat(0,b);mat_calculator(ij,b,c,d);matassignment(2,0,0,bv,b)
                    inversemat(0,d,0,z)
                else:
                    inversemat(0,X,0,z)
            elif list(F[q])[0] == 'M':
                ZZ= list(F[q]);rr = 0; del ZZ[0]
                while rr < len(ZZ):
                    X+=ZZ[rr];rr+=1
                if '(' in X:
                    D = list(X); del D[0];del D[-1]; ij =''
                    for item in X:
                        ij += item
                    bv = get_Mat(0,b);mat_calculator(ij,b,c,d);matassignment(2,0,0,bv,b);
                    Modal_mat(d,z)
                else:
                    bv = get_Mat(0,w);Modal_mat(X,z);matassignment(2,0,0,bv,w)
            elif list(F[q])[0] == 'T':
                ZZ= list(F[q]);rr = 0; del ZZ[0]
                while rr < len(ZZ):
                    X+=ZZ[rr];rr+=1
                if '(' in X:
                    X = list(X); del X[0];del X[-1]; ij =''
                    for item in X:
                        ij += item
                    bv = get_Mat(0,b);mat_calculator(ij,b,c,d);matassignment(2,0,0,bv,b);
                    transpose_mat(d,z)
                else:
                    transpose_mat(X,z)
            elif list(F[q])[0] == 'S':
                ZZ= list(F[q]);rr = 0; del ZZ[0]
                while rr < len(ZZ):
                    X+=ZZ[rr];rr+=1
                if '(' in X:
                    X = list(X); del X[0];del X[-1]; ij =''
                    for item in X:
                        ij += item
                    bv = get_Mat(0,b);mat_calculator(ij,b,c,d);matassignment(2,0,0,bv,b);
                    Spectral_mat(0,d,0,z)
                else:
                    Spectral_mat(X,z)
            elif F[q] == 'i':
                if q < len(F)-1 and F[q+1].isdigit():
                    matassignment(2,0,0,IdentityMat(F[q+1]),z);
                else:matassignment(2,0,0,IdentityMat(get_Mat(0,z)[0]),z)
            elif list(F[q])[0] in Matlist:
                if '^' in F[q]:
                    D = F[q].split('^');DF=F[q].replace('^'+D[1],'')
                    try:
                        int(D[1]);gp = 1;Dj=DF;vb = 0
                        if int(D[1]) < 1:
                            vb = 1
                        while gp < abs(int(D[1])):
                            Dj+='*'+DF;gp+=1
                        if vb == 1:
                            mat_calculator(Dj,b,c,d);inversemat(0,d,0,z)
                        else:
                            bv = get_Mat(0,b);mat_calculator(Dj,b,c,d);matassignment(2,0,0,bv,b);matassignment(3,0,2,d,z)
                    except TypeError:
                        pass
                else:
                    matassignment(3,3,2,F[q],z)

            s =0
            if b != 0:
                matassignment(2,0,0,LL,w)
            if get_Mat(0,z) == [] or get_Mat(0,z) == [4] or get_Mat(0,z) == 'Empty':
                break
            if F[q] in ('+','-','*'):
                pass
            else:
                if S != '':
                    matassignment(3,2,2,z,y);s=1
                else:
                    matassignment(3,2,2,z,w)
                if s == 1:
                    vi = matopr(1,1,1,1,w,S,y,1,z);matassignment(3,2,2,z,w);S=''
                if vi == 'Error':
                    break
            q+=1
    except ValueError:
        vi = 'Error'
    except TypeError:
        vi = 'Error'
    if og == 0:
        if vi == 'Error' or get_Mat(0,z) == [4] or get_Mat(0,z) == 'Empty':
            print('Error, No result to Display')
        else:
            print('Answer')
            show_mat(z,2)
            print('In the process A new Matrix been created:  Press\n 1. To copy it into your Matrix: ')
            res = input()
            if res == '1':
                j = checkMat(4); sil =1
                if j == 'Full':
                    print('All Matrix have been occupied, Enter the Matrix you want to copy to or press N to abort: ')
                    jj = input()
                    if jj == 'N':
                        sil = 4
                    else:
                        tty = 'Mat' + jj
                        if tty in matrixlist:
                            matassignment(3,2,1,z,jj)
                            print('You sucessfully copy the Answer to Mat' + jj)
                        else:
                            print('No such Matrix Exist')
                            sil = 4
                else:
                    matassignment(3,2,1,z,j)
                    print('You sucessfully copy the Answer to Mat' + j)
            else:
               sil=4
            if sil == 4:
                matassignment(3,2,3,z,g)
                print('The result is saved into MatAns' + g)
            else:
                pass
        print('Do you still have any expression, Press: \n 1. Re-peat   2. To Continue : ')
        bb = input()
        if bb == '1':
            return mat_calculator(1,0,0,0)
        else:
            pass        
def eignValues(X,p):
    try:
        from math_functions import NewtonRaphson as NR
        from equation import equation
        from polynomial import Multiply_function as mf
        from polynomial import standard_expr as S
        from polynomial import display as D
    except ImportError:
        print('A required File is missing, the program will now close')
        exit()
    XX = get_Mat(0,X)
    if XX[0] == XX[1]:
        if p == 0:
            YY = [];b =0;YY.append(XX[0]);YY.append(XX[0])
            while b < XX[0]:
                c = 0
                while c < XX[0]:
                    if c ==b:
                        YY.append(str(XX[b*XX[0]+c+2])+'-x')
                    else:
                         YY.append(XX[b*XX[0]+c+2])
                    c +=1
                b+=1
            XX = YY
        else:pass
        if XX[0] == 2:
            v = S('('+str(XX[2])+')'+'('+str(XX[5])+')-'+'('+str(XX[3])+')'+'('+str(XX[4])+')')
        else:
            col = 1; M  = [];op = []
            mm=checkMat(2);matassignment(2,0,0,2,mm);mn=checkMat(2);matassignment(2,0,0,2,mn)
            XC = list(XX); XX=tuple(XX);M.append(XC[2]); del XC[2]
            while col < XC[0]:
                M.append(XC[2]*(-1)**col);del XC[2];col+=1
            col= 0; XC = tuple(XC);
            while col < XC[0]:
                row = 0; temp = [];
                XXC1 = list(XC);  vol = 0
                while vol < XX[0]-1:
                    del XXC1[vol*XXC1[0] + col + 2 - vol]; vol+=1
                if len(XXC1) > 6:
                    matassignment(2,0,0,XXC1,mm); mat_reoder(1,XX[0]-1,XX[0]-1,mm)
                    op.append(mf('('+str(M[col])+')'+ '('+eignValues(mm,1)+')'))
                else:
                    matassignment(2,0,0,XXC1,mn); mat_reoder(1,XX[0]-1,XX[0]-1,mn)
                    aneqn = eignValues(mn,1)
                    op.append(mf('('+str(M[col])+')'+ '('+aneqn+')'))
                col+=1
            te = ''
            for item in op:
                if type(item) == int or type(item) == int:
                    if item < 0:
                        te+=str(item)
                    else:te+='+'+str(item)
                elif list(item)[0] == '-':
                    te += item
                else:te+='+'+item
            v = te
        if p == 0:
            v = NR(v)
            return gL(v,1)
        elif p == 1:
            return v
    else: return 'Not Support by the Matrix'
def type_mat(X):
    XX = list(get_Mat(0,X)); v = []; n =2; c = 0
    if XX[0] == XX[1]:
        vi = checkMat(2)
        v.append('Square')
        if derterminat(X,0) == 0:
            v.append('Singular')
        else:v.append('Non-Singular')
        XX = list(get_Mat(0,X))
        m=transpose_mat(X,'11');T = get_Mat(0,m)
        if XX == T:
            v.append('Symmetric')
        if XX == matopr(0,1,2,2,-1.0,'*',m,3,5):
            v.append('Skew-Symmetric')
        if XX == IdentityMat(XX[0]):
            v.append('Unit')
        matassignment(2,0,0,IdentityMat(XX[0]),vi)
        if XX == matopr(0,1,1,2,XX[2],'*',vi,3,5):
            v.append('Scalar')
        while n < len(XX):
            if XX[n] != 0:
                c+=1
            n+=1
        if c == 0:
            v.append('Null')
        else:
            c = 0
            cl=0
            while c < XX[0]:
                o = 0
                while o < XX[0]:
                    if o <= c:
                        pass
                    elif XX[c*XX[0]+o+2] != 0:
                        cl+=1
                    o+=1
                c+=1
            c = 0;ch =0
            while c < XX[0]:
                o = 0
                while o < XX[0]:
                    if o >= c:
                        pass
                    elif XX[c*XX[0]+o+2] != 0:
                        ch+=1
                    o+=1
                c+=1
            if ch == 0 and cl == 0:
                v.append('Diagonal')
            elif cl == 0:
                v.append('Lower-Triangular')
            elif ch == 0:
                v.append('Upper-Triangular')
    elif XX[1] != XX[0]:
        v.append('Non-Singular');v.append('Non-Scalar'); c,n =0,2
        while n < len(XX):
            if XX[n] != 0:
                c+=1
            n+=1
        if c == 0:
            v.append('Null')
        if XX[1] > XX[0]:
            v.append('Augmented')
    if XX == matopr(0,1,1,1,X,'*',X,3,5):
        v.append('Idempotent')
    return gL(v,0)+ ' Matrix'
def eigenVectors(X):
    try:
        from solve_eqn import Sim_eqn as S
    except ImportError:
        print('A required File is missing, the program will now close')
        exit()
    XX = get_Mat(0,X);
    try:
        eV = cf.re_getList(eignValues(X,0))
    except ValueError:
        return 'Not Supported'
    n = 0;E=[];sd = 1;ch = checkMat(2);
    while n < len(eV):
        if sd == 1:
            df = get_Mat(0,ch);sd+=1
        matassignment(2,0,0,IdentityMat(XX[0]),ch); matopr(0,1,2,2,eV[n],'*',ch,1,ch); XXX = matopr(0,1,2,1,X,'-',ch,3,ch)
        intt = list(range(2,XX[0]+1)); v, m = 0,0;eqn = [];b = 0
        if XX[0] == 2:
            vv = [1,-XXX[2]/XXX[3]]; E.append(cf.whole(vv))
        else:
            while v < XX[0]-(b+1):
                t = '';zero = 0;c = 0
                if m >= XX[0]:
                    b+=1;m=0;v = 0;eqn=[]
                    if b == XX[0]-1:
                        return 'Error'
                while c < XX[0]-(b+1):
                    s = XXX[m*XX[0]+b+c+3]
                    if s == 0:zero += 1
                    t += '+'+str(s)+'x'+str(intt[c+b]);c+=1
                t += ' = ' + str(-XXX[m*XX[0] + 2+b])
                if zero == XX[0]-(b+1):
                    pass
                else:v +=1; eqn.append(t)
                m += 1
            D = S(eqn);p = 0
            if len(D) <= XX[0] - 2:
                DD = []
                while p < XX[0]:
                    if p < XX[0] - (len(D)+1):
                        DD.append(0)
                    elif p < XX[0] - len(D):
                        DD.append(1)
                    else:
                        for i in D:
                            DD.append(i)
                    p+=1
                E.append(cf.whole(DD))
            else:
                D = D[:0] + [1] + D[0:]
                E.append(cf.whole(D))
        n += 1
    matassignment(2,0,0,df,ch)
    return E
def Modal_mat(X,c):
    XX = get_Mat(0,X); F = eigenVectors(X)
    if type(F) == str:
        print('Modal Matrix not Supported')
        return 'Modal Matrix not Supported'
    n= 0;M = [len(F),len(F)]
    while n < len(F):
        m = 0
        while m < len(F):
            M.append(F[m][n]);m+=1
        n+=1
    if c == '11':
        o = checkMat(2)
    else:
        o = c
    matassignment(2,0,0,M,o)
    if len(F) == XX[0]:
        return o
    else:return 'F'

def Spectral_mat(X,c):
    XX = get_Mat(0,X);n= 0
    try:
        eV = cf.re_getList(eignValues(X,0))
    except ValueError:
        n=10000
    if c == '11':
        o = checkMat(2)
    else:
        o = c
    
    if n>100:
        print('Spectral Matrix not Supported');matassignment(2,0,0,'Empty',o)
        return 'Spectral Matrix not Supported'
    M = [len(eV),len(eV)];
    while n < len(eV):
        m = 0
        while m < len(eV):
            if n == m:
                M.append(eV[n])
            else:M.append(0)
            m+=1
        n+=1
    matassignment(2,0,0,M,o)
    return o
def fullmatrice():
    global MatA, MatB,MatC,MatD,MatE,MatF,MatG,MatH,MatI,matrices,matrixlist,alpha
    matriceint()
    def matrixmode():
        global MatA, MatB,MatC,MatD,MatE,MatF,MatG,MatH,MatI,matrices,matrixlist,alpha
        quest = input('Press\n 1. To Create a Matrix    2. Your Matrices    3. Properties\n 4. Operations    5. Special Matrix Operations: ')
        if quest == '1':
            cr8newmat()
            return matrixmode()
        elif quest == '2':
            checkMat(1)
            print(matrixlist)
            shel = input('Select a Matrix to Continue: ')
            v = 500
            while v != 10:
                while str(shel).isdigit() == False:
                    shel = input('Error, You are to enter a digit which is the index number of the Matrix you to Edit: ')
                shel = int(shel)
                v =10
                try:
                    while shel > len(matrixlist):
                        print('Error, the digit you enter is out of range\nYou only have ', len(matrixlist),' matrices so the max integer you can eneter is ',len(matrixlist))
                        shel = input()
                        v = 10
                except TypeError:
                    shel = int(shel)
                    v = 27
            shel = int(shel)
            vv = matrixlist[shel-1]
            print('You choose ',vv)
            Type = vv.replace('Mat','')
            show_mat(Type,1)
            return matrixmode()
        elif quest == '3':
            print(matrixlist)
            shel = input('Select a Matrix to Continue: ')
            v = 500
            while v != 10:
                while str(shel).isdigit() == False:
                    shel = input('Error, You are to enter a digit which is the index number of the Matrix you to Edit: ')
                shel = int(shel)
                v =10
                try:
                    while shel > len(matrixlist):
                        print('Error, the digit you enter is out of range\nYou only have ', len(matrixlist),' matrices so the max integer you can eneter is ',len(matrixlist))
                        shel = input()
                        v = 10
                except TypeError:
                    shel = int(shel)
                    v = 27
            shel = int(shel)
            vv = matrixlist[shel-1]
            print('You choose ',vv)
            Type = vv.replace('Mat','')
            show_mat(Type,1)
            ty = type_mat(Type)
            line3 = '1. Type: ' + ty
            line1 = '2. Rank is '+ str(rank(Type))+'    3. Determinant is '+str(derterminat(Type,0))
            line2 = '3. Eigenvalues: ' + eignValues(Type,0)
            print(line3)
            print(line1)
            print(line2)
            I = inversemat(1,Type,0,0)
            print('1. Inverse: ')
            if show_mat(I,2) == 'Empty':
                print('No Inverse')
            else:
                pass
            T = transpose_mat(Type,'11')
            print('2. Transpose: ')
            show_mat(T,2)
            if 'Square' in ty:
                print('3. Modal Matrix: ');bvn = Modal_mat(Type,'11')
                try:
                    int(bvn)
                    show_mat(bvn,2)
                except TypeError:
                    print(bvn)
                except ValueError:
                    print(bvn)
                print('4. Spectral Matrix: ')
                show_mat(Spectral_mat(Type,'11'),2)
            return matrixmode()
        elif quest == '4':
            print('Ok')
            print(matrixlist)
            shel = input('Select a Matrix to Continue: ')
            v = 500
            while v != 10:
                while str(shel).isdigit() == False:
                    shel = input('Error, You are to enter a digit which is the index number of the Matrix you to Edit: ')
                shel = int(shel)
                v= 10
                try:
                    while shel > len(matrixlist):
                        print('Error, the digit you enter is out of range\nYou only have ', len(matrixlist),' matrices so the max integer you can eneter is ',len(matrixlist))
                        shel = input()
                        v = 10
                except TypeError:
                    shel = int(shel)
                    v = 27
            shel = int(shel)
            vv = matrixlist[shel-1]
            print('You choose ',vv)
            Type = vv.replace('Mat','')
            show_mat(Type,1)
            mat_calculator(1,0,0,0)
            return matrixmode()
        elif quest == '5':
            print('Ok')
            print(matrixlist)
            shel = input('Select a Matrix to Continue: ')
            v = 500
            while v != 10:
                while str(shel).isdigit() == False:
                    shel = input('Error, You are to enter a digit which is the index number of the Matrix you to Edit: ')
                shel = int(shel)
                v=10
                try:
                    while shel > len(matrixlist):
                        print('Error, the digit you enter is out of range\nYou only have ', len(matrixlist),' matrices so the max integer you can eneter is ',len(matrixlist))
                        shel = input()
                        v = 10
                except TypeError:
                    shel = int(shel)
                    v = 27
            shel = int(shel)
            vv = matrixlist[shel-1]
            print('You choose ',vv)
            Type = vv.replace('Mat','')
            show_mat(Type,1)
            #inversemat(Type,1,0)
            #eignValues(Type,0)
            Modal_mat(Type,'11')
            show_mat(Type,1)
            return matrixmode()
        else:
            pass
        return matrixmode()
    matrixmode()
alpha = ['A','B','C','D','E','F','G','H','I','Z']
alphA = ['1','2','3','4','5','6','7','8']
alphB = ['1','2','3']
MatA,MatB,MatC,MatD,MatE,MatF,MatG,MatH,MatI,MatZ,MatSys1,MatSys2,MatSys3,MatSys4,MatSys5,MatSys6,MatSys7,MatSys8,MatAns1,MatAns2,MatAns3=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
ACV,XC,detList,LL,GenList,matrixlist,matrixSys_list,matrixAns_list =0, [],[],[],[],[],[],[]
det,genVar,countt,genVar2,QQ,CHECKMAT2,CHECKMAT= 'E',0,0,0,[],0,0
Matttlist = ['MatA','MatB','MatC','MatD','MatE','MatF','MatG','MatH','MatI','MatZ','MatSys1','MatSys2','MatSys3','MatSys4','MatSys5','MatSys6','MatSys7','MatSys8','MatAns1','MatAns2','MatAns3']
matrices = [MatA,MatB,MatC,MatD,MatE,MatF,MatG,MatH,MatI,MatZ]
matAns = [MatAns1,MatAns2,MatAns3]
matriceS= [MatSys1,MatSys2,MatSys3,MatSys4,MatSys5,MatSys6,MatSys7,MatSys8]
restricted = ['MatSys1','MatSys2','MatSys3','MatSys4','MatSys5','MatSys6','MatSys7','MatSys8','MatAns1','MatAns2','MatAns3','MatZ']
fullmatrice()
