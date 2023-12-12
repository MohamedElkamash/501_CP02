#pragma once

#include <vector>



class Surface
{
    public:
    //constructor
    Surface(int id, int axis, double coordinate);

    //returns the id of the surface
    int id();

    //returns the axis of the surface
    int axis();

    //returns the coordinate of the surface
    double coordinate();

    private:

    //id of the surface
    int _id;

    //axis perpendicular to the surface (x = 0, y = 1, z = 2)
    int _axis;

    //coordinate of the surface
    double _coordinate;
};