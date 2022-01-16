from PIL import Image, ImageOps

NO_OF_POINTS = 5

checknorth = {"andromeda":"1", "aries":"1", "auriga":"1", "bootes":"1", "aquarius":"1", "aquila":"1", "ursa_major":"1", "antlia":"0", "apus":"0", "ara":"0"}
checksouth = {"aquarius":"1", "aquila":"1", "antlia":"1", "apus":"1", "ara":"1", "andromeda":"0", "aries":"0", "auriga":"0", "bootes":"0", "ursa_major":"0"}

class Star:
    def __init__(self, x, y, brightness):
        self.x = x
        self.y = y
        self.brightness = brightness


def get_normed_predictors(file, rotat=0, resize=True):
    predictorlist = []
    im = Image.open(file)
    if resize:
        im = im.resize((100,round(im.height*100/im.width)), Image.ANTIALIAS)
    im = ImageOps.grayscale(im)

    
    im = im.rotate(rotat)
    pix = im.load()

    starlist = []
    for x in range(im.width):
        for y in range(im.height):
            if im.getpixel((x,y)) > 100: 
                starlist.append(Star(x,y,im.getpixel((x,y))))

    starlist.sort(reverse=True, key=lambda x: x.brightness)
    starlist = starlist[0:NO_OF_POINTS]

    dbeo = []       #distances between each other
    for star1 in starlist:
        for star2 in starlist:
            if star1 != star2:
                dbeo.append(((star1.x-star2.x)**2 + (star1.y-star2.y)**2)**0.5)
    #for star in starlist:
    #    dbeo.append(star.x-starlist[0].x)
    #    dbeo.append(star.y-starlist[0].y)


    #normeddbeo = [float(i)/sum(dbeo) for i in dbeo]
    return dbeo