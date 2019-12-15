import sys
path = "D:\\All_Projs\\amazon_proj\\maya_converter_calc"#provide path where you are saving the script
if path in sys.path:
    print "path already exists"
else:
    print "path does not exist"
    sys.path.append(path)

def main():
    """
    The main function is to run the code and exit on recalling the tool
    Returns:
        None
    """
    # CAVEAT: "win" var is global so that it can be used in multiple situations in the script
    global window
    # CAVEAT: first it will try to close if the win exist
    try:
        window.close()
    except:
        pass
    window = maya_converter_calc_func.MayaConverterCalcFunc()
    # CAVEAT: if the exception is raised the window will be shown
    window.show()

main()
