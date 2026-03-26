# Import classes from your brand new package
import animals

# Create an object of Mammals class & call a method of it
myMammal = animals.Mammals()
myMammal.printmembers()

# Create an object of Birds class & call a method of it
myBird = animals.Birds()
myBird.printmembers()

# Create an object of Fish class & call a method of it
myFish = animals.Fish()
myFish.printmembers()

# Created overridden Bird class in separate folder to give it its own name space
harmless_birds = animals.harmless.Birds()       
harmless_birds.printmembers()

# Created overridden Fish class in separate folder to give it its own name space
harmless_fish = animals.dangerous.Fish()       
harmless_fish.printmembers()

