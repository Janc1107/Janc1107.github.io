# 2020/3/18
# CSUF CPSC 386 Midterm

class Ship:
	def __init__(self, vector=Vector()):
		self.v = vector
		self.screen_rect = game.screen.get_rect()
		self.image = pg.image.load("shipimage")
		self.rect = self.image.get_rect()
		self.rect.midbottom = self.screen_rect.midbottom
		self.laser = pg.sprite.Group()

	def center_ship(self):
		self.rect.midbottom = self.screen_rect.midbottom

	def fire(self):
		laser = Laser()
		self.laser.add(laser)

	def remove_lasers(self):
		self.laser.remove()

	def move(self):
		if self.v == Vector():
			return
		self.rect.left += self.v.x
		self.rect.top += self.v.y

	def draw(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		self.move()
		self.draw()


class Vector:
	def __init__(self,x=0.0, y=0.0):
		self.x = x
		self.y = y

	def __repr__(self):
		return "Vector ({}, {})".format(self.x, self.y)

	def __add__(self, other):
		return Vector(self.x+other.x, self.y+other.y)

	def __sub__(self, other):
		return Vector(self.x-other.x, self.y-other.y)

	def __rmul__(self, k: float):
		return Vector(self.x*k, self.y*k)

	def __mul__(self, k: float):
		return self.__rmul__(k)

	def __truediv__(self, k: float):
		return Vector(self.x/k, self.y/k)

	def __neg__(self):
		self.x *= -1
		self.y *= -1

	def __eq__(self):
		return self.x == other.x and self.y == other.y

@staticmethod
def test(): # feel free to change the test code
	v = Vector(x=5, y=5)
	u = Vector(x=4, y=4)
	print("v is {}".format(v))
	print("u is {}".format(u))
	print("u+v is {}".format(u + v))
	print("u-v is {}".format(u - v))
	print("ku is {}".format(3 * u))
	print("-u is {}".format(-1 * u))


def main():
	Vector.test()