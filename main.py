
from service import add_ci_to_reestr, cls_cnsl, see_all_ci_in_reestr, see_N_last_added
from service import remove_ci_from_reestr, clear_reestr, statistics, import_ci_from_csv        

print('Welcome to reestr Mi app!')
while True:
    while True:
        print("""
        1. Add Mi to reestr;
        2. See all Mi in reestr;
        3. See N last added Mi in reestr;
        4. Remove Mi from reestr;
        5. Remove all Mi from reestr;
        6. See statistics;
        7. Import Mi from csv;
        8. Exit\n""")
    
        inp = input('What want you do? Please, write the number of action:')
        try:
            action = int(inp)
            break
        except:
            print('You should write just a number of ation. Try again.')
    
    cls_cnsl()
    match action:
        case 1:
            add_ci_to_reestr()
        case 2:
            see_all_ci_in_reestr()
        case 3:
            see_N_last_added()    
        case 4:
            remove_ci_from_reestr()
        case 5:
            clear_reestr()
        case 6:
            statistics()
        case 7:
            import_ci_from_csv()
        case 8:
            print('Goodbye!')
            break