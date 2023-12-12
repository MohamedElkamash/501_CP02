#pragma once

#include "InputParameters.h"
#include "Material.h"
#include "Surface.h"
#include "Cell.h"
#include "Neutron.h"
#include "Constants.h"

#include <string>
#include <vector>

/* This class carries all the information of the geometry. 
The geometry consists of a vector of cells.
Also the geometry carries a vector of materials to carry all the cross sections of all the materials in the problem
*/


class Geometry
{
    typedef std::map<std::array<int, 3>, Cell> Mesh;

    public:

    //constructor
    Geometry(InputParameters & parameters);

    //returns vector of surfaces positions
    std::map<int, std::vector<Surface>> surfaces();

    //returns map of cells in the domain
    Mesh cells();

    //returns a vector of the materials in the domain
    std::vector<Material> materials();

    //returns number of cells in the domain
    std::vector<int> cellCount();

    //returns the minimum coordinates of the of the domain
    std::vector<double> rMin();

    //returns the maximum coordinates of the of the domain
    std::vector<double> rMax();

    //returns the width of the domain in all dimensions
    std::vector<double> domainWidth();

    //returns cell width in all dimensions
    std::vector<double> cellWidth();

    //returns number of materials in the domain
    int materialCount(); 


    private:

    //number of cells 
    std::vector<int> _cell_count;

    //minimum point coordinates in the mesh
    std::vector<double> _r_min;

    //maximum point coordinates in the mesh
    std::vector<double> _r_max;

    //cell width
    std::vector<double> _cell_width;

    //carrying surfaces positions
    std::map<int, std::vector<Surface>> _surfaces;

    //carrying cells 
    Mesh _cells;

    //carrying materials information
    std::vector<Material> _materials;
};