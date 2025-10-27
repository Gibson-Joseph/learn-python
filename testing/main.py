def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return "Please enter number"
    except ValueError as err:
        # err is a instance of ValueError
        return err
