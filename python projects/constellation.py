from PIL import Image, ImageOps
import glob
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing


NO_OF_POINTS = 6
class Star:
    def __init__(self, x, y, brightness):
        self.x = x
        self.y = y
        self.brightness = brightness

 
def get_normed_predictors(file, no_of_points, rotation=0):
    im = Image.open(file)
    im = im.resize((100,round(im.height*100/im.width)), Image.ANTIALIAS)
    im = im.rotate(rotation)
    

    im = ImageOps.grayscale(im)
    
    pix = im.load()

    starlist = []
    for x in range(im.width):
        for y in range(im.height):
            if im.getpixel((x,y)) > 100: 
                starlist.append(Star(x,y,im.getpixel((x,y))))
            #if len(starlist) < NO_OF_POINTS:
            #    starlist = [] 
            #    if im.getpixel((x,y)) > 150: 
            #        starlist.append(Star(x,y,im.getpixel((x,y))))

    starlist.sort(reverse=True, key=lambda x: x.brightness)
    starlist = starlist[0:no_of_points]

    dbeo = []       #distances between each other
    for star1 in starlist:
        for star2 in starlist:
            if star1 != star2:
                dbeo.append(((star1.x-star2.x)**2 + (star1.y-star2.y)**2)**0.5)

    dbeo = [float(i)/sum(dbeo) for i in dbeo]
    return dbeo

    '''
        starlist.sort(reverse=True, key=lambda x: x.brightness)
        starlist = starlist[0:no_of_points]

        anotherset = []
        for star in starlist:
            anotherset.append(star.x)
            anotherset.append(star.y)    
        return anotherset
    '''
        
    


const_pngs = glob.glob("c:/Users/Mishal/Desktop/constellations/*.png")
predictors = []
for png in const_pngs:    
    predictors.append(get_normed_predictors(png, NO_OF_POINTS))
    predictors.append(get_normed_predictors(png, NO_OF_POINTS, 90))
    predictors.append(get_normed_predictors(png, NO_OF_POINTS, 180))
    predictors.append(get_normed_predictors(png, NO_OF_POINTS, 270))
    predictors.append(get_normed_predictors(png, NO_OF_POINTS, 360))
    predictors.append(get_normed_predictors(png, NO_OF_POINTS, 450))

dict_of_consts = {}
i = 1
for png in const_pngs:
    dict_of_consts[i] = png.split("\\")[-1]
    i = i + 1
outcomes = []
for num in dict_of_consts.keys():
    outcomes.append(num)
    outcomes.append(num)
    outcomes.append(num)
    outcomes.append(num)
    outcomes.append(num)
    outcomes.append(num)
#important files are dict_of_consts and predictors


knn = KNeighborsClassifier(n_neighbors = 1)
#standard_predictors = preprocessing.scale(predictors)
knn.fit(predictors, outcomes)


sk_predictions = knn.predict(predictors)

#print(im.width)
#print(im.height)
#print(im.width * im.height)
#print(len(starlist))
#print(type(pixellist[0]))
#print(starlist)
#for star in starlist:
#    print((star.x, star.y, star.brightness))
#print(starlist)
#print(dbeo)
#print(list_of_predictors)
#print(const_pngs)
#print(sk_predictions)

#test = get_normed_predictors("c:/Users/Mishal/Desktop/constellations/ursa_major.png", NO_OF_POINTS, 90)
#testing = []
#for i in range(10):
#    testing.append(test)
#knn.predict(testing)

