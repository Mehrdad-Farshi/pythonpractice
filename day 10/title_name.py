# what i did 
def format_name(fir_name,las_name):
    fir_name = fir_name.lower()
    las_name = las_name.lower()
    fir_name = fir_name[0].upper() + fir_name[1 :]
    las_name = las_name[0].upper() + las_name[1 :2]
    return (f'{fir_name} {las_name}')

print(format_name('mehrdad','farshi'))

# what class told me 

def title_name (fir_name,las_name):
    fir_name=fir_name.title()
    las_name=las_name.title()
    return (fir_name,las_name[0:2])
print(title_name('mehrdad','farshi'))


# function output 