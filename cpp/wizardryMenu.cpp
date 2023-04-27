#include <iostream>

class Weapon {       // The class
  public:             // Access specifier
    std::string name;
};

class Actor{
	public:
		std::string name;
		Weapon equippedWeapon;
};


int main(){
	printf("dinner when");
	return 0;
}