def check_switches(args, switches=None, delimiter="-"):
    """
    Maps argv variable to usable dictionary
    :param args: argv variable from sys.argv
    :param switches: Optional list of required/optional switches, switches w/argument or singular
    :param delimiter: String used to denote a switch. Defaults to a dash
    :return: Dictionary of args bound to their switch
    """
    # Dictionary assigned with all args and their values
    count = 0
    parsed_args = {}
    for i in range(1, len(args)):
        if delimiter in list(args[i])[0]:
            if switches is None:
                try:
                    if delimiter in list(args[i+1])[0]:
                        parsed_args[args[i]] = True
                        count += 1
                    else:
                        parsed_args[args[i]] = args[i + 1]
                except IndexError:
                    # Assume if index error, there is a singular switch at the end of the file
                    parsed_args[args[i]] = True
                    count += 1
            else:
                if any(x in args[i] for x in switches):
                    try:
                        if delimiter in list(args[i+1])[0]:
                            parsed_args[args[i]] = True
                            count += 1
                        else:
                            parsed_args[args[i]] = args[i + 1]
                    except IndexError:
                        # Assume if index error, there is a singular switch at the end of the file
                        parsed_args[args[i]] = True
                        count += 1
                else:
                    print(f"Bad option {args[i]}. Quitting")
                    raise SystemExit
    # check if the args dictionary matches what was given in the command
    # Minus 1 because we don't count the name of the program, add the count value back for correct number
    if len(parsed_args) * 2 != len(args) - 1 + count:
        print("Malformed command. Possible spaces in source or destination paths. Use quotations around paths"
              " if there are spaces.")
        raise SystemExit
    else:
        return parsed_args

