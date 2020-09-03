def check_jpg(arr):
    if len(arr) >= 4:
        a = arr[0] == 255 
        b = arr[1] == 216 
        c = arr[2] == 255 
        d = arr[3] >= 224 
        e = arr[3] <= 239
        return a and b and c and d and e
    else:
        return False

# Save jpg
def create_jpg(inp, out, arr, count):
    out.write(arr)
    while(True):
        arr = inp.read(count)
        if arr != '':
            if not check_jpg(arr):
                out.write(arr)
            else:
                return arr
        else:
            break

def recover(path, dest):
    count = 512
    inp = open(path, "rb")
    
    i = 0
    jpg_file = open('image/img1.jpg', 'wb+')
    while(True):
        arr = inp.read(count)
        if len(arr) < 512:
            inp.close()
            jpg_file.close()
            return i
        if arr != '': 
            if check_jpg(arr):
                i += 1
                if i == 1:
                    jpg_file.write(arr)
                else:
                    jpg_file.close()
                    jpg_file = open(f'{dest}/img' + str(i) + '.jpg', 'wb+')
                    jpg_file.write(arr)
            else:
                if i >= 1:
                    jpg_file.write(arr)
        else:
            inp.close()
            return i
            break

if __name__ == "__main__":
    print("Does not mean to be executed Directly")
    pass