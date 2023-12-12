#pragma once

#include "Cell.h"
#include <array>

/*This class contain the main functionality of the neutron
*/

class Neutron
{
    public:

    //constructor
    Neutron(int id, std::array<double, 3> position, std::array<double, 3> mu);

    //returns the id of the neutron
    int id();

    //returns the neutron position
    std::array<double, 3> position();

    //returns the current cosine of the polar angle of the neutron relative to each axis
    std::array<double, 3> mu();

    //updates the neutron x-coordinate
    void updatePosition(std::array<double, 3> x);

    //updates the neutron cosine polar angle
    void updateMu(std::array<double, 3> mu);
    
    private:

    //neutron id
    int _id;

    //position
    std::array<double, 3> _position;

    //cosine the polar angle of the neutron relative to each axis
    std::array<double, 3> _mu;
};