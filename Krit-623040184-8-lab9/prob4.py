from abc import ABC, abstractmethod


class Image(ABC):

    @abstractmethod
    def save_image(self, filename):
        print(f"saving bitmap file {filename}")

    @abstractmethod
    def load_image(self, filename):
        print(f"loading bitmap file {filename}")


class Bitmap(Image):
    def save_image(self, filename):
        super(Bitmap, self).save_image(filename)

    def load_image(self, filename):
        super(Bitmap, self).load_image(filename)


class Jpeg(Image):
    def save_image(self, filename):
        super(Jpeg, self).save_image(filename)

    def load_image(self, filename):
        super(Jpeg, self).load_image(filename)


if __name__ == '__main__':
    bitmap1 = Bitmap()
    bitmap1.save_image("kku.bmp")
    bitmap1.load_image("kku.bmp")
    jpeg1 = Jpeg()
    jpeg1.save_image("en.jpg")
    jpeg1.load_image("en.jpg")
