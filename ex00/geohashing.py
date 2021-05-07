import sys
from antigravity import geohash 

def valid_format(date_str):
    part_date = date_str.split("-")
    try:
        if int(part_date[1]) and len(part_date[1]) == 2 and \
            int(part_date[0]) and len(part_date[0]) == 4 and \
                int(part_date[2]) and len(part_date[2]) == 2 and \
                    float(part_date[3]):
            return True
    except Exception as e:
            print(e)

def ge_hash():
    if len(sys.argv) == 4 and valid_format(sys.argv[3]) == True:
        try:
            geohash(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3].encode('utf-8'))
        except Exception as e:
            print(e)
    else:
        print("Not valid quantity of the input arguments")


if __name__ == "__main__":
    ge_hash()

# ex: 37.421542 -122.085589 2005-05-26-10458.68