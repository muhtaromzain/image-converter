from PIL import Image
import PIL
import os
import magic
import glob
import shutil

# set global variables
# path = os.getcwd() + '\\image'
# convertPath = os.getcwd() + '\\converted'

class converter():
    path        = ''
    convertPath = ''
    
    def __init__(self, path, convertPath):
        self.path        = path
        self.convertPath = convertPath
    
    def run(self):
        images = self.getListImages()

        for image in images:
            # check if image file
            mime = self.checkMimeType(image).split('/')

            if (mime[0] == 'image'):
                # accept only jpg, png and webp
                if (mime[1] == 'jpeg' or mime[1] == 'png' or mime[1] == 'webp'):
                    # check if webp
                    if (mime[1] != 'webp'):
                        # convert image
                        print('convert ' + image)
                        self.convertImage(image)
                    else:
                        # check if mime is not same with ext name
                        orgImageExt = image.split('.')[1]
                        if (orgImageExt != mime[1]):
                            # rename and save the with correct ext
                            print('Rename and copy ' + image)
                            src = self.path + '\\' + image
                            dst = self.convertedPath + '\\' + image.split('.')[0] + '.webp'
                            shutil.copyfile(src, dst)
                        else:
                            # move and copy current webp image
                            print('Move and copy ' + image)
                            src = self.path + '\\' + image
                            dst = self.convertedPath + image
                            shutil.copyfile(src, dst)

    def checkMimeType(self, image, isOrigin = True):
        # mime reader
        mime = magic.Magic(mime=True)
        if (isOrigin):
            convertedPath = self.convertImagePath(image)
        else:
            convertedPath = self.destinationPath(image)
        mimeType = mime.from_file(convertedPath)
        return mimeType

    def convertImagePath(self, image):
        return self.path + "\\" + image

    def destinationPath(self, image, image_type = ''):
        if (image_type == 'jpg' or image_type == 'jpeg' or image_type == 'png' or image_type == 'webp'):
            ext = '.' + image_type
        else :
            ext = '.webp'
        
        image = image.split('.')[0]
        return self.convertPath + "\\" + image + ext

    def getListImages(self):
        dirList = os.listdir(self.path)
        return dirList

    def convertImage(self, image, image_type = ''):
        if (image_type == 'jpg' or image_type == 'jpeg' or image_type == 'png' or image_type == 'webp'):
            ext = image_type
        else :
            ext = 'webp'

        convertImage = Image.open(self.convertImagePath(image))
        convertImage = convertImage.convert('RGBA')

        try:
            convertImage.save(self.destinationPath(image), ext)
            return True
        except Exception as e:
            return e

# if __name__ == "__main__":
    # app = converter()
    # app.run()