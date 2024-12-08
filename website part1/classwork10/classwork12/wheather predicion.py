weather=(1,1,1,1,0,0,0,1,1,1)
sun=weather.count(0)
rain=weather.count(1)
if sun>rain:
    print("it is a sunny day")
else:
    print("its is a  rainy day")

