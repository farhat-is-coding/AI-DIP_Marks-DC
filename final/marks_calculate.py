import cv2


def convert_string(string):
    string = string.replace('o', '0')
    string = string.replace('i', '1')
    string = string.replace('I', '1')
    string = string.replace('L', '1')
    string = string.replace('|', '1')
    string = string.replace('l', '1')
    string = string.replace('`', '1')
    string = string.replace('s', '5')
    string = string.replace('S', '5')
    string = string.replace('z', '2')
    string = string.replace('b', '6')
    string = string.replace('B', '8')
    string = string.replace('.', '')
    string = string.replace('-', '')
    string = string.replace(' ', '')

    return string

def GetMarks(image_path, reader):
    numbers = 0
    print(image_path)
    # reader = easyocr.Reader(['en'])
    image = cv2.imread(image_path, 0)
    result = reader.readtext(image)
    print(result)
    if len(result) == 0:
        return 0
    print('before returning', result[0][1])
    return int(convert_string(result[0][1]))

def GetRollNo(image_path, reader):
        
    # reader = easyocr.Reader(['en'])
    image = cv2.imread(image_path, 0)

    result = reader.readtext(image)

    if len(result) == 0:
        return ''
    
    print(result[-1][1])
    return convert_string(result[-1][1])

def GetSubject(image_path, reader):
    # reader = easyocr.Reader(['en'])
    image = cv2.imread(image_path, 0)

    result = reader.readtext(image)
    if len(result) == 0:
        return ''
    print(result)
    return result[-1][1]   