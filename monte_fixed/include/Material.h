#pragma once

#include <string>
#include <map>

/*This class describes material cross sections*/

class Material
{
    public:
    
    //Constructor
    Material(int id, std::map<int, double> cross_sections);

    //returns material id
    int id();
    
    //returns cross sections of the material
    std::map<int, double> crossSections();

    //returns the total cross section of the material
    double totalXS();

    private:

    //material id
    int _id;
    
    //macroscopic cross sections in units cm^-1
    std::map<int, double> _cross_sections;
};