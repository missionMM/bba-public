import random
import concurrent.futures
import bba


chars:str = "abcdefghijklmnopqrstuvwxyzABCEDFGIHJKLMNOPQRSTUVWXYZ0123456789~`!@#$%^&*()_-+=<,>.:;{[}] }?"
charss:str = "abcdefghijklmnopqrstuvwxyzABCEDFGIHJKLMNOPQRSTUVWXYZ0123456789~`!@#$%^&*()_-+=<,>.:;{[}]}?"
enc_char:str = charss + "~`!@#$%^&*()_-+=<,>.:;{[}]}"
bits_str:str = "01"



temp_str1:str= ""
temp_str2:str= ""
temp_str3:str= ""
temp_str4:str= ""
temp_str5:str= ""
temp_str6:str= ""
temp_str7:str= ""
temp_str8:str= ""
temp_str9:str= ""
temp_str10:str = ""

class b1:

    # function to generate the bit code ( used in while loop of the function gen_bit_code ) -- reasion for it being a seperate function is to provide additional functionality for the bit code generation mechanism
    def gen_code(size):
        temp_char = ""
        for a in range(size):
            temp_char = temp_char + bits_str[random.randint(0,1)]
        
        return temp_char

    # it generates the bit code for all the characters stored in the variable chars, it returns the generated bit code in dict formate  
    def gen_bit_code(size,gen_file):
        d1 = {}
        temp_char = ""
        l1 = []

        for p in range(len(chars)):
            temp_char = b1.gen_code(size)

            while temp_char in l1:
                print(f"[+] Found one : {temp_char}, of : {chars[p]}", style="bold red") # prints those generated values which already exists in the list and starts the replacement process
                temp_char = b1.gen_code(size)

            l1.append(temp_char) 
            d1.update(
                {
                    chars[p]:temp_char
                }
            )
            temp_char = ""
        if gen_file:
            dict1 = bba.FileDict("bit_code")
            dict1.createFile()

            for p in d1:
                dict1[p] = d1[p]

        return d1
    
    # it generates the encryption numbers for the characters, returns the generated number in the dict formate ( the value of the generated numbers depends on the x value which is supplied by the user - x value is also considered as the encryption and decryption key)
    def gen_number(dict1,x):
        prev_bit = ""
        current_bit = ""
        power = 0
        temp_number = 0
        number_dict = {}

        for p in range(len(chars)):
            for a in range(len(dict1[chars[p]])):
                current_bit = str(dict1[chars[p]])[a]
                if current_bit == prev_bit:
                    power += 1
                else:
                    temp_number = temp_number + x**power

                prev_bit = current_bit

            number_dict.update(
                {
                    chars[p]:temp_number
                }
            )
            prev_bit = ""
            temp_number = 0
            power = 0
        return number_dict
    
    def gen_dec_dict(enc_dict):
        d1 = {}
        for p in enc_dict:
            d1[enc_dict[p]] = p

        return d1

    # it is a function which generates the value of the encrypted character for a particular character at a time
    def enc_chars(number_dict,p):
        temp_char = ""

        for a in range(len(str(number_dict[chars[p]]))): # its range is upto the number length of that character

            # enc_char is variable that stored the characters which can be used to encrypt a character
            # in randint - random number b/w the a place number for the number dict p place character upto the length of the enc_char
            temp_char = temp_char + enc_char[random.randint(int(str(number_dict[chars[p]])[a]), len(enc_char)-1)]
        return temp_char

    # its generates the encryption and decryption dict, it returns the enc and dec dict in the list of dictonary in this formate
    def gen_crypt_dict(number_dict):
        temp_char = ""
        temp_number = 100000000000
        enc_dict = {}
        dec_dict = {}
        enc_list = []

        for p in range(len(chars)):
            temp_char = b1.enc_chars(number_dict,p)

            while temp_char in enc_list:
                print(f"found one enc char : {chars[p]}, enc char value : {temp_char}")
                temp_char = b1.enc_chars(number_dict,p)

            if len(temp_char) < temp_number:
                temp_number = len(temp_char)

            enc_dict.update(
                {
                    chars[p]:temp_char
                }
            )  
            enc_list.append(temp_char)
            
            temp_char = ""

        for p in range(len(chars)):
            enc_dict[chars[p]] = str(enc_dict[chars[p]])[0:temp_number]
            dec_dict.update(
                {
                    enc_dict[chars[p]][0:temp_number]:chars[p]
                }
            )    
        return [enc_dict,dec_dict]
    
    # this function encrypts the string
    def encrypt(enc_dict,string):
        enc_str = ""

        for p in range(len(string)):
            enc_str = enc_str + enc_dict[string[p]]

        return enc_str

    # this function decrypts the string
    def decrypt(enc_dict,dec_dict,string):
        dec_str = ""
        temp_char = ""


        for p in range(int(len(string)/len(enc_dict[chars[0]]))):

            temp_char = string[:len(enc_dict[chars[0]])]

            dec_str = dec_str + dec_dict[temp_char]
            string = string[len(enc_dict[chars[0]]):]

        return dec_str            

    # this is a concurrent future based decryption formate aka uses threading to decrypt a big value
    def cf_decrypt(enc_dict,dec_dict,string):

        v_len = len(enc_dict[chars[0]])

        str_len = len(string)

        total_parts = int(str_len/v_len)

        slice_number = int(((total_parts*v_len)/2))

        str1 = string[:slice_number]
        string = string[slice_number:]

        str2 = string[:slice_number]
        string = string[slice_number:]

        str3 = string[:slice_number]
        string = string[slice_number:]

        str4 = string[:slice_number]
        string = string[slice_number:]

        str5 = string[:slice_number]
        string = string[slice_number:]

        str6 = string[:slice_number]
        string = string[slice_number:]

        str7 = string[:slice_number]
        string = string[slice_number:]

        str8 = string[:slice_number]
        string = string[slice_number:]

        str9 = string[:slice_number]
        string = string[slice_number:]

        str10 = string

        # these are the threading functions
        def thread_fn1(string):
            global temp_str1
            v_len
            temp_char = ""
            for p in range(int(len(string)/len(enc_dict[chars[0]]))):

                temp_char = string[:len(enc_dict[chars[0]])]

                temp_str1 = temp_str1 + dec_dict[temp_char]
                string = string[len(enc_dict[chars[0]]):]

        def thread_fn2(string):
            global temp_str2
            v_len
            temp_char = ""
            for p in range(int(len(string)/len(enc_dict[chars[0]]))):

                temp_char = string[:len(enc_dict[chars[0]])]

                temp_str2 = temp_str2 + dec_dict[temp_char]
                string = string[len(enc_dict[chars[0]]):]                

        def thread_fn3(string):
            global temp_str3
            v_len
            temp_char = ""
            for p in range(int(len(string)/len(enc_dict[chars[0]]))):

                temp_char = string[:len(enc_dict[chars[0]])]

                temp_str3 = temp_str3 + dec_dict[temp_char]
                string = string[len(enc_dict[chars[0]]):]

        def thread_fn4(string):
            global temp_str4
            v_len
            temp_char = ""
            for p in range(int(len(string)/len(enc_dict[chars[0]]))):

                temp_char = string[:len(enc_dict[chars[0]])]

                temp_str4 = temp_str4 + dec_dict[temp_char]
                string = string[len(enc_dict[chars[0]]):]

        def thread_fn5(string):
            global temp_str5
            v_len
            temp_char = ""
            for p in range(int(len(string)/len(enc_dict[chars[0]]))):

                temp_char = string[:len(enc_dict[chars[0]])]

                temp_str5 = temp_str5 + dec_dict[temp_char]
                string = string[len(enc_dict[chars[0]]):]

        def thread_fn6(string):
            global temp_str6
            v_len
            temp_char = ""
            for p in range(int(len(string)/len(enc_dict[chars[0]]))):

                temp_char = string[:len(enc_dict[chars[0]])]

                temp_str6 = temp_str6 + dec_dict[temp_char]
                string = string[len(enc_dict[chars[0]]):]

        def thread_fn7(string):
            global temp_str7
            v_len
            temp_char = ""
            for p in range(int(len(string)/len(enc_dict[chars[0]]))):

                temp_char = string[:len(enc_dict[chars[0]])]

                temp_str7 = temp_str7 + dec_dict[temp_char]
                string = string[len(enc_dict[chars[0]]):]

        def thread_fn8(string):
            global temp_str8
            v_len
            temp_char = ""
            for p in range(int(len(string)/len(enc_dict[chars[0]]))):

                temp_char = string[:len(enc_dict[chars[0]])]

                temp_str8 = temp_str8 + dec_dict[temp_char]
                string = string[len(enc_dict[chars[0]]):]

        def thread_fn9(string):
            global temp_str9
            v_len
            temp_char = ""
            for p in range(int(len(string)/len(enc_dict[chars[0]]))):

                temp_char = string[:len(enc_dict[chars[0]])]

                temp_str9 = temp_str9 + dec_dict[temp_char]
                string = string[len(enc_dict[chars[0]]):]

        def thread_fn10(string):
            global temp_str10
            v_len
            temp_char = ""
            for p in range(int(len(string)/len(enc_dict[chars[0]]))):

                temp_char = string[:len(enc_dict[chars[0]])]

                temp_str10 = temp_str10 + dec_dict[temp_char]
                string = string[len(enc_dict[chars[0]]):]+ dec_dict[string[0:v_len]]


        # here we are generating 10 threads in total 
        with concurrent.futures.ThreadPoolExecutor(max_workers=0.01) as executor:
            future = []
            future.append(executor.submit(thread_fn1,str1))
            future.append(executor.submit(thread_fn2,str2))
            future.append(executor.submit(thread_fn3,str3))
            future.append(executor.submit(thread_fn4,str4))
            future.append(executor.submit(thread_fn5,str5))
            future.append(executor.submit(thread_fn6,str6))
            future.append(executor.submit(thread_fn7,str7))
            future.append(executor.submit(thread_fn8,str8))
            future.append(executor.submit(thread_fn9,str9))
            future.append(executor.submit(thread_fn10,str10))
            
            for future in concurrent.futures.as_completed(future):

                future.result()

        global temp_str1
        global temp_str2
        global temp_str3
        global temp_str4
        global temp_str5
        global temp_str6
        global temp_str7
        global temp_str8
        global temp_str9
        global temp_str10


        dec = temp_str1+temp_str2+temp_str3+temp_str4+temp_str5+temp_str6+temp_str7+temp_str8+temp_str9+temp_str10
        temp_str1 = ""
        temp_str2 = ""
        temp_str3 = ""
        temp_str4 = ""
        temp_str5 = ""
        temp_str6 = ""
        temp_str7 = ""
        temp_str8 = ""
        temp_str9 = ""
        temp_str10 = ""
        return dec



