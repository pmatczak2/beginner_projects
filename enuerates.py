new_list = ('dog', 'duck', 'chicken', 'goat')
print(list(enumerate(new_list, start=12)))  #  enumertes  have a index stat at any index number is
                                            #  assinged. pass the start peramiter with the assinged
                                            #  value and the index will start from that piont

type(enumerate(new_list))

for index, value in enumerate(new_list):
    print(f"The index number is: {index}. The value is: {value}.")