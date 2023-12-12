//This file is temporarily used as an input file

#include "InputParameters.h"
#include "Constants.h"

#include <string>
#include <vector>
#include <map>
#include <iostream>

typedef std::array<int, 3> Id_3d;

InputParameters::InputParameters() : _cell_count(3), _r_min(3), _r_max(3),
    
    //Enter the number of materials in the problem
    _materials_count(1)
{
    //Enter the number of cells in each dimension (x,y,z)
    _cell_count = {2, 3, 2};

    //Enter the coordinates of the minimum and maximum points in the mesh
    _r_min = {0, 0, 0};
    _r_max = {100, 10, 10};

    //Enter cross sections of each material
    //index is the material id
    //0 in pair is scattering
    //1 in pair is absorption 
    _cross_sections.push_back({{0, 0.05},
                               {1, 0.12}});

    int n_cells = 1;
    int n_dim = 3;

    for (int i = 0; i < n_dim; ++i)
        n_cells *= _cell_count[i];
    
    //Enter cell material map

    for (int i=0; i < _cell_count[0]; ++i)
    {
        for (int j=0; j < _cell_count[1]; ++j)
        {
            for (int k=0; k < _cell_count[2]; ++k)
            {
                Id_3d cell_id = {i,j,k};
                _cell_material_map[cell_id] = 0; 
            }
        }
    }
        

} //End of input file

std::vector<int> InputParameters::cellCount()
{ return _cell_count; }

std::vector<double> InputParameters::rMin()
{ return _r_min; }

std::vector<double> InputParameters::rMax()
{ return _r_max; }

int InputParameters::materialsCount()
{ return _materials_count; }

std::vector<std::map<int, double>> InputParameters::crossSections()
{ return _cross_sections; }

//maps each cell with its material
//each cell has one material only but each material can have many cells
std::map<Id_3d, int> InputParameters::cellMaterialMap()
{ return _cell_material_map; }