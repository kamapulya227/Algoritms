#include <iostream>
#include <unordered_map>

int main() {
    std::unordered_map<std::string, bool> myMap;

    myMap["light"] = true;
    myMap["door"] = false;
    myMap["window"] = true;
    
    for (const auto& pair : myMap) {
        std::cout << pair.first << ": " << (pair.second ? "on" : "off") << std::endl;
    }

    return 0;
}
