#pragma once

#include "Material.h"
#include "Surface.h"
#include <array>
#include <vector>

/*This class describes the cell. 
A cell consists of two surfaces and a material.*/

class Cell
{
    typedef std::array<int, 3> Id_3d;

    public:

    //constructor
    Cell(Id_3d id, std::vector<Surface> surfaces, const Material & material);

    /* Cell(Cell & cell); */

    //returns the id of the cell
    Id_3d id();

    //returns the surfaces bounding the cell
    std::vector<Surface> surfaces();

    //returns the material inside the cell
    Material material();

    private:

    //id of the cell
    Id_3d _id;

    //list of surfaces bounding the cell
    std::vector<Surface> _surfaces;

    //material inside the cell
    const Material & _material;
};
