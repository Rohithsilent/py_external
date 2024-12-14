def divide(a,b):
    try:
       result =a/b
    except ZeroDivisionError as e:
        print("zero divison error",e)
    except TypeError:
        print("invalid input")
    except Exception as e:
        print(e)
    else:
        print(result)
    finally:
        print("executed")

divide(10,2)
divide(10,0)
divide(10,"a")
