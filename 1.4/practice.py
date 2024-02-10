from platform import version
from platform import system
from platform import processor
from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))

print(processor())

print(system())

print(version())
